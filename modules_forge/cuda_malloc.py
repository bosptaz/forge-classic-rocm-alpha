# reference: https://github.com/Comfy-Org/ComfyUI/blob/master/cuda_malloc.py

import importlib.util
import os.path
import subprocess


def get_gpu_names() -> set[str]:
    gpu_names = set()
    out = subprocess.check_output(["rocm-smi", "--showproductname"], text=True)
    for l in out.splitlines():
        if len(l) > 0:
            gpu_names.add(l.strip())
    return gpu_names


def cuda_malloc_supported() -> bool:
    # ROCm-only fork: cudaMallocAsync-style allocation is a NVIDIA feature.
    # On ROCm the torch HIP allocator handles this natively, so skip it.
    return False


try:
    torch_spec = importlib.util.find_spec("torch")
    for folder in torch_spec.submodule_search_locations:
        ver_file = os.path.join(folder, "version.py")
        if os.path.isfile(ver_file):
            spec = importlib.util.spec_from_file_location("torch_version_import", ver_file)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            version = module.__version__
except Exception:
    version = ""


def try_cuda_malloc():
    if not cuda_malloc_supported():
        return

    env_var = os.environ.get("PYTORCH_CUDA_ALLOC_CONF", None)

    if env_var is None:
        env_var = "backend:cudaMallocAsync"
    else:
        env_var += ",backend:cudaMallocAsync"

    os.environ["PYTORCH_CUDA_ALLOC_CONF"] = env_var


def try_expandable_segments():
    env_var = os.environ.get("PYTORCH_ALLOC_CONF", None)

    if env_var is None:
        env_var = "expandable_segments:True"
    else:
        env_var += ",expandable_segments:True"

    os.environ["PYTORCH_ALLOC_CONF"] = env_var


def get_torch_version() -> str:
    return str(version)
