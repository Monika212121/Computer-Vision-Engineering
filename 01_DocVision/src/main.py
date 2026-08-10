from pathlib import Path
from pipeline import DocumentScanner
import cv2 as cv


def main():
    test_image_path = Path("D:/Computer-Vision-Engineering/01_DocVision/data/input/page.jpeg")

    scanner = DocumentScanner()

    result = scanner.process(image_path= test_image_path)

    cv.imshow("Final scanned document: ", result)

    cv.waitKey(0)

    cv.destroyAllWindows()




if __name__ == "__main__":
    main()