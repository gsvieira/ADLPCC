#!/bin/bash
size=32
lambdas=(100 1000 5000)
alpha=0.9
device=0
for lambda in "${lambdas[@]}"; do
    screen -dm -S "train_block_${size}_lambda${lambda}" ./script_training_args.sh ${size} ${lambda} ${alpha} ${device}
done

# screen -dm -S "train_alpha0.9_lambda5000"