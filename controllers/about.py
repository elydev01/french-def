from PyQt5.QtWidgets import QDesktopWidget, QDialog

from interface.about import Ui_Dialog

# from PyQt5.uic import loadUiType

# from manager.utils import get_abspath


# Ui_Dialog, _ = loadUiType(get_abspath(["ui", "about.ui"]))


class AboutDialog(QDialog, Ui_Dialog):
    """
    About
    """

    def __init__(self, parent=None):
        super(AboutDialog, self).__init__(parent)
        QDialog.__init__(self)
        self.setupUi(self)
        self.setFixedSize(410, 410)
        self.init_all()

    def init_all(self):
        self.close_about_btn.clicked.connect(self.close)

        fg = self.frameGeometry()
        qdw = QDesktopWidget().availableGeometry().center()
        fg.moveCenter(qdw)
        self.move(fg.topLeft())

    def show_dialog(self):
        self.show()
        self.exec_()
