# Aim: Detecting Maxima and Minima

import numpy as np
from typing import Tuple
from scipy.signal import find_peaks

from config import DISTANCE, PROMINENCE



class ExtremaDetector:

    def __init__(self):
        self.maxima_indices: np.ndarray
        self.minima_indices: np.ndarray



    def find_extrema_indices(self, smoothed_y: np.ndarray):

        maxima_indices, maximum_properties = find_peaks(-smoothed_y, distance= DISTANCE, prominence= PROMINENCE)

        minima_indices, minimum_properties = find_peaks(smoothed_y, distance= DISTANCE, prominence= PROMINENCE)

        self.maxima_indices = maxima_indices
        self.minima_indices = minima_indices

        return



    def find_extremas(self, full_x: np.ndarray, smoothed_y : np.ndarray) -> Tuple[np.ndarray, np.ndarray]:

        # Finding extrema indices first
        self.find_extrema_indices(smoothed_y= smoothed_y)

        # Finding extrema values (x and y for each maxima/minima)
        # Keeping extremas' corrosponding x and y values together to make coordinates
        maxima = np.column_stack((full_x[self.maxima_indices], smoothed_y[self.maxima_indices]))

        minima = np.column_stack((full_x[self.minima_indices], smoothed_y[self.minima_indices]))

        print("Maxima: ", maxima)
        print("\nMinima: ", minima)

        return (maxima, minima)
    

        



