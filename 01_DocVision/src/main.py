from pathlib import Path
from pipeline import DocumentScanner



def main():
    test_image_path = Path("D:/Computer-Vision-Engineering/01_DocVision/data/input/test.jpg")

    scanner = DocumentScanner()

    scanner.process()



if __name__ == "__main__":
    main()