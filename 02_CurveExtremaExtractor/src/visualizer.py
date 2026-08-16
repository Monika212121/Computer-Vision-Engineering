# Aim: Overlay calculated extremas on the original curve image

import cv2 as cv
import numpy as np
from config import OUTPUT_IMAGE_NAME, OUTPUT_DIR
from utils import save_image



class Visualizer:

    def __init__(self):
        pass


    def draw_extrema_on_curve(self, image: np.ndarray, minima: np.ndarray, maxima: np.ndarray) -> np.ndarray:

        output = image.copy()

        for x, y in maxima:
            x, y = int(round(x)), int(round(y))

            cv.circle(output, (x, y), 8, (255, 0, 0), -1)

            cv.putText(output, f"MAX ({x}, {y})", (x+10, y+10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1, cv.LINE_AA)


        for x, y in minima:
            x, y = int(round(x)), int(round(y))

            cv.circle(output, (x, y), 8, (0, 255, 0), -1)

            cv.putText(output, f"MIN ({x}, {y})", (x+10, y-10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0,255, 0), 1, cv.LINE_AA)


        save_image(image= output, save_path= OUTPUT_DIR / OUTPUT_IMAGE_NAME)
        return output

    
         


