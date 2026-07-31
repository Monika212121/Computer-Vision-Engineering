# Aim: Detect the document contour from a preprocessed image.

import cv2 as cv
import numpy as np
from config import APPROX_POLY_EPSILON_RATIO

from geometry import order_points, is_valid_document



class DocumentDetector:
    """
    Detect the largest valid document in an image.
    """
    def __init__(self):
        pass


    def _find_contours(self, edge_image: np.ndarray) -> list[np.ndarray]:
        """
        Find external contours.
        """
        contours, _ = cv.findContours(edge_image, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

        contours = sorted(contours, key = cv.contourArea, reverse = True)

        return contours



    def _approximate_polygon(self, contour: np.ndarray) -> np.ndarray:
        """
        Approximate contour into a polygon.
        """
        perimeter = cv.arcLength(contour, True)

        epsilon = APPROX_POLY_EPSILON_RATIO * perimeter

        polygon = cv.approxPolyDP(contour, epsilon, True)

        return polygon



    def _is_quadrilateral(self, polygon: np.ndarray) -> bool:
        """
        Check whether polygon has 4 corners.
        """
        return len(polygon) == 4



    def detect(self, edge_image: np.ndarray) -> np.ndarray | None:
        """
        Detect document.

        Returns:
            ndarray (4,2) -> Ordered document corners.
            or 
            None -> If document not found.
        """

        contours = self._find_contours(edge_image)
        print("No. of contours:", len(contours))

        image_shape = edge_image.shape
        print("image shape:", image_shape)

        for contour in contours:
            polygon = self._approximate_polygon(contour)

            if not self._is_quadrilateral(polygon):
                print("It is not a quadrilateral, polygon shape: ", polygon.shape)
                continue

            corners = polygon.reshape(4, 2).astype(np.float32)
            print("corners: ", corners)

            corners = order_points(corners)
            print("ordered points: ", corners)

            if not is_valid_document(corners, image_shape):
                print("It is not a valid document")
                continue
            
            return corners              # return first valid detected document


        return None

    