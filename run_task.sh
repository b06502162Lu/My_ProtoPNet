#!/bin/bash
#PBS -l select=1:ncpus=8:ngpus=1  
#PBS -q ee
conda activate b06502162
cd $PBS_O_WORKDIR
module load cuda/cuda-10.0/x86_64
python main.py
conda deactivate
