from pathlib import Path
import numpy as np

betas = [3000]
Experiment = 7
basepath = f"/workspaces/ADLPCC/Experiments/Experiment_7/training_PC/pre_processed"

for lamb in betas:
    dirpath = Path(basepath).joinpath(f"beta_{lamb}")
    files = sorted(dirpath.glob("*.txt"))
    for file in files:
        bpv = []
        psnr = []
        focal = []
        cloudNames = []
        with open(file) as f:
            lines = f.readlines()
            for line in lines: 
                if "bpv: " in line:
                    bpv.append(float(line[4:-1]))
                elif "psnr:" in line:
                    psnr.append((float(line[5:-1])))
                elif "Final Focal Losses:" in line:
                    focal.append(line[20:-1])
                elif line:
                    cloudNames.append(line[:-1])
        # print(bpv)
        npbpv = np.array(bpv)
        nppsnr = np.array(psnr)
        npfocal = np.fromstring(focal[0], sep=', ')
        # print(npbpv.mean())
        # print(npbpv.var())
        final_file = Path(basepath).parent
        final_file = final_file.joinpath("results_processed", f"beta_{lamb}")
        
        if(final_file.is_dir() == False):
            final_file.mkdir(parents=True, exist_ok=True)
        final_file = final_file.joinpath(file.name)

        bpvlist = npbpv.tolist()
        psnrlist = nppsnr.tolist()
        with open(final_file, "w") as f:
            for i in range(len(cloudNames)):
                f.write(f"{cloudNames[i]}\n")
                f.write(f"BPV: {bpvlist[i]}\n")
                f.write(F"PSNR: {psnrlist[i]}\n")
            
            f.write("\nBPV\n")
            f.write(f"mean: {npbpv.mean()}\n")
            f.write(f"var: {npbpv.var()}\n")
            f.write(f"min: {npbpv.min()}\n")
            f.write(f"max: {npbpv.max()}\n")
            f.write("\nPSNR\n")
            f.write(f"mean: {nppsnr.mean()}\n")
            f.write(f"var: {nppsnr.var()}\n")
            f.write(f"min: {nppsnr.min()}\n")
            f.write(f"max: {nppsnr.max()}\n")
            i = 0
            for fline in focal:
                npfocal = np.fromstring(fline, sep=', ')
                f.write(f"\nFocal {cloudNames[i]}\n")
                f.write(f"mean: {npfocal.mean()}\n")
                f.write(f"var: {npfocal.var()}\n")
                f.write(f"min: {npfocal.min()}\n")
                f.write(f"max: {npfocal.max()}\n")
                i = i+1
