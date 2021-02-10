import cv2 as cv
import numpy as np

from enum import Enum


class Noise(Enum):
    GAUSSIAN = 0
    SALT_PEPPER = 1


def noise(img, noise_type):

    def gaussian():

        rows = np.shape(img)[0]
        cols = np.shape(img)[1]

        mean = 0
        var = 1
        sigma = np.power(var, 0.5)

        gaussian = np.random.normal(mean, sigma, (rows, cols))
        gaussian = np.reshape(gaussian, (rows, cols))
        gaussian = np.uint8(gaussian)

        noisy_img = cv.addWeighted(img, 1.0, gaussian, 0.2, 0.0)

        return (noisy_img)

    def salt_pepper():
        
        rows = np.shape(img)[0]
        cols = np.shape(img)[1]

        ratio = 0.5
        volume = 0.01

        salt = np.ceil(volume * img.size * (ratio))
        salt_coordinates = [np.random.randint(0, i - 1, int(salt)) for i in img.shape]

        pepper = np.ceil(volume * img.size * (1.0 - ratio))
        pepper_coordinates = [np.random.randint(0, i - 1, int(pepper)) for i in img.shape]

        noisy_img = img
        noisy_img[tuple(salt_coordinates)] = 255
        noisy_img[tuple(pepper_coordinates)] = 0

        return (noisy_img)

    switch = {
        Noise.GAUSSIAN: gaussian(),
        Noise.SALT_PEPPER: salt_pepper()
    }

    return switch.get(noise_type)
