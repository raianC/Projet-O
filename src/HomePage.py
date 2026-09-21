# Display.py
from PySide6.QtWidgets import * #importe tous les widgets pip install PySide6
from PySide6.QtCore import * #importe tous les modules de base
from PIL import Image
import src.Jesus as Jesus

class HomePage(QWidget):
    def __init__(self,stack,StackList,app):
        super().__init__()
        self.setWindowTitle("Display")
        self.setMinimumSize(800, 600)
        layout = QVBoxLayout()

        self.stack = stack
        StackList["HomePage"] = self
        self.StackList = StackList
        self.app = app
        self.path = ""

        Blessingbutton = QPushButton("Bless Image")
        Blessingbutton.clicked.connect(self.ModifyImage)
        ImportButton = QPushButton("Import Image")
        ImportButton.clicked.connect(self.download_image)
        Quitbutton = QPushButton("Quit")
        Quitbutton.clicked.connect(self.app.quit)

        layout.addWidget(Blessingbutton)
        layout.addWidget(ImportButton)
        layout.addWidget(Quitbutton)

        self.setLayout(layout)

    def ModifyImage(self):
        if self.path == "":
            message_box = QMessageBox()
            message_box.setIcon(QMessageBox.Warning)
            message_box.setWindowTitle("No Image Path")
            message_box.setText("Please enter a valid image path.")
            message_box.exec()
            return

        im = Image.open(self.path)
        original = im.copy()
        Jesus.Jesus(im)
        im.save("images_modified.jpg")
        self.showResult(original,im)

    def download_image(self):
        temp = QFileDialog.getOpenFileName(self, "Select Image", "", "Image Files (*.png *.jpg *.jpeg *.bmp)")[0]
        url = QUrl.fromLocalFile(temp)
        if url.isValid():
            self.path = temp
        else:
            message_box = QMessageBox()
            message_box.setIcon(QMessageBox.Warning)
            message_box.setWindowTitle("Invalid URL")
            message_box.setText("The selected file is not a valid image.")
            message_box.exec()

    def showResult(self,original,modified):
        image_page = self.StackList["ImagePage"]
        image_page.setImages(original,modified)
        self.stack.setCurrentWidget(self.StackList["ImagePage"])