clouds=(House Klimt Longdress Queen)
betas=(500 3000)
alphas=(9)
experiment=5
basedir=/home/gabriel/PCC_fernando
r_targets=(5)

for r_target in "${r_targets[@]}"; do
    for beta in "${betas[@]}"; do
        for cloud in "${clouds[@]}"; do 
            for alpha in "${alphas[@]}"; do 
                python ${basedir}/ADLPCC/src/ADLPCC.py compress "/home/valeska/MPEG_Down/Testing/${cloud}.ply" "${basedir}/Training_500k/Experiment_${experiment}/${beta}/0.${alpha}/r_target0.${r_target}/"

                python ${basedir}/ADLPCC/src/ADLPCC.py decompress "${basedir}/ADLPCC/results/r_target0.${r_target}/${cloud}/${cloud}.pkl.gz" "${basedir}/Training_500k/Experiment_${experiment}/${beta}/0.${alpha}/r_target0.${r_target}/"

                python ${basedir}/ADLPCC/scripts/psnr.py --input "/home/valeska/MPEG_Down/Testing/${cloud}.ply" --target "/home/gabriel/PCC_fernando/ADLPCC/results/r_target0.${r_target}/${cloud}/${cloud}.pkl.gz.dec.ply" --result "${basedir}/ADLPCC/results/r_target0.${r_target}/${cloud}/"

                mkdir -p ${basedir}/ADLPCC/results/${beta}/0.${alpha}/${cloud}/r_target0.${r_target}/
                mv ${basedir}/ADLPCC/results/r_target0.${r_target}/${cloud}/* ${basedir}/ADLPCC/results/${beta}/0.${alpha}/${cloud}/r_target0.${r_target}/
            done
        done
    done
done
# python ADLPCC.py compress "/home/valeska/MPEG_Down/Testing/Longdress.ply" "../../Training_500k/Experiment_5/3000/0.9/r_target0.5"

# python psnr.py --input "/home/valeska/MPEG_Down/Testing/Longdress.ply"  --target "/home/gabriel/PCC_fernando/ADLPCC/results/0.5/Longdress/Longdress.pkl.gz.dec.ply" --result "/home/gabriel/PCC_fernando/ADLPCC/results/0.5/Longdress/"

# python ADLPCC.py compress "/home/valeska/MPEG_Down/Testing/House.ply" "/home/gabriel/PCC_fernando/Training_500k/Experiment_5/3000/0.9/r_target0.5/"