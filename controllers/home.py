import json

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget, QMainWindow, QMessageBox

from interface.home import Ui_MainWindow
from manager import api
from manager.const import home_page, search_style
from manager.history import History
from manager.theme import get_dark_theme, get_light_theme
from manager.utils import get_abspath

from .about import AboutDialog

# from PyQt5.uic import loadUiType


# Ui_MainWindow, _ = loadUiType(get_abspath(["ui", "home.ui"]))


class Home(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Home, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.theme_is_dark = False
        self.setFixedSize(1030, 600)
        self.center()
        self.init_ui()
        self.connection()

    def init_ui(self):
        """
        Initialization
        """
        self.init_autocomplete_data()
        self.init_history()
        self.search_response.setHtml(home_page)
        self.change_theme()

    def center(self):
        """
        Center window
        """
        fg = self.frameGeometry()
        qdw = QDesktopWidget().availableGeometry().center()
        fg.moveCenter(qdw)
        self.move(fg.topLeft())

    def connection(self):
        """
        Binding widgets to events
        """
        self.started.clicked.connect(lambda _: self.get_started(1))
        self.search_exit.clicked.connect(lambda _: self.get_started(0))
        self.search_button.clicked.connect(self.search)
        self.search_input.returnPressed.connect(self.search)
        self.reset_search.clicked.connect(self.clear_search)
        self.reset_history.clicked.connect(self.clear_history)
        self.toggle_theme.clicked.connect(self.change_theme)
        self.history_view.itemDoubleClicked.connect(self.item_as_clicked)
        self.about.clicked.connect(self.open_about_window)

    def get_started(self, p):
        """
        Access to search interface
        """
        self.screen.setCurrentIndex(p)

    # AUTO-COMPLETE

    def load_json_file(self):
        """
        Loading the autocomplete data file

        Returns:
            list: List of French words
        """
        with open(get_abspath(["assets", "data", "auto-complete.json"])) as f:
            data = json.loads(f.read())
        return data

    def init_autocomplete_data(self):
        """
        Initialization of the autocompletion system
        """
        self.search_input.returnPressed.connect(self.autocomplete_filter)
        autocomplete_word_list = self.load_json_file()
        self.autocomplete_model = QtGui.QStandardItemModel()
        f = self.search_input.font()
        f.setPointSize(10)

        for text in autocomplete_word_list:
            sitem = QtGui.QStandardItem(text)
            sitem.setFont(f)
            self.autocomplete_model.appendRow(sitem)

        self.completer = QtWidgets.QCompleter()
        self.completer.setModel(self.autocomplete_model)
        self.search_input.setCompleter(self.completer)

    def autocomplete_filter(self):
        """
        Auto-complete data filtering
        """
        user_input = self.search_input.text()
        items = self.autocomplete_model.findItems(
            user_input, QtCore.Qt.MatchContains | QtCore.Qt.MatchRecursive
        )
        for item in items:
            self.autocomplete_model.takeItem(item.row())

    # SEARCH ACTION

    def search(self):
        word = self.search_input.text()
        if not word or word.isspace():
            QMessageBox.warning(self, "EMPTY WORD", "Aucun mot à définir")
            return
        result = api.get_definition(word)
        self.set_result(result)
        self.add_on_history(word)

    def set_result(self, res):
        self.search_response.setHtml(search_style + res)

    def clear_search(self):
        self.search_input.setText("")
        self.search_response.setHtml(home_page)

    # HISTORIQUE

    def init_history(self):
        datas = History.get_history_data()
        for data in datas:
            self.history_view.insertItem(0, data)

    def add_on_history(self, word):
        status = History.add_new_item(word)
        if status:
            self.history_view.insertItem(0, word)

    def clear_history(self):
        self.history_view.clear()
        History.clear_all()

    def change_theme(self):
        if self.theme_is_dark:
            self.setStyleSheet(get_dark_theme())
            self.toggle_theme.setIcon(QtGui.QIcon("assets/bulb-1.png"))
        else:
            self.setStyleSheet(get_light_theme())
            self.toggle_theme.setIcon(QtGui.QIcon("assets/bulb-0.png"))
        self.theme_is_dark = not self.theme_is_dark

    def item_as_clicked(self, item):
        self.search_input.setText(item.text())
        self.search()

    @staticmethod
    def open_about_window(self, *_):
        about_diag = AboutDialog()
        about_diag.exec_()
