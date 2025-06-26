from pathlib import Path
import numpy as np
import plotly.express as px
import pandas as pd


betas = [300]
Experiment = 15
basepath = f"/workspaces/ADLPCC/results/Experiments/Experiment_{Experiment}"

results = []


def gain(target, min, max):
    try:
        return f"[-{(abs(target - min) / target):.2%}, {(abs(target - max) / target):.2%}]"
    except ZeroDivisionError:
        return 0


def process_values(df: pd.DataFrame, file: Path, beta: int, col_focal:str = "Final Focal Losses Hat", col_bpv: str = "Final Blocks bpv"):
    d_target = float(file.stem[file.stem.find("d_target")+len("d_target"):])

    for cloud, group in df.groupby("cloud"):
        focal = group[col_focal]
        focal_mean = focal.mean()
        focal_min = focal.min()
        focal_max = focal.max()

        variation = gain(d_target, focal_min, focal_max)

        focal_q5 = focal.quantile(0.05)
        focal_q95 = focal.quantile(0.95)
        mask_90 = (focal >=focal_q5) & (focal <= focal_q95)
        focal_90 = focal[mask_90]
        focal_mean_90 = focal_90.mean()
        variation_90 = gain(d_target, focal_90.min(), focal_90.max())

        bpv = group[col_bpv]
        bpv_90 = bpv[mask_90]

        psnr = group["psnr"].iloc[0]

        bpv_outliers = bpv[~mask_90]
        bpv_5 = bpv[focal < focal_q5]
        bpv_95 = bpv[focal > focal_q95]

        weigths = group["Final points per voxel"]

        bpv_mean = np.average(bpv, weights=weigths)
        bpv_5_mean = np.average(bpv_5, weights=weigths[focal < focal_q5])
        bpv_95_mean = np.average(bpv_95, weights=weigths[focal > focal_q95])
        bpv_outliers_mean = np.average(bpv_outliers, weights=weigths[~mask_90])
        bpv_without_outliers_mean = np.average(bpv_90, weights=weigths[mask_90])

        results.append({
            "cloud": cloud,
            "beta": beta,
            "psnr": psnr,
            "d_target": int(d_target),
            "mean_focal_loss": focal_mean,
            "variation": variation,
            "mean_focal_5_95": focal_mean_90,
            "variation_5_95": variation_90,
            "bpv_5": bpv_5_mean,
            "bpv_95": bpv_95_mean,
            "bpv_outliers": bpv_outliers_mean,
            "bpv_without_outliers": bpv_without_outliers_mean,
            "bpv": bpv_mean,
        })



for lamb in betas:
    step = 300000
    dirpath = Path(basepath).joinpath(f"steps_{step}/beta_{lamb}")
    files = sorted(dirpath.glob("*.txt"))
    d_targets = []

    
    dirpath = Path(dirpath).joinpath("results_processed")
        
    if(dirpath.is_dir() == False): #test if needed
        dirpath.mkdir(parents=True, exist_ok=True)


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

        target = file.stem[file.stem.find("d_target")+len("d_target"):]

        flat_data = []
        for i, cloud_name in enumerate(cloudNames):
            max_len = max(len(stat_list[i].split(', ')) for stat_list in split_lines)
            for j in range(max_len):
                linha = {'cloud': cloud_name}
                for stat_name, stat_list in zip(statistics_names, split_lines):
                    value = [float(v.strip()) for v in stat_list[i].split(', ')]
                    if len(value) == 1:
                        linha[stat_name] = value[0]
                    else:
                        linha[stat_name] = value[j] if j < len(value) else None
                flat_data.append(linha)
        df = pd.DataFrame(flat_data)

        for cloud, group in df.groupby("cloud"):
            for col in group.columns[1:]:
                if 'bpv' not in col:
                    final_string += f"\n{col} {cloud}\n"
                    final_string += f"mean: {group[col].mean()}\n"
                    final_string += f"var: {group[col].var()}\n"
                    final_string += f"min: {group[col].min()}\n"
                    final_string += f"max: {group[col].max()}\n"
                elif 'Final' not in col:
                    final_string+=f"{col} {cloud}: {float(group[col].iloc[0]):.4f}\n"


        process_values(df, file, lamb)

        fig = px.box(df, "cloud", "Final Blocks bpv", points=False, color='cloud')
        fig.update_yaxes(type='log')
        fig.update_layout(
            yaxis_title="Cloud",
            xaxis_title="BPV per Blocks",
            title=f"BPV per Blocks_beta_{lamb}_target_{target}_step{step}"
        )
        fig.write_image(f"{basepath}/steps_{step}/beta_{lamb}/results_processed/bpv_target_{target}_num_bpv.png")
        fig.show()

        fig = px.box(df, "cloud", "Final Focal Losses Hat", points='outliers', color='cloud')
        fig.update_layout(
            xaxis_title="Focal Loss",
            yaxis_title="Cloud",
            title=f"Focal Loss_beta_{lamb}_target_{target}_step{step}"
        )
        fig.update_yaxes(type='log')
        fig.add_hline(target, line_dash="dot", label=dict(text="d_target",
                                                        textposition="end",
                                                        font=dict(size=20, color="black"),
                                                        yanchor="top"),
                                                        )

        fig.write_image(f"{basepath}/steps_{step}/beta_{lamb}/results_processed/focal_target_{target}_num_bpv.png")
        fig.show()

        df1 = df.groupby('cloud', as_index=False).mean()
        fig = px.bar(df1, "cloud", "psnr", color='cloud')
        fig.update_layout(
            xaxis_title="Cloud",
            yaxis_title="PSNR-D1",
            title=f"PSNR_beta_{lamb}_target_{target}_step{step}"
        )
        fig.write_image(f"{basepath}/steps_{step}/beta_{lamb}/results_processed/psnr_target_{target}_num_bpv.png")
        fig.show()

        for i in range(len(cloudNames)):

            df1 = df[df['cloud'] == 'Longdress']
            q5 = df1['Final Focal Losses Hat'].quantile(0.05)
            q95 = df1['Final Focal Losses Hat'].quantile(0.95)
            df1['tipo'] = df1["Final Focal Losses Hat"].apply(
                lambda val: 'outlier' if val < q5 or val > q95 else 'normal'
            )
            fig = px.scatter(df1,'Final points per voxel', 'Final Blocks bpv', color='tipo')
            fig.update_layout(
                # xaxis_title="number of voxels",
                yaxis_title="BPV",
                title=f"Scatter Graph {cloudNames[i]}_{lamb}_target_{target}"
            )
            fig.write_image(f"{basepath}/steps_{step}/beta_{lamb}/{cloudNames[i]}_target_{target}_num_bpv.png")
            # fig.show()

            fig1 = px.scatter(df1,'Final points per voxel', 'Final Focal Losses Hat', color='tipo')
            fig1.update_layout(
                # xaxis_title="number of voxels",
                # yaxis_title="Focal Loss",
                title=f"Scatter Graph {cloudNames[i]}_{lamb}_target_{target}"
            )
            fig1.write_image(f"{basepath}/steps_{step}/beta_{lamb}/{cloudNames[i]}_target_{target}_num_loss.png")
            # fig1.show()
        final_file = dirpath.joinpath(file.name)

        with open(final_file, "w") as f:
            f.write(final_string)
results_df = pd.DataFrame(results)
results_df.sort_values(by=["d_target","beta"], ascending=[True, True], inplace=True)
results_df.to_csv(Path(basepath).joinpath(f"statistics_step{step}.csv"), index=False, float_format="%.2f")