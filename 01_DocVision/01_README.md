# DocVision --- Classical Computer Vision Document Scanner

DocVision is a small classical Computer Vision learning challenge, built with OpenCV.

The goal is to detect a photographed document, find its four corners, correct perspective distortion, and produce a cleaner scanner-like output.

**Project goal**: Learn CV reasoning, debugging, geometry, and OpenCV implementation --- not build a production document-scanning application.

1. Problem Statement

Given a photograph containing a paper document:

detect the document boundary

find its four corners

correct perspective distortion

enhance the extracted document

save/display the result

Input: A document photographed from an arbitrary position or angle.

Output: A perspective-corrected document that is approximately rectangular andeasier to read.

2. Pipeline
```
Input Image
    ↓
Resize
    ↓
Grayscale
    ↓
Gaussian Blur
    ↓
Threshold / Edge Processing
    ↓
Morphological Closing
    ↓
Contour Detection
    ↓
Polygon Approximation
    ↓
Quadrilateral Validation
    ↓
Corner Ordering
    ↓
Perspective Transform
    ↓
Grayscale / CLAHE Enhancement
    ↓
Final Document
```
The important design decision is to keep detection, geometry,transformation, and enhancement separate so each stage can beinspected independently.

3. Computer Vision Concepts Practiced

Preprocessing

image resizing

grayscale conversion

Gaussian filtering

thresholding

Canny edge detection

morphological closing

Shape detection

contour extraction

contour area

contour perimeter

cv2.approxPolyDP

quadrilateral detection

geometric validation

Geometry

corner ordering

perspective transformation

homography

coordinate mapping

image warping

Enhancement

grayscale conversion

CLAHE

adaptive thresholding

understanding illumination, noise, texture, and bleed-through

4. Project Structure
```
DocVision/
│
├── src/
│   ├── config.py
│   ├── utils.py
│   ├── preprocess.py
│   ├── geometry.py
│   ├── detector.py
│   ├── transform.py
│   ├── enhance.py
│   ├── pipeline.py
│   ├── main.py
│   └── test_detector.py
│
├── data/
│   ├── test/
│   │   ├── 01_straight_top_view.png
│   │   ├── 02_rotated_10_clockwise.png
│   │   ├── 03_rotated_20_counter_clockwise.png
│   │   └── ...
│   │
│   └── output/
│
└── README.md
```


5. Document Detection

The detector follows this general reasoning:
```
Contours
    ↓
Candidate contour
    ↓
Polygon approximation
    ↓
4 vertices?
    ↓
Extract corners
    ↓
Order corners
    ↓
Geometric validation
    ↓
Valid document
```

For a candidate contour:

Calculate its perimeter.

Approximate it using cv2.approxPolyDP.

Check whether the approximation has four vertices.

Extract the four points.

Order them consistently as top-left, top-right, bottom-right,bottom-left.

Validate the candidate.

Return a valid document candidate.

6. Polygon Approximation: Important Debugging Lesson

Initially, one epsilon value was used:

epsilon = ratio * perimeter

Some real document contours were not simplified to four vertices. Theyproduced shapes such as:

8 vertices
6 vertices
5 vertices

even though the contour represented the document.

The solution was to test several approximation ratios:

APPROX_RATIOS = [
    0.02,
    0.03,
    0.04,
    0.05,
]

This made the detector more tolerant of imperfect document boundaries.

Lesson

approxPolyDP is an approximation algorithm. A real photographed pagedoes not necessarily produce exactly four vertices for one fixedepsilon.

The important CV habit is:

Inspect the contour and intermediate output before changingparameters.

7. Perspective Transformation

After detection, the four corners are ordered consistently:
```
TL ---------------- TR
|                    |
|      DOCUMENT      |
|                    |
BL ---------------- BR
```
These points are mapped to a rectangular destination.

Conceptually:
```
Photographed page             Corrected page

      /---------/              +---------+
     /         /               |         |
    /         /       --->     |         |
   /---------/                 +---------+
```
This is a perspective/projective transformation, not simply arotation.

8. Enhancement

The enhancement stage was intentionally kept small.

The main tested pipeline is:
```
Warped document
      ↓
Grayscale
      ↓
CLAHE
      ↓
Enhanced grayscale document
```
Adaptive thresholding was also tested to create a binary scanner-likeresult.

However, testing showed an important failure: aggressive adaptivethresholding can amplify:

paper texture

faint background marks

shadows

camera noise

writing visible through the paper

Therefore, binary thresholding is treated as an optional result,rather than something that must always be applied.

Important lesson

More preprocessing is not automatically better.

Every operation should have a reason and should be validated on actualimages.

9. Test Set

A small set of document images was used to test different conditions:

straight document

small clockwise rotation

counter-clockwise rotation

perspective from one side

perspective from the other side

larger rotation

dark background

textured background

uneven lighting/shadows

difficult angle + lighting

The purpose of the test set is not to force a 10/10 score.

The purpose is to answer:
```
What works?
What fails?
Why does it fail?
Which CV stage caused the failure?
```
10. Failure Cases

Failure 1 --- Document contour is not a quadrilateral

Observation

A document contour can produce 8, 6, or 5 vertices instead of four.

Possible causes

shadows

broken page boundaries

folds

background edges

thresholding artifacts

perspective

Response

Try several approxPolyDP epsilon ratios rather than relying on onevalue.

Lesson

Polygon approximation is parameter-dependent.

Failure 2 --- Wrong quadrilateral selected

Observation

The detector can find a valid four-sided shape that belongs to thebackground rather than the document.

Cause

Classical contour detection sees edges and shapes, not the semanticconcept of "document."

Lesson

len(polygon) == 4

is not enough.

A stronger detector should score candidates using properties such as:

area

rectangularity

aspect ratio

