#!/bin/bash
lambda=$1
alpha=$2
device=$3
experiment=$4
basedir_train="/home/valeska/MPEG_Down/Training/*.ply"
source /home/gabriel/miniconda3/etc/profile.d/conda.sh
conda activate tf1.15
echo "Training_lambda${lambda}_alpha${alpha}"
CUDA_VISIBLE_DEVICES=${device} python ../ADLPCC/src/ADLPCC.py train ${basedir_train} "../Training/Experiment_${experiment}/${lambda}/${alpha}/" --last_step 50000 --lambda ${lambda} --fl_alpha ${alpha}

# CUDA_VISIBLE_DEVICES=0 python ../ADLPCC/src/ADLPCC.py train "/home/valeska/MPEG_Down/Training/*.ply" "../Training/Experiment_0/100/0.9/" --last_step 50000 --lambda 100 --fl_alpha 0.9