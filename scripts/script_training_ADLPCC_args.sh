#!/bin/bash
beta=$1
alpha=$2
device=$3
experiment=$4
basedir_train="/home/valeska/MPEG_Down/Training/*.ply"
source /home/gabriel/anaconda3/etc/profile.d/conda.sh
conda activate tf1.15
echo "Training_beta${beta}_alpha${alpha}"
CUDA_VISIBLE_DEVICES=${device} python ../ADLPCC/src/ADLPCC.py train ${basedir_train} "../Training/Experiment_${experiment}/${beta}/${alpha}/" --last_step 50000 --beta ${beta} --fl_alpha ${alpha}

# CUDA_VISIBLE_DEVICES=0 python ../ADLPCC/src/ADLPCC.py train "/home/valeska/MPEG_Down/Training/*.ply" "../Training/Experiment_0/5000/0.9/" --last_step 50000 --beta 5000 --fl_alpha 0.9