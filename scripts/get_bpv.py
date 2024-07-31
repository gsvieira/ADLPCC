import os
import glob
import open3d as o3d
from pathlib import Path
import numpy as np
import pandas as pd
from numpy import load

def get_bpv(path_blocks):
    path_csv = os.path.join(path_blocks, '_results.csv')
    df = pd.read_csv(path_csv)
    df = df.iloc[:-1]
    sum_bits = 0
    qnt_voxels = 0
    for index, row in df.iterrows():
        block_name = row.values[1].split('/')[-1]
        voxels = load(os.path.join(path_blocks, block_name))
        voxels = voxels.astype(int)
        qnt_voxels += np.sum(voxels)
        sum_bits += np.double(row.values[-1])
    return (sum_bits/qnt_voxels)


if __name__ == "__main__":
    basedir = '/home/gabriel/PCC_fernando/ADLPCC/results/0.5/'
    lmbdas = 0.5
    clouds = 'Longdress'
    for l in lmbdas:
        with open(os.path.join(basedir,'Results','BPV_'+str(s)+'_lambda'+str(l)+'_alpha'+str(b)+'.txt'), 'w') as f:
            for cloud in clouds:
                path_blocks= path_decoded_blocks = f"{basedir}/Outputs/Focal_Hyperprior_Training_block_{s}_1mi200k_lambda{l}_alpha{b:.1f}/{cloud}"
                bpv = get_bpv(path_blocks)
                f.write("Cloud %s: %f\n"%(cloud, bpv))