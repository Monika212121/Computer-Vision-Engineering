import cv2 as cv
from pathlib import Path
from config import OUTPUT_DIR, OUTPUT_IMAGE_NAME


from detector import DocumentDetector
from enhancer import DocumentEnhancer
from preprocesser import DocumentPreprocessor
from transformer import PerspectiveTransformer

from utils import load_image, save_image



class DocumentScanner:
    def __init__(self):
        self.preprocessor = DocumentPreprocessor()
        self.detector = DocumentDetector()
        self.transformer = PerspectiveTransformer()
        self.enhancer = DocumentEnhancer()



    def process(self, image_path: str | Path):

        image = load_image(image_path)

        preprocessed_result = self.preprocessor.run(image)

        corners = self.detector.detect(preprocessed_result.closed)
        
        if corners is None:
            raise RuntimeError("Document cound not be detected.")

        warped = self.transformer.warp(preprocessed_result.resized, corners)

        enhanced_output = self.enhancer.enhance(image= warped)

        cv.imshow("Enhanced image output", enhanced_output)

        save_image(image= enhanced_output, save_path= OUTPUT_DIR / OUTPUT_IMAGE_NAME)

        return enhanced_output

    

