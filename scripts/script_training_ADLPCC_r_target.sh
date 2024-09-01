#!/bin/bash
beta=$1
alpha=0.9
device=$2
experiment=$3
basedir_train="/home/valeska/MPEG_Down/Training/*.ply"
basedir="/home/gabriel/PCC_fernando/"
d_target=$4
source /home/gabriel/.bashrc
conda activate tf1.15
echo "Training_beta${beta}_alpha${alpha}"
CUDA_VISIBLE_DEVICES=${device} python ${basedir}/ADLPCC/src/ADLPCC.py train ${basedir_train} "${basedir}/Training/Experiment_${experiment}/${beta}/${alpha}/" --last_step 50000 --beta ${beta} --fl_alpha ${alpha} --target_distortion ${d_target}

# CUDA_VISIBLE_DEVICES=0 python ../ADLPCC/src/ADLPCC.py train "/home/valeska/MPEG_Down/Training/*.ply" "../Training_150k/Experiment_4/500/0.9/d_target0.5/" --last_step 150000 --beta 500 --fl_alpha 0.9 --target_distortion 0.5

# CUDA_VISIBLE_DEVICES=0 python ../src/ADLPCC.py train "/home/valeska/MPEG_Down/Training/*.ply" "../Training_1000k/Experiment_4/3000/0.9/r_target0.5/" --last_step 1000000 --beta 3000 --fl_alpha 0.9 --target_distortion 0.5