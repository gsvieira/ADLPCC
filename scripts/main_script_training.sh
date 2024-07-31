#!/bin/bash
lambda=1000
alpha=0.9
device=0
experiment=3
screen -S "train_${alpha}_lambda${lambda}"

# screen -dm -S "train_0.9_lambda0.9" ./script_training_ADPLPCC_args.sh 0.9 1000 0 0