import cv2 as cv
from pipeline import Pipeline



def main():

    extrema_extractor = Pipeline()

    output_curve = extrema_extractor.run()

    cv.imshow("Extracted Maxima and Minima", output_curve)

    cv.waitKey(0)

    cv.destroyAllWindows()



if __name__ == "__main__":
    main()
