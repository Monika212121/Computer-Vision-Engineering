import cv2 as cv
import numpy as np
from pathlib import Path



def load_image(image_path: str | Path) -> np.ndarray:

    image_path = Path(image_path)

    if not image_path.exists():
        raise FileNotFoundError(f"{image_path} does not exist.")

    image = cv.imread(image_path)

    if image is None:
        raise ValueError("Failed to decode image.")
    
    return image




def save_image(image: np.ndarray, save_path: str | Path) -> None:

    save_path = Path(save_path)

    save_path.parent.mkdir(parents= True, exist_ok= True)

    cv.imwrite(str(save_path), image)

    print(f"Image saved successfully in path: {save_path}")

    return