#!/bin/bash
lambda=100
alpha=0.9
device=0
experiment=0
basedir_train="/home/gabriel/PCC_fernando/Training_blocks_64"
basedir_test="/home/gabriel/PCC_fernando/Testing_blocks_64"
save_model=/home/gabriel/PCC_fernando/Training_IT-DL-PCC
source /home/gabriel/anaconda3/etc/profile.d/conda.sh
conda activate IT-DL
echo "Training_lambda${lambda}_alpha${alpha}"
CUDA_VISIBLE_DEVICES=${device} python ../IT-DL-PCC/src/train.py -v -d ${basedir_train} --val_data ${basedir_test} --model_dir "${save_model}/Experiment_${experiment}/${alpha}" --fl_alpha ${alpha} --batch-size 32  --epochs 250 --cuda --save

#CUDA_VISIBLE_DEVICES=0 python /home/gabriel/PCC_fernando/IT-DL-PCC/src/train.py -v -d "/home/gabriel/PCC_fernando/Training_blocks_64" --val_data "/home/gabriel/PCC_fernando/Testing_blocks_64" --model_dir "/home/gabriel/PCC_fernando/Training_IT-DL-PCC/Experiment_0/0.9" --fl_alpha 0.9 --batch-size 32  --epochs 250 --cuda --save