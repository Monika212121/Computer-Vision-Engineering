from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

INPUT_DIR = PROJECT_ROOT / 'data' / 'input'
OUTPUT_DIR = PROJECT_ROOT / 'data' / 'output'

OUTPUT_IMAGE_NAME = 'output.jpg'



# Image processing
MAX_IMAGE_DIMENSION = 1200

GAUSSIAN_KERNEL_SIZE = (5,5)

CANNY_LOW_THRESHOLD = 30
CANNY_HIGH_THRESHOLD = 120


# Thresholding
USE_ADAPTIVE_THRESHOLD = True

ADAPTIVE_BLOCK_SIZE = 21
ADAPTIVE_C = 15


# Morphology
MORPH_KERNEL_SIZE = (11,11)
MORPH_ITERATIONS = 2



# Contour Approximation
APPROX_POLY_EPSILON_RATIO = 0.03

APPROX_RATIOS = [
    0.02,
    0.03,
    0.04,
    0.05,
]


# CLAHE
CLAHE_CLIP_LIMIT = 2.0
CLAHE_GRID_SIZE = (8,8)

