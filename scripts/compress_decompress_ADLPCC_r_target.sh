clouds=(House Klimt Longdress Queen)
betas=(300)
alpha=9
experiment=15
basedir=/workspaces/ADLPCC
d_targets=(750)
experiment_steps=(100000 200000 300000)

for d_target in "${d_targets[@]}"; do
    for beta in "${betas[@]}"; do
        for cloud in "${clouds[@]}"; do 
            for experiment_step in "${experiment_steps[@]}"; do 
                # python ${basedir}/src/ADLPCC.py compress "${basedir}/MPEG_Down/Testing/${cloud}.ply" "/workspaces/ADLPCC/Training/Experiment_15/steps_${experiment_step}/${beta}/0.9/d_target${d_target}/" --beta "${beta}" --target_distortion "${d_target}"

                # python ${basedir}/src/ADLPCC.py decompress "${basedir}/results/d_target${d_target}/${cloud}/${cloud}.pkl.gz" "/workspaces/ADLPCC/Training/Experiment_15/steps_${experiment_step}/${beta}/0.9/d_target${d_target}/"

                # mkdir -p ${basedir}/results/steps_${experiment_step}/${beta}/0.${alpha}/${cloud}/d_target${d_target}/
                # mv ${basedir}/results/d_target${d_target}/${cloud}/* ${basedir}/results/steps_${experiment_step}/${beta}/0.${alpha}/${cloud}/d_target${d_target}/

                python ${basedir}/scripts/psnr.py --input "${basedir}/MPEG_Down/Testing/${cloud}.ply" --target "${basedir}/results/steps_${experiment_step}/${beta}/0.${alpha}/${cloud}/d_target${d_target}/${cloud}.pkl.gz.dec.ply" --result "${basedir}/results/steps_${experiment_step}/${beta}/0.${alpha}/${cloud}/d_target${d_target}/" 
            done
        done
    done
done
# python ADLPCC.py compress "/workspaces/ADLPCC/MPEG_Down/Training/Head.ply" "/workspaces/ADLPCC/Training_100k/Experiment_7/1500/0.9/d_target2000/"

# python psnr.py --input "/home/valeska/MPEG_Down/Testing/Longdress.ply"  --target "/home/gabriel/PCC_fernando/ADLPCC/results/0.5/Longdress/Longdress.pkl.gz.dec.ply" --result "/home/gabriel/PCC_fernando/ADLPCC/results/0.5/Longdress/"

# python ADLPCC.py compress "/home/valeska/MPEG_Down/Testing/House.ply" "/home/gabriel/PCC_fernando/500k/Experiment_5/3000/0.9/d_target0.5/"