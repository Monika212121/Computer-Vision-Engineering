from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

INPUT_DIR = PROJECT_ROOT / 'data' / 'input'
OUTPUT_DIR = PROJECT_ROOT / 'data' / 'output'

OUTPUT_IMAGE_NAME = 'output.jpg'



# Image processing
MAX_IMAGE_DIMENSION = 1200

GAUSSIAN_KERNEL_SIZE = (5,5)

CANNY_LOW_THRESHOLD = 75
CANNY_HIGH_THRESHOLD = 200



# Morphology
MORPH_KERNEL_SIZE = (5,5)
MORPH_ITERATIONS = 2



# Contour Approximation
APPROX_POLY_EPSILON_RATIO = 0.02



# CLAHE
CLAHE_CLIP_LIMIT = 2.0
CLAHE_GRID_SIZE = (8,8)


