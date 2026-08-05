# Aim: To test Image preprocessor

import cv2 as cv

from config import INPUT_DIR, OUTPUT_DIR
from utils import load_image, save_image 
from preprocess import ImagePreprocessor


test_image = load_image(INPUT_DIR / 'page1.jpeg')

preprocessor = ImagePreprocessor()

result = preprocessor.run(test_image)


cv.imshow("RESIZED IMAGE", result.resized)
cv.imshow("GRAY IMAGE", result.gray)
cv.imshow("BLURRED IMAGE", result.blurred)
cv.imshow("EDGES IMAGE", result.edges)
cv.imshow("CLOSE MORPHED IMAGE", result.closed)

# Saving intermediate images
save_image_path = OUTPUT_DIR

save_image(result.blurred, save_image_path / 'blur.png')
save_image(result.edges, save_image_path / 'edges.png')
save_image(result.closed, save_image_path / 'close_morphed.png')


cv.waitKey(0)
cv.destroyAllWindows()