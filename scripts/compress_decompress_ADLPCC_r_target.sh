clouds=(House Klimt Longdress Queen)
betas=(500)
alphas=(9)
experiment=7
basedir=/home/gabriel/PCC_fernando
d_targets=(1000)
experiment_steps=50k

for d_target in "${d_targets[@]}"; do
    for beta in "${betas[@]}"; do
        for cloud in "${clouds[@]}"; do 
            for alpha in "${alphas[@]}"; do 
                python ${basedir}/ADLPCC/src/ADLPCC.py compress "/home/valeska/MPEG_Down/Testing/${cloud}.ply" "${basedir}/Experiment_${experiment}/${experiment_steps}/${beta}/0.${alpha}/d_target${d_target}/"

                python ${basedir}/ADLPCC/src/ADLPCC.py decompress "${basedir}/ADLPCC/results/d_target${d_target}/${cloud}/${cloud}.pkl.gz" "${basedir}/Experiment_${experiment}/${experiment_steps}/${beta}/0.${alpha}/d_target${d_target}/"

                python ${basedir}/ADLPCC/scripts/psnr.py --input "/home/valeska/MPEG_Down/Testing/${cloud}.ply" --target "/home/gabriel/PCC_fernando/ADLPCC/results/d_target${d_target}/${cloud}/${cloud}.pkl.gz.dec.ply" --result "${basedir}/ADLPCC/results/d_target${d_target}/${cloud}/"

                mkdir -p ${basedir}/ADLPCC/results/${beta}/0.${alpha}/${cloud}/d_target${d_target}/
                mv ${basedir}/ADLPCC/results/d_target${d_target}/${cloud}/* ${basedir}/ADLPCC/results/${beta}/0.${alpha}/${cloud}/d_target${d_target}/
            done
        done
    done
done
# python ADLPCC.py compress "/home/valeska/MPEG_Down/Testing/Longdress.ply" "../../500k/Experiment_5/3000/0.9/d_target0.5"

# python psnr.py --input "/home/valeska/MPEG_Down/Testing/Longdress.ply"  --target "/home/gabriel/PCC_fernando/ADLPCC/results/0.5/Longdress/Longdress.pkl.gz.dec.ply" --result "/home/gabriel/PCC_fernando/ADLPCC/results/0.5/Longdress/"

# python ADLPCC.py compress "/home/valeska/MPEG_Down/Testing/House.ply" "/home/gabriel/PCC_fernando/500k/Experiment_5/3000/0.9/d_target0.5/"