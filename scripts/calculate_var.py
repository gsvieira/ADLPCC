from pathlib import Path
import numpy as np

betas = [500, 1000, 2000, 3000]
Experiment = 4
basepath = f"/home/gabriel/PCC_fernando/results/ADLPCC/Experiment_{Experiment}/"

for lamb in betas:
    dirpath = Path(basepath).joinpath(f"beta_{lamb}")
    files = sorted(dirpath.glob("*.txt"))
    for file in files:
        bpp = []
        psnr = []
        with open(file) as f:
            lines = f.readlines()
            for line in lines: 
                if "bpp: " in line:
                    bpp.append(float(line[4:-1]))
                elif "psnr:" in line:
                    psnr.append((float(line[5:-1])))
        # print(bpp)
        npbpp = np.array(bpp)
        nppsnr = np.array(psnr)
        # print(npbpp.mean())
        # print(npbpp.var())
        with open(file, "a") as f:
            f.write("BPP\n")
            f.write(f"mean: {npbpp.mean()}\n")
            f.write(f"var: {npbpp.var()}\n")
            f.write(f"min: {npbpp.min()}\n")
            f.write(f"max: {npbpp.max()}\n")
            f.write("PSNR\n")
            f.write(f"mean: {nppsnr.mean()}\n")
            f.write(f"var: {nppsnr.var()}\n")
            f.write(f"min: {nppsnr.min()}\n")
            f.write(f"max: {nppsnr.max()}\n")