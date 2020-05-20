# %%

import IPython.display as display
import numpy as np
import os
import pathlib
import tensorflow as tf

from PIL import Image
from utils import show_batch

np.set_printoptions(precision=3,
                    suppress=True)

print(tf.__version__)

data_dir = tf.keras.utils.get_file(origin='https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz',
                                   fname='flower_photos', untar=True)
data_dir = pathlib.Path(data_dir)

print(data_dir)

class_names = [item.name for item in data_dir.glob('*') if item.name != "LICENSE.txt"]

print(class_names)

image_count = len(list(data_dir.glob('*/*.jpg')))

print(image_count)

daisies = list(data_dir.glob('daisy/*'))
display.display(Image.open(str(daisies[0])))

image_generator = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1.0/255)

batch_size = 32
img_height = 224
img_width = 224
steps_per_epoch = np.ceil(image_count / batch_size)

train_data_gen = image_generator.flow_from_directory(directory=str(data_dir),
                                                     batch_size=batch_size,
                                                     shuffle=True,
                                                     target_size=(img_height, img_width),
                                                     classes=list(class_names))

image_batch, label_batch = next(train_data_gen)

print(image_batch[0].shape)
print(len(label_batch[0]))
print(label_batch[0])

show_batch(image_batch, label_batch, class_names)