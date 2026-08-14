# DocVision

A small **Classical Computer Vision** project built with OpenCV to detect a document from a photograph, correct its perspective, and produce a cleaner scanned-style output.

Part of my **Computer Vision Challenge Series** focused on building practical CV intuition through small problems.

---

## Problem

Given a photograph of a document:

- Detect the document boundary
- Find its four corners
- Correct perspective distortion
- Enhance the extracted document

---

## Pipeline

```text
Input Image
    ↓
Preprocessing
    ↓
Edge / Threshold Processing
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
Enhancement
    ↓
Final Document
```

## Failure Cases

1.) Non-quadrilateral contour

- A document contour may produce 5–8 vertices instead of 4.

- Cause: shadows, broken edges, perspective, or background interference.

- Approach: test multiple polygon approximation ratios.

2.) Wrong contour selected

- A background object may also form a quadrilateral.

- Cause: classical contour detection understands geometry, not the semantic concept of a document.

3.) Skewed perspective output

Possible causes:

- incorrect detected corners
- incorrect corner ordering
- poor contour approximation

4.) Noisy binary output

- Adaptive thresholding can amplify:

- paper texture
- shadows
- noise
- bleed-through writing

This showed that more preprocessing is not always better.


## Future Improvements

- Possible improvements for a stronger version:

- Candidate scoring instead of first valid contour
- Better quadrilateral selection
- minAreaRect() fallback
- Optional manual corner correction
- More robust testing

These are intentionally left out of the current learning version.