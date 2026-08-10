# Aim: Perspective transformation for document scanning

import cv2 as cv
import numpy as np

from geometry import compute_destination_size, destination_points



class PerspectiveTransformer:
    """
    Perform perspective correction on a detected document.
    """
    def __init__(self):
        pass


    def warp(self, image: np.ndarray, corners: np.ndarray) -> np.ndarray:
        """
        Warp document into a top-down view.

        Parameters
        -------------------
        image: np.ndarray -> Original resized image

        corners: ndarray -> Ordered document corners [top-left, top-right, bottom-right, bottom-left]

        Returns
        -------------------
        ndarray: Perspective corrected docuement.
        """

        width, height = compute_destination_size(corners)
        print("width: ", width, "height: ", height)

        dst = destination_points(width, height)

        transform_matrix = cv.getPerspectiveTransform(corners, dst)

        warped = cv.warpPerspective(image, transform_matrix, (width, height))

        return warped
