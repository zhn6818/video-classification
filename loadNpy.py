import numpy as np
import matplotlib.pyplot as plt

A = np.load('./ResNetCRNN/CRNN_epoch_training_losses50.npy')
B = np.load('./ResNetCRNN/CRNN_epoch_training_scores50.npy')
C = np.load('./ResNetCRNN/CRNN_epoch_test_loss50.npy')
D = np.load('./ResNetCRNN/CRNN_epoch_test_score50.npy')

epochs = 50

# plot
fig = plt.figure(figsize=(10, 4))
plt.subplot(121)
plt.plot(np.arange(1, epochs + 1), A[:, -1])  # train loss (on epoch end)
plt.plot(np.arange(1, epochs + 1), C)         #  test loss (on epoch end)
plt.title("model loss")
plt.xlabel('epochs')
plt.ylabel('loss')
plt.legend(['train', 'test'], loc="upper left")
# 2nd figure
plt.subplot(122)
plt.plot(np.arange(1, epochs + 1), B[:, -1])  # train accuracy (on epoch end)
plt.plot(np.arange(1, epochs + 1), D)         #  test accuracy (on epoch end)
plt.title("training scores")
plt.xlabel('epochs')
plt.ylabel('accuracy')
plt.legend(['train', 'test'], loc="upper left")
title = "./ResNetCRNN/fig_UCF101_CRNN50.png"
plt.savefig(title, dpi=600)
# plt.close(fig)
plt.show()

# print('data:', data)
# print('test: ', test[:, -1])