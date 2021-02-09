import matplotlib.pyplot as plt
import numpy as np
import os
import tensorflow as tf


def make_cluster(pos=None, num=None, r=None):

    if pos is None:
        return

    if num is None:
        return

    if r is None:
        return

    theta = np.random.uniform(0, 2 * np.pi, [num, 1])
    dr = np.random.uniform(0, r, [num, 1])

    dx = dr * np.cos(theta)
    dy = dr * np.sin(theta)
    x = pos[0] + dx
    y = pos[0] + dy

    X = np.hstack([x, y])
    print(np.shape(X))

    return X


def show_batch(image_batch, label_batch, class_names):

    plt.figure(figsize=(10, 10))
    for i in range(9):
        plt.subplot(3, 3, i+1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(image_batch[i])
        plt.title(class_names[np.argmax(label_batch[i])])
