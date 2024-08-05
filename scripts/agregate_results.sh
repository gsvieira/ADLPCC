clouds=(Klimt Longdress House Queen)
betas=(500 3000)
alphas=(9)
experiment=5
basedir=/home/gabriel/PCC_fernando

for alpha in "${alphas[@]}"; do 
    for beta in "${betas[@]}"; do
        mkdir -p ${basedir}/results/ADLPCC/Experiment_${experiment}/beta_${beta}/
        for cloud in "${clouds[@]}"; do
            for filename in ${basedir}/ADLPCC/results/${beta}/0.${alpha}/${cloud}/*; do
                dirname=$(basename $filename)
                echo ${cloud} >> ${basedir}/results/ADLPCC/Experiment_${experiment}/beta_${beta}/results_alpha0.${alpha}_${dirname}.txt
                cat ${basedir}/ADLPCC/results/${beta}/0.${alpha}/${cloud}/${dirname}/${cloud}_statistics.txt >> ${basedir}/results/ADLPCC/Experiment_${experiment}/beta_${beta}/results_alpha0.${alpha}_${dirname}.txt
            done
        done
    done
done