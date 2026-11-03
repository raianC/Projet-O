from pathlib import Path
from ultralytics import YOLO

ROOT = Path(__file__).resolve().parent



class JesusAi:
    Im_Path = None
    
    def __init__(self):
        MODEL_PATH = (
            "C:/Users/ghost/Documents/GitHub/Projet-O/runs/segment/water_train/weights/best.pt"
        )
        self.model = YOLO(str(MODEL_PATH))
        IMAGE_PATH = Path("C:/Users/ghost/Documents/GitHub/Projet-O/Mediterranee-img.jpg.webp")
        self.Im_Path = IMAGE_PATH

    def setImagePath(self, image_path):
        IMAGE_PATH = Path(image_path)
        self.Im_Path = IMAGE_PATH
        
    def predict(self):
        return self.model.predict( source=str(self.Im_Path), imgsz=640, conf=0.25, device=0, save=True, show=True)
