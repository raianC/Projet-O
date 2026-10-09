
from pathlib import Path
from ultralytics import YOLO

ROOT = Path(__file__).resolve().parent

MODEL_PATH = (
    ROOT / "runs" / "segment" / "water_train"
    / "weights" / "best.pt"
)

DATA = ROOT / "dataset_yolo" / "data.yaml"


def main():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"Modèle introuvable : {MODEL_PATH}\n"
            "Lance d'abord train.py."
        )

    model = YOLO(str(MODEL_PATH))

    metrics = model.val(
        data=str(DATA),
        split="test",
        imgsz=640,
        batch=8,
        device=0,
        plots=True
    )

    print("\n--- Résultats du test ---")
    print("mAP50 :", metrics.seg.map50)
    print("mAP50-95 :", metrics.seg.map)


if __name__ == "__main__":
    main()