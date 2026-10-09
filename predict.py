
from pathlib import Path
from ultralytics import YOLO

ROOT = Path(__file__).resolve().parent

MODEL_PATH = (
    "C:\\Users\\raian\\Documents\\GitHub\\Projet-O\\segment\\runs\\eau\\segmentation-6\\weights\\best.pt"
)

# Modifie ce chemin pour sélectionner une image.
IMAGE_PATH = Path("C:/Users/raian/Documents/GitHub/Projet-O/images.jpg")


def main():

    model = YOLO(str(MODEL_PATH))

    model.predict(
        source=str(IMAGE_PATH),
        imgsz=640,
        conf=0.25,
        device=0,
        save=True,
        show=True
    )


if __name__ == "__main__":
    main()