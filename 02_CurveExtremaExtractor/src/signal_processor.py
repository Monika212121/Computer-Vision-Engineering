# Aim: Find Missing values + Interpolation + Smoothening

import numpy as np
from config import SMOOTHENING_SIGMA
from scipy.ndimage import gaussian_filter1d



class SignalProcessor:

    def __init__(self):
        self.full_x: np.ndarray
        self.full_y: np.ndarray



    def _find_all_values(self, curve_points: np.ndarray):

        x_values = curve_points[:, 0]

        x_start = int(x_values.min())
        x_end = int(x_values.max())

        self.full_x = np.arange(x_start, x_end + 1)
        self.full_y = np.full(len(self.full_x), np.nan)

        for x, y in curve_points:
            self.full_y[int(x - x_start)] = y

        missing_values = np.isnan(self.full_y).sum()

        print("full_x: ", len(self.full_x))
        print("full_y: ", len(self.full_y))

        print("Missing curve points: ", missing_values)

        return



    def _interpolate_missing_values(self) -> np.ndarray:
        valid = ~np.isnan(self.full_y)

        interpolated_y = self.full_y.copy()

        interpolated_y[~valid] = np.interp(self.full_x[~valid], self.full_x[valid], self.full_y[valid])

        return interpolated_y



    def _smooth_curve(self, interpolated_y: np.ndarray) -> np.ndarray:
        smoothed_curve = gaussian_filter1d(interpolated_y, sigma= SMOOTHENING_SIGMA)

        return smoothed_curve



    def process_curve_points(self, curve_points: np.ndarray) -> np.ndarray:

        self._find_all_values(curve_points= curve_points)

        interpolated_y = self._interpolate_missing_values()

        smoothed_curve = self._smooth_curve(interpolated_y= interpolated_y)

        return smoothed_curve

