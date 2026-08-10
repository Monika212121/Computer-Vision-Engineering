import cv2 as cv

from config import INPUT_DIR, OUTPUT_DIR
from utils import load_image, save_image
from detector import DocumentDetector
from preprocesser import DocumentPreprocessor
from transformer import PerspectiveTransformer
from enhancer import DocumentEnhancer


image = load_image(INPUT_DIR / 'page.jpeg')

processor = DocumentPreprocessor()
result = processor.run(image)


detector = DocumentDetector()
corners = detector.detect(result.closed)
if corners is None:
    print("No document found")
    exit()

transformer = PerspectiveTransformer()
warped = transformer.warp(result.resized, corners)

enhancer = DocumentEnhancer()

enhanced_image = enhancer.enhance(image= warped)

cv.imshow("Enhanced image", enhanced_image)
save_image(enhanced_image, OUTPUT_DIR / 'enhanced1.png')

cv.waitKey(0)
cv.destroyAllWindows()