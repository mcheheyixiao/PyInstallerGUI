from PySide6.QtWidgets import QApplication, QMainWindow
from ui_main import Ui_MainWindow
class MyWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(800, 480)

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()