clouds=(Klimt Longdress House Queen)
lambdas=(500 1000 2000 3000)
alphas=(9)
experiment=4
basedir=/home/gabriel/PCC_fernando

for alpha in "${alphas[@]}"; do 
    for lambda in "${lambdas[@]}"; do
        mkdir -p ${basedir}/results/ADLPCC/Experiment_${experiment}/lambda_${lambda}/
        for cloud in "${clouds[@]}"; do
            for filename in ${basedir}/ADLPCC/results/${lambda}/0.${alpha}/${cloud}/*; do
                dirname=$(basename $filename)
                echo ${cloud} >> ${basedir}/results/ADLPCC/Experiment_${experiment}/lambda_${lambda}/results_alpha0.${alpha}_${dirname}.txt
                cat ${basedir}/ADLPCC/results/${lambda}/0.${alpha}/${cloud}/${dirname}/${cloud}_statistics.txt >> ${basedir}/results/ADLPCC/Experiment_${experiment}/lambda_${lambda}/results_alpha0.${alpha}_${dirname}.txt
            done
        done
    done
done