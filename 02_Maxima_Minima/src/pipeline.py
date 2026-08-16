from utils import load_image
from config import INPUT_DIR, INPUT_IMAGE_NAME

from visualizer import Visualizer
from preprocessor import ImagePreprocessor
from curve_extractor import CurveExtractor
from signal_processor import SignalProcessor
from extrema_detector import ExtremaDetector



class Pipeline:
    def __init__(self):
        self.processor = ImagePreprocessor()
        self.curve_extractor = CurveExtractor()
        self.signal_processor = SignalProcessor()
        self.extrema_detector = ExtremaDetector()

        self.visualizer = Visualizer()



    def run(self):

        # Load curve image
        image = load_image(image_path= INPUT_DIR / INPUT_IMAGE_NAME)

        # Preprocess image
        binary_image = self.processor.process(image= image)

        # Extract curve from the binary image
        curve_points_list = self.curve_extractor.extract_curve(image= binary_image)

        # Detect extremas(maxima + minima) from the x and y values
        smoothed_curve = self.signal_processor.process_curve_points(curve_points= curve_points_list)     # smoothed y values
        full_x = self.signal_processor.full_x

        # Finding extremas of the curve
        maxima, minima = self.extrema_detector.find_extremas(full_x= full_x, smoothed_y= smoothed_curve)

        # Draw extreme points (MAXIMA + MINIMA) on the orignal provided curve
        output_curve = self.visualizer.draw_extrema_on_curve(image= image, maxima= maxima, minima= minima)

        return output_curve




    