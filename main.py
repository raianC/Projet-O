# main.py
import sys
from PySide6.QtWidgets import * #importe tous les widgets pip install PySide6
from PySide6.QtCore import * #importe tous les modules de base
from PySide6 import QtGui
import src.HomePage as HomePage
import src.ImageDisplay as ImageDisplay

if __name__ == "__main__":
    app = QApplication([])
    window = QMainWindow()
    StackList  = {}

    app.setApplicationName("Jesus Image Modifier")
    app.setApplicationVersion("0.1")

    window.setWindowIcon(QtGui.QIcon("Images/Jesus.jpg"))
    window.setMinimumSize(QSize(500, 400))

    stack = QStackedWidget()
    window.setCentralWidget(stack)
    
    homePage = HomePage.HomePage(stack,StackList,app)
    ImagePage = ImageDisplay.ImageDisplay(stack,StackList)

    for name, widget in StackList.items():
            stack.addWidget(widget)

    stack.setCurrentWidget(StackList["HomePage"])

    window.show()
    sys.exit(app.exec())
    
    