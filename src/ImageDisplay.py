# ImageDisplay.py
from PySide6.QtWidgets import * #importe tous les widgets pip install PySide6
from PySide6.QtCore import * #importe tous les modules de base
import PySide6.QtGui as QtGui
from PIL import Image

class ImageDisplay(QWidget):
    def __init__(self, stack, StackList):
        super().__init__()
        self.setWindowTitle("Image Display")
        self.setMinimumSize(800, 600)
        layout = QVBoxLayout()
        self.stack = stack
        StackList["ImagePage"] = self
        self.StackList = StackList

        self.original_label = QLabel()
        self.modified_label = QLabel()

        self.Exitbutton = QPushButton()
        self.Exitbutton.setIcon(QtGui.QIcon("Images/HomeIcon.png"))
        self.Exitbutton.setStyleSheet("background-color: white;")
        self.Exitbutton.clicked.connect(self.ReturnToHomePage)
        self.Exitbutton.setFixedSize(50,50)
        layout.addWidget(self.Exitbutton, alignment=Qt.AlignTop | Qt.AlignLeft)

        layout.addWidget(self.original_label, alignment=Qt.AlignCenter)
        layout.addWidget(self.modified_label, alignment=Qt.AlignCenter)




        self.setLayout(layout)

    def setImages(self,original,modified):
        self.original = self.Converter(original)
        self.modified = self.Converter(modified)
        self.original_label.setPixmap(self.original)
        self.modified_label.setPixmap(self.modified)

    def Converter(self, image):
        image = image.convert("RGBA")

        data = image.tobytes("raw", "RGBA")

        NewImage = QtGui.QImage(
            data,
            image.width,
            image.height,
            QtGui.QImage.Format_RGBA8888
        )

        return QtGui.QPixmap.fromImage(NewImage)

    def ReturnToHomePage(self):
        self.stack.setCurrentWidget(self.StackList["HomePage"])