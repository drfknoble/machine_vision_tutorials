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

list_ds = tf.data.Dataset.list_files(str(data_dir/'*/*'))

batch_size = 32
img_height = 224
img_width = 224
steps_per_epoch = np.ceil(image_count / batch_size)

def get_label(file_path):

    parts = tf.strings.split(file_path, os.path.sep)

    return parts[-2] == class_names


def decode_img(img):

    img = tf.image.decode_jpeg(img, channels=3)

    img = tf.image.convert_image_dtype(img, tf.float32)

    return tf.image.resize(img, [img_width, img_height])


def process_path(file_path):

    label = get_label(file_path)

    img = tf.io.read_file(file_path)

    img = decode_img(img)

    return img, label

labeled_ds = list_ds.map(process_path, num_parallel_calls=1)

for image, label in labeled_ds.take(1):
    print("Image shape: {}".format(image.numpy().shape))
    print("Label: {}".format(label.numpy()))

def prepare_for_training(ds, cache=True, shuffle_buffer_size=1000):
    if cache:
        if isinstance(cache, str):
            ds = ds.cache(cache)
        else:
            ds = ds.cache()

    ds = ds.shuffle(buffer_size=shuffle_buffer_size)

    ds = ds.repeat()

    ds = ds.batch(batch_size)

    ds = ds.prefetch(buffer_size = 1)

    return ds

train_ds = prepare_for_training(labeled_ds)

image_batch, label_batch = next(iter(train_ds))

show_batch(image_batch.numpy(), label_batch.numpy(), class_names)