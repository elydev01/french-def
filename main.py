import sys

from PyQt5.QtWidgets import QApplication

from controllers.home import Home

# import res_rc


def main():
    app = QApplication(sys.argv)
    wind = Home()
    wind.show()
    app.exec_()


if __name__ == "__main__":
    main()
