import pickle
import numpy as np
from pathlib import Path
import os

root_dir = Path("/home/valeska/point_cloud_project/Trainable_blocks_64/Training/")
save_root_dir = Path("/home/gabriel/PCC_fernando/Training_blocks_64/")
folder_names = sorted(os.listdir(root_dir))

for folder_name in folder_names:
    folder_path = root_dir.joinpath(folder_name)
    npy_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.npy')]
    for npy_path in npy_files:
        npy = np.load(npy_path).astype(np.float32)
        save_dir = save_root_dir.joinpath(Path(npy_path).parent.name)
        if Path.exists(save_dir) == False:
            Path.mkdir(save_dir)
        with open(save_dir.joinpath(Path(npy_path).stem).with_suffix(".pkl"), 'wb') as f:
            pickle.dump(npy,f)
    print(f"{folder_name} ok!")
            
        
        
        

