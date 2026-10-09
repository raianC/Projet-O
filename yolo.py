
from pathlib import Path
from ultralytics import YOLO

# Dossier contenant train.py
ROOT = Path(__file__).resolve().parent

DATA = ROOT / "dataset_yolo" / "data.yaml"

# Modèle de segmentation pré-entraîné
MODEL = "yolo26n-seg.pt"

def main():
    if not DATA.exists():
        raise FileNotFoundError(
            f"Fichier data.yaml introuvable : {DATA}"
        )

    model = YOLO(MODEL)

    model.train(
        data=str(DATA),
        epochs=10,
        imgsz=640,
        batch=8,
        device=0,
        workers=4,
        project=str(ROOT / "runs" / "segment"),
        name="water_train",
        plots=True,
        save=True
    )

if __name__ == "__main__":
    main()