#!/bin/bash
#PBS -l select=1:ncpus=8:ngpus=1  ###請完全照樣輸入，在課程帳號環境沒有其他選項
#PBS -q ee ###請完全照樣輸入，只允許使用ee

source activate b06502162
###cd $PBS_O_WORKDIR
module load cuda/cuda-10.0/x86_64
python main.py ###你要跑的code
source deactivate