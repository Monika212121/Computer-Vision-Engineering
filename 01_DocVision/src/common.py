import cv2 as cv
import numpy as np

from config import GAUSSIAN_KERNEL_SIZE


def grayscale(image: np.ndarray) -> np.ndarray:
    """
    Converts BGR image to grascale
    """
    return cv.cvtColor(image, cv.COLOR_BGR2GRAY)



def blur(image: np.ndarray) -> np.ndarray:
    """
    Remove high frequency noise
    """
    return cv.GaussianBlur(image, GAUSSIAN_KERNEL_SIZE, sigmaX = 0)


def adaptive_threshold(
        image: np.ndarray, 
        adaptive_method: int, 
        threshold_type: int, 
        block_size: int, 
        c: float
    ) -> np.ndarray:
    """
    Generate a binary image using adaptive thresholding
    """

    return cv.adaptiveThreshold(
        image, 
        255, 
        adaptive_method, 
        threshold_type, 
        block_size, 
        c
    )