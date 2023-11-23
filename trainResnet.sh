#!/bin/bash
source /root/anaconda3/bin/activate pytorch


CUDA_VISIBLE_DEVICES=1,2,0 python ResNetCRNN/UCF101_ResNetCRNN50.py --cnnPath cnn_encoder_epoch49.pth --rnnPath rnn_decoder_epoch49.pth
