# Aim: Preprocess the input image
'''
Responsibilities of this Preprocessor are :-
- 1. Resize large image
- 2. Convert to Grayscale
- 3. Reduce noise via suitable blurring technique
- 4. Extract edges
- 5. Close broken edges
- 6. Return intermediate outputs at every sub-process

'''
import cv2 as cv
import numpy as np
from dataclasses import dataclass

from config import (
    MAX_IMAGE_DIMENSION,
    GAUSSIAN_KERNEL_SIZE,
    CANNY_LOW_THRESHOLD,
    CANNY_HIGH_THRESHOLD,
    MORPH_KERNEL_SIZE,
    MORPH_ITERATIONS,
    ADAPTIVE_BLOCK_SIZE,
    ADAPTIVE_C
)


@dataclass
class PreprocessResult:
    resized: np.ndarray
    gray: np.ndarray
    blurred: np.ndarray
    binary: np.ndarray
    edges: np.ndarray
    closed: np.ndarray
    scale: float



class ImagePreprocessor:
    """
    Preprocess image beofre document detection
    """
    def __init__(self):
        pass


    def _resize(self, image: np.ndarray) -> tuple[np.ndarray, float]:
        """
        Resize while maintaining aspect ratio
        """

        h, w, _ = image.shape

        longest_side = max(h, w)

        # if input image is smaller/equal to maximum dimension, the return the original image
        if longest_side <= MAX_IMAGE_DIMENSION:
            return image.copy(), 1.0

        # else scale the image accordingly
        scale = MAX_IMAGE_DIMENSION / longest_side

        new_w = int(w * scale)
        new_h = int(h * scale)

        resized_image = cv.resize(image, (new_w, new_h), interpolation= cv.INTER_AREA)

        return resized_image, scale



    def _grayscale(self, image: np.ndarray) -> np.ndarray:
        """
        Converts BGR image to grascale
        """
        return cv.cvtColor(image, cv.COLOR_BGR2GRAY)


    def _blur(self, image: np.ndarray) -> np.ndarray:
        """
        Remove high frequency noise
        """
        return cv.GaussianBlur(image, GAUSSIAN_KERNEL_SIZE, sigmaX = 0)


    def _detect_edges(self, image: np.ndarray) -> np.ndarray:
        """
        Detect edges using Canny
        """
        return cv.Canny(image, CANNY_LOW_THRESHOLD, CANNY_HIGH_THRESHOLD)


    def _close_edges(self, edges: np.ndarray) -> np.ndarray:
        """
        Close small gaps in edges
        """
        kernel = cv.getStructuringElement(cv.MORPH_RECT, MORPH_KERNEL_SIZE)

        closed = cv.morphologyEx(edges, cv.MORPH_CLOSE, kernel, iterations = MORPH_ITERATIONS)

        return closed


    def _adaptive_threshold(self, image: np.ndarray) -> np.ndarray:
        """
        Generate a binary image using adaptive thresholding
        """
        return cv.adaptiveThreshold(
            image, 
            255, 
            cv.ADAPTIVE_THRESH_GAUSSIAN_C, 
            cv.THRESH_BINARY_INV, 
            ADAPTIVE_BLOCK_SIZE, 
            ADAPTIVE_C
        )

        
    def run(self, image: np.ndarray) -> PreprocessResult:
        """
        Complete preprocessing pipeline
        """
        resized, scale = self._resize(image)

        gray_image = self._grayscale(resized)

        smoothed_image = self._blur(gray_image)

        binary = self._adaptive_threshold(smoothed_image)

        close_morphed = self._close_edges(binary)

        edges = self._detect_edges(close_morphed)


        processed_image = PreprocessResult(
            resized= resized,
            gray= gray_image,
            blurred= smoothed_image,
            binary= binary,
            edges= edges,
            closed= close_morphed,
            scale= scale
        )

        return processed_image

