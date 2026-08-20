# Aim: Extract curve points + centerline

import numpy as np
from typing import List, Tuple



class CurveExtractor:

    def __init__(self):
        pass


    def _get_curve_points(self, image: np.ndarray) -> List[Tuple[int,float]]:

        curve_points: List[Tuple[int, float]] = []

        height, width = image.shape

        print("Height: ", height, "Width: ", width)
        

        for x in range(width):
            ys = np.where(image[:, x] > 0)[0]

            if len(ys) == 0:                # missing y_value for the specific x_value
                continue

            top_y = ys.min()
            bottom_y = ys.max()

            center_y = (top_y + bottom_y) / 2.0

            curve_points.append((x, center_y))

        print("CurveExtractor -> get_curve_points(), No. of curve points: ", len(curve_points))
        return curve_points



    def _convert_curve_points(self, curve_points: List[ Tuple[int, float]]):
        curve_point_list = np.array(curve_points)

        return curve_point_list



    def extract_curve(self, image: np.ndarray) -> np.ndarray:

        curve_pts = self._get_curve_points(image= image)

        curve_points_list = self._convert_curve_points(curve_points= curve_pts)

        print("\nCurve points: ", curve_points_list)

        return curve_points_list


                
