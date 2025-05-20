import numpy as np
from sklearn.linear_model import LinearRegression
from pathlib import Path

betas = [500,1000,1500,2000,2500,3000]
Experiment = 10
d_targets = [250,500,1000]
alpha = 0.9
blocks_bpv = 0
blocks_bpv_hat = 0

basepath = f"/workspaces/ADLPCC/results/Experiments/Experiment_{Experiment}"
result_str = ""
for beta in betas:
    for d_target in d_targets:
        file = Path(basepath).joinpath(f"beta_{beta}", f"results_alpha{alpha}_d_target{d_target}.txt")
        if file.is_file == 0:
            continue
        with open(file) as f:
            lines = f.readlines()
        for line in lines:
            if "Final Blocks bpv" in line:
                blocks_bpv = line[line.find(":")+1:]
            elif "Final BPVs Hat" in line:
                blocks_bpv_hat = line[line.find(":")+1:]
            elif ":" not in line:
                cloudname = line
        x = np.fromstring(blocks_bpv_hat,  float, sep=", ")
        x = x.reshape((-1, 1))
        y = np.fromstring(blocks_bpv, float, sep=", ")
        model = LinearRegression().fit(x, y)
        if len(result_str) != 0:
            result_str+="\n"
        result_str+=f"LR_alpha{alpha}_beta{beta}_d_target{d_target}"
        result_str+=f"\n{cloudname}"
        result_str+=f"Score: {model.score(x, y)}\n"
        result_str+=f"Slope: {model.coef_}\n"
        result_str+=f"Constant: {model.intercept_}"

outfile = Path(basepath).joinpath(f"LR_results.txt")
with open(outfile, "w") as f:
    f.write(result_str)

