import cv2 as cv
import numpy as np
from config import THRESHOLD_VALUE, THRESHOLD_TYPE




class ImagePreprocessor:
    def __init__(self):
        pass


    def _apply_grayscale(self, image: np.ndarray) -> np.ndarray:
        """
        Converts BGR image to grascale
        """
        gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

        return gray_image



    def _apply_threshold(self, image: np.ndarray) -> np.ndarray:
        """
        Creates a binary mask over the image
        """
        _, binary = cv.threshold(image, THRESHOLD_VALUE, 255, THRESHOLD_TYPE)

        return binary



    def process(self, image: np.ndarray) -> np.ndarray:

        gray_image = self._apply_grayscale(image = image)

        binary_image = self._apply_threshold(image= gray_image)

        return binary_image




        