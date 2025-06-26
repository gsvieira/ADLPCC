clouds=(House Klimt Longdress Queen)
betas=(300)
alphas=(9)
experiment=15
basedir=/workspaces/ADLPCC
steps=(100000 200000 300000)

for alpha in "${alphas[@]}"; do 
    for beta in "${betas[@]}"; do
        for step in "${steps[@]}"; do
            mkdir -p ${basedir}/results/Experiments/Experiment_${experiment}/steps_${step}/beta_${beta}
            for cloud in "${clouds[@]}"; do
                for filename in ${basedir}/results/steps_${step}/${beta}/0.${alpha}/${cloud}/*; do
                    dirname=$(basename $filename)
                    echo ${cloud} >> ${basedir}/results/Experiments/Experiment_${experiment}/steps_${step}/beta_${beta}/results_alpha0.${alpha}_${dirname}.txt
                    cat ${basedir}/results/steps_${step}/${beta}/0.${alpha}/${cloud}/${dirname}/${cloud}_statistics.txt >> ${basedir}/results/Experiments/Experiment_${experiment}/steps_${step}/beta_${beta}/results_alpha0.${alpha}_${dirname}.txt
                done
            done
        done
    done
done