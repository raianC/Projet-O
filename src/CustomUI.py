from PySide6.QtWidgets import * #importe tous les widgets pip install PySide6
from PySide6.QtCore import * #importe tous les modules de base
from PySide6.QtGui import QPixmap


class CustomButton(QWidget):

    clicked = Signal()

    def __init__(self,Im_Normal,Im_Pressed,Im_Hover,Button_rec):
        super().__init__()
        self.Im_Normal = QPixmap(Im_Normal)
        self.Im_Pressed = QPixmap(Im_Pressed)
        self.Im_Hover = QPixmap(Im_Hover)
        self.setFixedSize(500,200)
        self.Button_Im = QLabel(self)
        self.Button_Im.setPixmap(self.Im_Normal)
        self.Button_Im.setGeometry(0,0,500,200)
        self.Button = QPushButton(self)
        self.Button.setGeometry(Button_rec)
        self.Button.setStyleSheet("background: transparent; border: none")
        self.Button.clicked.connect(self.clicked.emit)
        self.Button.installEventFilter(self)

    def eventFilter(self, watched, event):
        if watched == self.Button:
            if event.type() == QEvent.Type.Enter:
                self.Button_Im.setPixmap(self.Im_Hover)
            elif event.type() == QEvent.Type.Leave:
                self.Button_Im.setPixmap(self.Im_Normal)
            elif event.type() == QEvent.Type.MouseButtonPress:
                if event.button() == Qt.MouseButton.LeftButton:
                    self.Button_Im.setPixmap(self.Im_Pressed)
            elif event.type() == QEvent.Type.MouseButtonRelease:
                if event.button() == Qt.MouseButton.LeftButton:
                        if self.Button.rect().contains(event.pos()):
                            self.Button_Im.setPixmap(self.Im_Hover)
                        else:
                            self.Button_Im.setPixmap(self.Im_Normal)

        return super().eventFilter(watched, event)

    