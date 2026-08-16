from pathlib import Path
import cv2 as cv


PROJECT_ROOT = Path(__file__).resolve().parent.parent

INPUT_DIR = PROJECT_ROOT / 'data' / 'input'
OUTPUT_DIR = PROJECT_ROOT / 'data' / 'output'

INPUT_IMAGE_NAME = "image.png"
OUTPUT_IMAGE_NAME = 'output_curve.jpg'


THRESHOLD_VALUE = 10
THRESHOLD_TYPE = cv.THRESH_BINARY


SMOOTHENING_SIGMA = 3

DISTANCE = 30
PROMINENCE = 5