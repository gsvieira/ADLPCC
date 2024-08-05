from pathlib import Path
import numpy as np

betas = [500, 3000]
Experiment = 5
basepath = f"/home/gabriel/PCC_fernando/results/ADLPCC/Experiment_{Experiment}/"

for lamb in betas:
    dirpath = Path(basepath).joinpath(f"beta_{lamb}")
    files = sorted(dirpath.glob("*.txt"))
    for file in files:
        bpv = []
        psnr = []
        with open(file) as f:
            lines = f.readlines()
            for line in lines: 
                if "bpv: " in line:
                    bpv.append(float(line[4:-1]))
                elif "psnr:" in line:
                    psnr.append((float(line[5:-1])))
        # print(bpv)
        npbpv = np.array(bpv)
        nppsnr = np.array(psnr)
        # print(npbpv.mean())
        # print(npbpv.var())
        with open(file, "a") as f:
            f.write("BPV\n")
            f.write(f"mean: {npbpv.mean()}\n")
            f.write(f"var: {npbpv.var()}\n")
            f.write(f"min: {npbpv.min()}\n")
            f.write(f"max: {npbpv.max()}\n")
            f.write("PSNR\n")
            f.write(f"mean: {nppsnr.mean()}\n")
            f.write(f"var: {nppsnr.var()}\n")
            f.write(f"min: {nppsnr.min()}\n")
            f.write(f"max: {nppsnr.max()}\n")