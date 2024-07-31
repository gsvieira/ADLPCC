clouds=(Queen)
lambdas=(100 1000 5000)
alphas=(9 75 5)
experiment=0
basedir=/home/gabriel/PCC_fernando

for cloud in "${clouds[@]}"; do
    for lambda in "${lambdas[@]}"; do
        for alpha in "${alphas[@]}"; do
            python ${basedir}/ADLPCC/src/ADLPCC.py compress "/home/valeska/MPEG_Down/Testing/${cloud}.ply" "${basedir}/Training/Experiment_${experiment}/${lambda}/0.${alpha}/"

            python ${basedir}/ADLPCC/src/ADLPCC.py decompress "${basedir}/ADLPCC/results/0.${alpha}/${cloud}/${cloud}.pkl.gz" "${basedir}/Training/Experiment_${experiment}/${lambda}/0.${alpha}/"

            python ${basedir}/scripts/psnr.py --input "/home/valeska/MPEG_Down/Testing/${cloud}.ply" --target "/home/gabriel/PCC_fernando/ADLPCC/results/0.${alpha}/${cloud}/${cloud}.pkl.gz.dec.ply" --result "${basedir}/ADLPCC/results/0.${alpha}/${cloud}/"

            mkdir -p ${basedir}/ADLPCC/results/${lambda}/0.${alpha}/${cloud}/
            mv ${basedir}/ADLPCC/results/0.${alpha}/${cloud}/* ${basedir}/ADLPCC/results/${lambda}/0.${alpha}/${cloud}/
        done
    done 
done

# python ADLPCC.py compress "/home/valeska/MPEG_Down/Testing/Longdress.ply" "../../Training/Experiment_0/100/0.5/"

# python psnr.py --input "/home/valeska/MPEG_Down/Testing/Longdress.ply"  --target "/home/gabriel/PCC_fernando/ADLPCC/results/0.5/Longdress/Longdress.pkl.gz.dec.ply" --result "/home/gabriel/PCC_fernando/ADLPCC/results/0.5/Longdress/"

# python ../../scripts/psnr.py --input "/home/valeska/MPEG_Down/Testing/Queen.ply" --target "/home/gabriel/PCC_fernando/ADLPCC/r_target_results/100/0.9/Queen/r_target1.5/Queen.pkl.gz.dec.ply" --result "../r_target_results/r_target1.5/Queen/"