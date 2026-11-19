# SD WebUI Forge Classic (ROCm)

Native AMD ROCm port of [SD WebUI Forge Classic](https://github.com/Haoming02/sd-webui-forge-classic/tree/neo). Built for CachyOS and modern AMD GPUs (RX 7000 series / gfx1101) without CUDA dependencies.

pacman -S git python3.13 uv rocm-smi

./webui.sh

Base Model
Illustrious

Steps: 24, Sampler: Euler a, Schedule type: Automatic, CFG scale: 4.5, Seed: xxxxxxxxx, Size: 1024x1024, Model: xxxxxxx, Model hash: xxxxxxxxx, RNG: CPU, Emphasis: Original, Version: neo-2.32
Time taken: 15.2 sec.
A: 12.39 GB, R: 12.66 GB, Sys: 13.2/15.9844 GB (82.8%)

version: neo  •  python: 3.13.15  •  torch: 2.12.1+rocm7.1  •  gradio: 4.40.0  •  checkpoint:
