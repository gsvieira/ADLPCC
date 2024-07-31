#!/bin/bash
lambda=$1
alpha=0.9
device=$2
experiment=$3
basedir_train="/home/valeska/MPEG_Down/Training/*.ply"
basedir="/home/gabriel/PCC_fernando/"
r_target=$4
source /home/gabriel/.bashrc
conda activate tf1.15
echo "Training_lambda${lambda}_alpha${alpha}"
CUDA_VISIBLE_DEVICES=${device} python ${basedir}/ADLPCC/src/ADLPCC.py train ${basedir_train} "${basedir}/Training/Experiment_${experiment}/${lambda}/${alpha}/" --last_step 50000 --lambda ${lambda} --fl_alpha ${alpha} --target_rate ${r_target}

# CUDA_VISIBLE_DEVICES=0 python ../ADLPCC/src/ADLPCC.py train "/home/valeska/MPEG_Down/Training/*.ply" "../Training_150k/Experiment_4/500/0.9/r_target0.5/" --last_step 150000 --lambda 500 --fl_alpha 0.9 --target_rate 0.5

# CUDA_VISIBLE_DEVICES=0 python ../ADLPCC/src/ADLPCC.py train "/home/valeska/MPEG_Down/Training/*.ply" "../Training_50k/Experiment_4/2500/0.9/r_target0.25/" --last_step 50000 --lambda 2500 --fl_alpha 0.9 --target_rate 0.25