from utils import load_image
from config import INPUT_DIR
from detector import DocumentDetector
from preprocess import ImagePreprocessor

image = load_image(INPUT_DIR / 'messi.jpg')

preprocessor = ImagePreprocessor()

result = preprocessor.run(image)

detector = DocumentDetector()
corners = detector.detect(result.closed)

print("Final detected document corners: ", corners)
