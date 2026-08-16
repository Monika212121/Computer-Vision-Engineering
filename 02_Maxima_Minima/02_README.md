# Curve Extrema Extractor

A Computer Vision challenge to detect **local maxima and minima of a curve from an image**.

This project was inspired by a real Computer Vision interview problem and was built as part of my **Vision Challenges** series.

---

## Problem

Given an image containing a curve:

- Extract the curve from the image.
- Convert it into `(x, y)` coordinates.
- Handle missing points.
- Reduce noise.
- Detect local maxima and minima.
- Visualize the detected extrema on the original image.

---

## Pipeline

```
Input Image
     ↓
Preprocessing
     ↓
Curve Extraction
     ↓
Centerline Estimation
     ↓
Missing Point Interpolation
     ↓
Signal Smoothing
     ↓
Extrema Detection
     ↓
Visualization
```

## Approach

- The curve is first extracted from the image using image processing techniques.

- Since the curve has thickness, the centerline is estimated using the topmost and bottommost curve pixels for each x coordinate: 
```center_y = (top_y + bottom_y) / 2```

- The resulting (x, y) coordinates are treated as a 1D signal.

- After smoothing the signal, local maxima and minima are detected.

- Because image coordinates have their origin at the top-left, the y direction is inverted compared to standard mathematical coordinates.


## Key Concepts Learned
- Image thresholding
- Binary masks
- Pixel coordinate extraction
- Curve / centerline extraction
- Missing data interpolation
- 1D signal processing
- Noise reduction
- Local extrema detection
- Image coordinate systems
- Visualization and validation
- Failure-case analysis


## Failure Cases

The approach can become unreliable when:

- The curve is heavily noisy.
- Large sections of the curve are missing.
- Multiple curves overlap.
- The curve merges with the background.
- Curve thickness varies significantly.
- Thresholding fails because of poor contrast.
- Small fluctuations are incorrectly detected as extrema.


## Result

The final output overlays the detected maxima and minima on the original curve image for visual verification.

```Image → Curve → 1D Signal → Extrema → Visualization```


## Level

Level 1 — Interview Problem

```Focus: Classical Computer Vision + Signal Processing```


NOTE: This is the version I'd actually keep in the repository. **Short enough to read, but it still shows the interviewer that you understood the problem, approach, failure cases, and engineering structure.**