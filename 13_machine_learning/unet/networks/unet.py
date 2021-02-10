import tensorflow as tf


def network(img_height=224, img_width=224, channels=3):

    # data_format = 'channels_last'

    # tf.keras.backend.set_image_data_format(data_format)

    inputs = tf.keras.layers.Input([img_height, img_width, 3])

    conv1 = tf.keras.layers.Conv2D(64, 3, activation = 'relu', padding = 'same', kernel_initializer = 'he_normal')(inputs)
    conv1 = tf.keras.layers.Conv2D(64, 3, activation = 'relu', padding = 'same', kernel_initializer = 'he_normal')(conv1)
    conv1 = tf.keras.layers.BatchNormalization(axis=1, trainable=True)(conv1)
    pool1 = tf.keras.layers.MaxPooling2D(pool_size=(2, 2))(conv1)

    conv2 = tf.keras.layers.Conv2D(128, 3, activation = 'relu', padding = 'same', kernel_initializer = 'he_normal')(pool1)
    conv2 = tf.keras.layers.Conv2D(128, 3, activation = 'relu', padding = 'same', kernel_initializer = 'he_normal')(conv2)
    conv2 = tf.keras.layers.BatchNormalization(axis=1, trainable=True)(conv2)
    pool2 = tf.keras.layers.MaxPooling2D(pool_size=(2, 2))(conv2)

    conv3 = tf.keras.layers.Conv2D(256, 3, activation = 'relu', padding = 'same', kernel_initializer = 'he_normal')(pool2)
    conv3 = tf.keras.layers.Conv2D(256, 3, activation = 'relu', padding = 'same', kernel_initializer = 'he_normal')(conv3)
    conv3 = tf.keras.layers.BatchNormalization(trainable=True)(conv3)
    pool3 = tf.keras.layers.MaxPooling2D(pool_size=(2, 2))(conv3)

    conv4 = tf.keras.layers.Conv2D(512, 3, activation = 'relu', padding = 'same')(pool3)
    conv4 = tf.keras.layers.Conv2D(512, 3, activation = 'relu', padding = 'same')(conv4)
    conv4 = tf.keras.layers.BatchNormalization(trainable=True)(conv4)
    drop4 = tf.keras.layers.Dropout(0.5)(conv4)
    pool4 = tf.keras.layers.MaxPooling2D(pool_size=(2, 2))(drop4)

    conv5 = tf.keras.layers.Conv2D(1024, 3, activation = 'relu', padding = 'same')(pool4)
    conv5 = tf.keras.layers.Conv2D(1024, 3, activation = 'relu', padding = 'same')(conv5)
    drop5 = tf.keras.layers.Dropout(0.5)(conv5)

    up6 = tf.keras.layers.Conv2DTranspose(512, 1, strides=(2, 2), activation='relu', padding='same')(drop5)
    merge6 = tf.keras.layers.concatenate([drop4, up6])
    conv6 = tf.keras.layers.Conv2D(512, 3, activation = 'relu', padding = 'same')(merge6)
    conv6 = tf.keras.layers.Conv2D(512, 3, activation = 'relu', padding = 'same')(conv6)

    up7 = tf.keras.layers.Conv2DTranspose(256, 1, strides=(2, 2), activation='relu', padding='same')(conv6)
    merge7 = tf.keras.layers.concatenate([conv3, up7])
    conv7 = tf.keras.layers.Conv2D(256, 3, activation = 'relu', padding = 'same')(merge7)
    conv7 = tf.keras.layers.Conv2D(256, 3, activation = 'relu', padding = 'same')(conv7)

    up8 = tf.keras.layers.Conv2DTranspose(128, 1, strides=(2, 2), activation='relu', padding='same')(conv7)
    merge8 = tf.keras.layers.concatenate([conv2, up8])
    conv8 = tf.keras.layers.Conv2D(128, 3, activation = 'relu', padding = 'same')(merge8)
    conv8 = tf.keras.layers.Conv2D(128, 3, activation = 'relu', padding = 'same')(conv8)

    up9 = tf.keras.layers.Conv2DTranspose(64, 1, strides=(2, 2), activation='relu', padding='same')(conv8)
    merge9 = tf.keras.layers.concatenate([conv1, up9])
    conv9 = tf.keras.layers.Conv2D(64, 3, activation = 'relu', padding = 'same')(merge9)
    conv9 = tf.keras.layers.Conv2D(64, 3, activation = 'relu', padding = 'same')(conv9)
    conv9 = tf.keras.layers.Conv2D(2, 1, activation = 'relu', padding = 'same')(conv9)
    
    outputs = conv9
    
    model = tf.keras.Model(inputs=[inputs], outputs=[outputs], name="unet")

    return model