angle consistency

position

Failure 3 --- Correct detection but skewed output

Observation

A document is detected, but the warped result is still skewed.

Possible causes

incorrect corner positions

incorrect corner ordering

approximate contour does not match true page corners

wrong quadrilateral selected

Debugging method

Draw the four detected points on the original image:

TL ---------------- TR
|                    |
|      DOCUMENT      |
|                    |
BL ---------------- BR

If the points are wrong, investigate detection.

If the points are correct, investigate the perspective transformation.

Lesson

Separate detection errors from transformation errors.

Failure 4 --- Text becomes noisy after thresholding

Observation

The final binary image contains many black artifacts and faint unwantedmarks.

Cause

Adaptive thresholding reacts to local intensity differences. Thosedifferences may come from paper texture or writing visible through thepage.

Lesson

A clean grayscale result can be better than an aggressively binarizedresult.

Failure 5 --- Background interferes with contour detection

Observation

The detector selects background edges or fails to find the page.

Cause

A textured or high-contrast background can create strong contours.

Lesson

Classical CV depends heavily on assumptions about the scene.

Failure 6 --- Uneven illumination

Observation

A page boundary becomes difficult to detect under strong shadows ornon-uniform lighting.

Cause

Shadows can break edges, create additional contours, or merge thedocument boundary with the background.

Lesson

Illumination is part of the Computer Vision problem.

11. Testing / Debugging Method

For each test image, record:

Image   Detection   Perspective   Enhancement   Observation

01      PASS/FAIL   PASS/FAIL     PASS/FAIL     ...02      PASS/FAIL   PASS/FAIL     PASS/FAIL     ...03      PASS/FAIL   PASS/FAIL     PASS/FAIL     ...

Do not immediately change the algorithm after every failed image.

First run the complete test set.

Then group failures by cause.

For example:

7/10 passed

Failure group A:
wrong contour selected → 2 images

Failure group B:
thresholding artifacts → 1 image

Then fix the underlying CV issue and retest.

12. Useful Debug Outputs

During development, inspect intermediate stages:
```
original
   ↓
resized
   ↓
gray
   ↓
threshold
   ↓
edges
   ↓
morphological result
   ↓
detected contour
   ↓
detected corners
   ↓
warped document
   ↓
enhanced document
```
A particularly useful detector debug image is one with the four detectedcorners drawn and labelled.

This makes it immediately obvious whether a failure comes from detectionor transformation.

13. Potential Version 2 Improvements

This project is intentionally not being turned into a productionscanner.

If more robustness were required, reasonable next improvements would be:

Candidate scoring

Instead of returning the first valid quadrilateral:

Candidate 1 ─┐
Candidate 2 ─┤
Candidate 3 ─┼→ score → best candidate
Candidate 4 ─┘

Possible scoring features:

contour area

rectangularity

aspect ratio

angle consistency

distance from image borders

Geometry fallback

If approxPolyDP cannot provide four corners, a minimum-area rectanglecould be considered as a fallback.

Better corner ordering

Test a more robust ordering strategy for unusual orientations.

Optional manual correction

A real scanner application could display the detected boundary and allowthe user to adjust the four corners.

These were intentionally not implemented because this is a learningchallenge, not a production application.

14. What This Challenge Taught Me

The main learning was not memorizing OpenCV functions.

It was learning the debugging chain:

Problem
   ↓
Preprocess
   ↓
Extract useful image structure
   ↓
Detect candidate geometry
   ↓
Validate geometry
   ↓
Transform
   ↓
Enhance
   ↓
Test
   ↓
Analyze failures
   ↓
Improve

Key lessons

1. Intermediate outputs matter

When a CV pipeline fails, inspect the stages rather than only looking atthe final image.

2. Parameters are data-dependent

Values such as epsilon, threshold block size, threshold constant, andkernel size depend on the image conditions.

3. Detection and transformation are different problems

Incorrect corners cannot be fixed by changing the perspectivetransformation.

4. More preprocessing is not always better

Every filter or enhancement operation can introduce new artifacts.

5. Failure analysis is a core CV skill

A strong solution should explain not only that an algorithm failed, butalso why it failed and what evidence supports that diagnosis.

15. Interview Questions Covered by This Project

Why use contours?

Contours provide connected boundaries that are useful for detectinggeometric objects such as document borders.

Why use approxPolyDP?

It simplifies a contour into a polygon while controlling approximationerror.

Why calculate contour area?

It helps reject tiny irrelevant contours and prioritize large candidateregions.

Why order the four corners?

The perspective transformation requires corresponding source anddestination points in a consistent order.

Is perspective transformation the same as rotation?

No. Rotation is a specific geometric transformation. Perspectivetransformation can model projective distortion caused by viewing aplanar object from an angle.

Why can adaptive thresholding fail?

Because it responds to local intensity variations, including unwantedvariations such as texture, shadows, noise, and bleed-through.

Why not always choose the largest contour?

The largest contour is not guaranteed to be the document. Backgroundregions can sometimes produce larger contours.

16. Final Takeaway

DocVision is deliberately a small classical Computer Visionchallenge.

The goal was to practice:

preprocessing

edge detection

morphology

contour analysis

polygon approximation

geometric validation

perspective transformation

image enhancement

systematic testing

failure analysis

The project is considered complete when the pipeline works on reasonabledocument images and its limitations are understood and documented.

The next step is not to keep adding complexity. The better learningstrategy is to move to a different CV problem and apply the sameworkflow again.
```
Build
  ↓
Test
  ↓
Observe
  ↓
Diagnose
  ↓
Improve
  ↓
Retest
  ↓
Document
  ↓
Move to next CV challenge
```

### Author

Built as part of a personal Computer Vision Challenge Series focused on developing practical Computer Vision intuition through small, progressively harder problems.