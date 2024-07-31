clouds=(House Klimt Longdress Queen)
lambdas=(500 1000 2000 3000)
alphas=(9)
experiment=4
basedir=/home/gabriel/PCC_fernando
r_targets=(0)

for r_target in "${r_targets[@]}"; do
    for lambda in "${lambdas[@]}"; do
        for cloud in "${clouds[@]}"; do 
            for alpha in "${alphas[@]}"; do 
                python ${basedir}/ADLPCC/src/ADLPCC.py compress "/home/valeska/MPEG_Down/Testing/${cloud}.ply" "${basedir}/Training_150k/Experiment_${experiment}/${lambda}/0.${alpha}/r_target2.${r_target}/"

                python ${basedir}/ADLPCC/src/ADLPCC.py decompress "${basedir}/ADLPCC/results/r_target2.${r_target}/${cloud}/${cloud}.pkl.gz" "${basedir}/Training_150k/Experiment_${experiment}/${lambda}/0.${alpha}/r_target2.${r_target}/"

                python ${basedir}/scripts/psnr.py --input "/home/valeska/MPEG_Down/Testing/${cloud}.ply" --target "/home/gabriel/PCC_fernando/ADLPCC/results/r_target2.${r_target}/${cloud}/${cloud}.pkl.gz.dec.ply" --result "${basedir}/ADLPCC/results/r_target2.${r_target}/${cloud}/"

                mkdir -p ${basedir}/ADLPCC/results/${lambda}/0.${alpha}/${cloud}/r_target2.${r_target}/
                mv ${basedir}/ADLPCC/results/r_target2.${r_target}/${cloud}/* ${basedir}/ADLPCC/results/${lambda}/0.${alpha}/${cloud}/r_target2.${r_target}/
            done
        done
    done
done
# python ADLPCC.py compress "/home/valeska/MPEG_Down/Testing/Longdress.ply" "../../Training/Experiment_2/5000/0.5/r_target0.5"

# python psnr.py --input "/home/valeska/MPEG_Down/Testing/Longdress.ply"  --target "/home/gabriel/PCC_fernando/ADLPCC/results/0.5/Longdress/Longdress.pkl.gz.dec.ply" --result "/home/gabriel/PCC_fernando/ADLPCC/results/0.5/Longdress/"

python ADLPCC.py compress "/home/valeska/MPEG_Down/Testing/House.ply" "/home/gabriel/PCC_fernando/Training_250k/Experiment_3/1000/0.9/r_target2.0/"