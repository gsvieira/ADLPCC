#!/bin/bash
beta=500
alpha=0.9
device=0
experiment=15
basedir_train=/workspaces/ADLPCC/MPEG_Down/Training/*.ply
basedir="/workspaces/ADLPCC"
# d_target=250
# steps=50000
# source /home/gabriel/.bashrc
# conda activate tf1.15
echo "Training_beta${beta}_alpha${alpha}"
for steps in 100000 200000 300000;
do for d_target in 750;
    do
        CUDA_VISIBLE_DEVICES=${device} python ${basedir}/src/ADLPCC.py train "${basedir_train}" "/workspaces/ADLPCC/Training/Experiment_${experiment}/${beta}/0.9/d_target${d_target}/" --last_step ${steps} --beta ${beta} --fl_alpha ${alpha} --target_distortion ${d_target};
        mkdir -p /workspaces/ADLPCC/Training/Experiment_${experiment}/steps_${steps}/${beta}/0.9/d_target${d_target}/
        cp -r /workspaces/ADLPCC/Training/Experiment_${experiment}/${beta}/0.9/d_target${d_target}/* /workspaces/ADLPCC/Training/Experiment_${experiment}/steps_${steps}/${beta}/0.9/d_target${d_target}/;
        linha="model_checkpoint_path: \"/workspaces/ADLPCC/Training/Experiment_${experiment}/steps_${steps}/${beta}/0.9/d_target${d_target}/model.ckpt-${steps}\""
        sed -i "1s|.*|$linha|" /workspaces/ADLPCC/Training/Experiment_${experiment}/steps_${steps}/${beta}/0.9/d_target${d_target}/checkpoint
    done
done
# CUDA_VISIBLE_DEVICES=0 python ../ADLPCC/src/ADLPCC.py train "/home/valeska/MPEG_Down/Training/*.ply" "../Training_150k/Experiment_4/500/0.9/d_target0.5/" --last_step 150000 --beta 500 --fl_alpha 0.9 --target_distortion 0.5

# CUDA_VISIBLE_DEVICES=0 python ../src/ADLPCC.py train "/home/valeska/MPEG_Down/Training/*.ply" "../Training_1000k/Experiment_4/3000/0.9/r_target0.5/" --last_step 1000000 --beta 3000 --fl_alpha 0.9 --target_distortion 0.5

# CUDA_VISIBLE_DEVICES=0 python ADLPCC.py train "/workspaces/ADLPCC/MPEG_Down/blocks/Longdress" "/workspaces/ADLPCC/Training/Experiment_10/64_blocks/3000/0.9/d_target50/" --last_step 50000 --beta 3000 --fl_alpha 0.9 --target_distortion 50

# CUDA_VISIBLE_DEVICES=0 python /workspaces/ADLPCC/src/ADLPCC.py train "${basedir_train}" "/workspaces/ADLPCC/Training/Experiment_${experiment}/64blocks_less2000/${beta}/0.9/d_target${d_target}/" --last_step ${steps} --beta ${beta} --fl_alpha ${alpha} --target_distortion ${d_target};