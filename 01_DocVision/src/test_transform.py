import cv2 as cv

from config import INPUT_DIR, OUTPUT_DIR
from utils import load_image, save_image
from detector import DocumentDetector
from preprocess import ImagePreprocessor
from transform import PerspectiveTransformer


image = load_image(INPUT_DIR / 'page3.jpeg')

processor = ImagePreprocessor()
result = processor.run(image)


detector = DocumentDetector()
corners = detector.detect(result.closed)

if corners is None:
    print("No document found")
    exit()

transformer = PerspectiveTransformer()
warped = transformer.warp(result.resized, corners)

cv.imshow("Warped image", warped)
save_image(warped, OUTPUT_DIR / 'warped3.png')

cv.waitKey(0)
cv.destroyAllWindows()



