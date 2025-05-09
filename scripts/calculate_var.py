from pathlib import Path
import numpy as np

betas = [500]
Experiment = 7
basepath = f"/workspaces/ADLPCC/results/0.9/Longdress"


def process_single_value(arr, name, cloud_names):
    np_arr = np.array(arr, float)
    np_list = np_arr.tolist()
    string = ""
    for i in range(len(cloud_names)):
        string += f"{cloudNames[i]} {name}: {np_list[i]}\n"
    
    string += f"\n{name}\n"
    string += f"mean: {np_arr.mean()}\n"
    string += f"var: {np_arr.var()}\n"
    string += f"min: {np_arr.min()}\n"
    string += f"max: {np_arr.max()}\n"

    return string




def process_multiple_value(arr, name, cloud_names):
    string = ""
    for i in range(len(arr)):
        np_arr = np.fromstring(arr[i], sep=', ')
        
        string += f"\n{name} {cloud_names[i]}\n"
        string += f"mean: {np_arr.mean()}\n"
        string += f"var: {np_arr.var()}\n"
        string += f"min: {np_arr.min()}\n"
        string += f"max: {np_arr.max()}\n"

    return string

for lamb in betas:
    dirpath = Path(basepath)#.joinpath(f"beta_{lamb}")
    files = sorted(dirpath.glob("*.txt"))

    
    final_file = Path(basepath).parent
    final_file = final_file.joinpath("results_processed", f"beta_{lamb}")
        
    if(final_file.is_dir() == False): #test if needed
        final_file.mkdir(parents=True, exist_ok=True)


    for file in files:
        split_lines = []
        cloudNames = []
        statistics_names = []
        final_string = ""
        with open(file) as f:
            lines = f.readlines()
            for line in lines: 
                if line.find(':') == -1:
                    cloudNames.append(line[:-1])
                else:
                    line_splitted = line.split(': ')
                    name = line_splitted[0]
                    if name in statistics_names:
                       index = statistics_names.index(name)
                       split_lines[index].append(line_splitted[1][:-1])

                    else:
                        statistics_names.append(name)
                        split_lines.append([line_splitted[1][:-1]])

            for i in range(len(split_lines)):
                if split_lines[i][0].find(',') == -1:
                    final_string += process_single_value(split_lines[i], statistics_names[i], cloudNames)
                else:
                    final_string += process_multiple_value(split_lines[i], statistics_names[i], cloudNames)

        # final_file = Path("/workspaces/ADLPCC/")
        final_file = final_file.joinpath(file.name)

        with open(final_file, "w") as f:
            f.write(final_string)
