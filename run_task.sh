#!/bin/bash
#PBS -l select=1:ncpus=8:ngpus=1  
#PBS -q ee
source activate env-name /home/eegroup/eefrank/anaconda3/envs/b06502162
cd $PBS_O_WORKDIR
module load cuda/cuda-10.0/x86_64
python /home/eegroup/eefrank/b06502162/My_ProtoPNet/main.py
source deactivate
