import cv2 as cv
import numpy as np

from config import CLAHE_CLIP_LIMIT, CLAHE_GRID_SIZE
from common import grayscale, adaptive_threshold, blur


class DocumentEnhancer:
    def __init__(self):
        pass


    def _apply_clahe(self, image: np.ndarray) -> np.ndarray:

        clahe = cv.createCLAHE(clipLimit= CLAHE_CLIP_LIMIT, tileGridSize = CLAHE_GRID_SIZE)

        return clahe.apply(image)


    def enhance(self, image: np.ndarray) -> np.ndarray:
        """
        Complete enhancement pipeline
        """

        gray = grayscale(image= image)

        blurred = blur(gray)

        contrast = self._apply_clahe(image= blurred)

        enhanced = adaptive_threshold(
            image= contrast,
            adaptive_method= cv.ADAPTIVE_THRESH_GAUSSIAN_C,
            threshold_type= cv.THRESH_BINARY,
            block_size= 31,
            c= 8
        )

        return enhanced