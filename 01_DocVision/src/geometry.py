# Aim: Geometry helper functions for Document detection
'''
Responsibilities of these helper fucntions are:-
- 1. Order the detected corner points.
- 2. Compute width and height of document after perspective correction.
- 3. Validate that the detected shape is reasonable.

'''

import numpy as np


def euclidean_distance(p1: np.ndarray, p2: np.ndarray) -> float:
    """
    Compute Euclidean distance between 2 points.
    """
    return float(np.linalg.norm(p1 - p2))



def order_points(points: np.ndarray) -> np.ndarray:
    """
    Order 4 corner points as: top-left, top-right, bottom-right, bottom-left
    
    input -> original_points : (4,2) ndarray
    output -> ordered_points : (4,2) ndarray
    
    """
    if points.shape != (4,2):
        raise ValueError("Exactly 4 points are required")

    ordered_list = np.zeros((4,2), dtype = np.float32)

    sum = points.sum(axis= 1)

    ordered_list[0] = points[np.argmin(sum)]        # top-left
    ordered_list[2] = points[np.argmax(sum)]        # bottom-right

    diff = np.diff(points, axis = 1)

    ordered_list[1] = points[np.argmin(diff)]       # top-right
    ordered_list[3] = points[np.argmax(diff)]       # bottom-left

    #print("points: ", points, "\nsum: ", sum, "\ndiff: ",diff)

    return ordered_list



def compute_destination_size(points: np.ndarray) -> tuple[int,int]:
    """
    Compute output width and height after perspective transform.
    """
    tl, tr, br, bl = points

    width_top = euclidean_distance(tl, tr)
    width_bottom = euclidean_distance(bl, br)

    height_left = euclidean_distance(tl, bl)
    height_right = euclidean_distance(tr, br)

    width = int(max(width_top, width_bottom))
    height = int(max(height_left, height_right))

    return width, height



def destination_points(width: int, height: int) -> np.ndarray:
    """
    Destination rectangle for perspective transform.
    """

    return np.array(
        [
            [0, 0],
            [width - 1, 0],
            [width - 1, height - 1],
            [0, height - 1],
        ],
        dtype = np.float32,
    )



def polygon_area(points: np.ndarray) -> float:
    """
    Compute polygon area using the Shoelace formula.
    """    

    x = points[:, 0]
    y = points[:, 1]

    return 0.5 * abs(np.dot(x, np.roll(y, -1) - np.dot(y, np.roll(x, -1))))



def is_valid_document(points: np.ndarray, image_shape: tuple[int, int], min_area_ratio: float = 0.15) -> bool:
    """"
    Basic validation for detected document.

    Checks:
    - Exactly 4 points
    - Sufficiently large area
    """

    # 1. Reject polygons other than quadrilateral
    if points.shape != (4,2):
        return False

    width, height = image_shape[0], image_shape[1]

    # 2. Reject very small document
    image_area =  width * height                        # area = width * height

    doc_area = polygon_area(points)

    doc_area_ratio = doc_area / image_area

    area_ratio_validity = doc_area_ratio >= min_area_ratio

    # 3. Reject unreasonable aspect ratio
    aspect_ratio = width / height                       # aspect_ratio = width / height

    aspect_ratio_validity = True if (aspect_ratio <= 2.5 and aspect_ratio > 0.4) else False

    # 4. Reject tiny dimensions
    size_validity = True if (width > 150 and height > 150) else False

    is_valid_document = area_ratio_validity and aspect_ratio_validity and size_validity

    return is_valid_document

