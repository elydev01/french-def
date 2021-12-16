from PyQt5 import QtCore, QtGui, QtWidgets

import res_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1030, 600)
        MainWindow.setStyleSheet(
            'QFrame[objectName="home_frame"] {\n'
            "    background-color: rgb(255, 255, 255);\n"
            "}\n"
            "\n"
            'QListWidget[objectName="history_view"] {\n'
            "    background-color: rgb(255, 255, 255);\n"
            "    padding: 10px;\n"
            "}\n"
            "\n"
            "QListWidget::item {\n"
            "    color: #444444;\n"
            "}\n"
            "\n"
            "/* QScrollArea */\n"
            "\n"
            "QScrollBar:vertical {\n"
            "    background-color: #19232D;\n"
            "    width: 12px;\n"
            "    margin: 16px 2px 16px 2px;\n"
            "    border: 1px solid #CCCCCC;\n"
            "    border-radius: 4px;\n"
            "}\n"
            "\n"
            "QScrollBar::add-line:vertical {\n"
            "    margin: 3px 0px 3px 0px;\n"
            '    border-image: url(":/styles/arrow_down_disabled.png");\n'
            "    height: 10px;\n"
            "    width: 10px;\n"
            "    subcontrol-position: bottom;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "\n"
            "QScrollBar::add-line:vertical:hover,\n"
            "QScrollBar::add-line:vertical:on {\n"
            '    border-image: url(":/arrow_down.png");\n'
            "    height: 10px;\n"
            "    width: 10px;\n"
            "    subcontrol-position: bottom;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "\n"
            "QScrollBar::sub-line:vertical {\n"
            "    margin: 3px 0px 3px 0px;\n"
            '    border-image: url(":/arrow_up_disabled.png");\n'
            "    height: 10px;\n"
            "    width: 10px;\n"
            "    subcontrol-position: top;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover,\n"
            "QScrollBar::sub-line:vertical:on {\n"
            '    border-image: url(":/arrow_up.png");\n'
            "    height: 10px;\n"
            "    width: 10px;\n"
            "    subcontrol-position: top;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "\n"
            "QScrollBar::up-arrow:vertical,\n"
            "QScrollBar::down-arrow:vertical {\n"
            "    background: #CCCCCC;\n"
            "    border-radius: 4px;\n"
            "}\n"
            ""
        )
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.screen = QtWidgets.QStackedWidget(self.centralwidget)
        self.screen.setGeometry(QtCore.QRect(10, 10, 1010, 580))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.screen.sizePolicy().hasHeightForWidth())
        self.screen.setSizePolicy(sizePolicy)
        self.screen.setStyleSheet("")
        self.screen.setObjectName("screen")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.home_frame = QtWidgets.QFrame(self.page_3)
        self.home_frame.setGeometry(QtCore.QRect(450, 165, 520, 300))
        self.home_frame.setMinimumSize(QtCore.QSize(520, 300))
        self.home_frame.setStyleSheet(
            "border: 1px solid lightgrey;\n"
            "border-radius: 8px;\n"
            "/*background-color: rgb(255, 255, 255);*/"
        )
        self.home_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.home_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.home_frame.setObjectName("home_frame")
        self.started = QtWidgets.QPushButton(self.home_frame)
        self.started.setGeometry(QtCore.QRect(180, 245, 150, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.started.setFont(font)
        self.started.setStyleSheet(
            "QPushButton {\n"
            "    border-radius: 18px;\n"
            "    padding: 10px;\n"
            "    color: #ffffff;\n"
            "    background-color: rgb(119, 127, 255);\n"
            "    border: 2px solid #777FFF;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: #777DDD;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-color: rgba(119, 122, 170, 254);\n"
            "}\n"
            ""
        )
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(":/assets/back-arrow.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.started.setIcon(icon)
        self.started.setObjectName("started")
        self.label_3 = QtWidgets.QLabel(self.home_frame)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 480, 55))
        self.label_3.setStyleSheet('font: 25 14pt "Umpush";\n' "padding: 0 15px;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.home_frame)
        self.label_4.setGeometry(QtCore.QRect(20, 95, 480, 55))
        self.label_4.setStyleSheet('font: 25 14pt "Umpush";\n' "padding: 0 15px;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.home_frame)
        self.label_5.setGeometry(QtCore.QRect(20, 170, 480, 55))
        self.label_5.setStyleSheet('font: 25 14pt "Umpush";\n' "padding: 0 15px;")
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(self.page_3)
        self.label_2.setGeometry(QtCore.QRect(60, 144, 371, 341))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/assets/book_lover.svg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.frame = QtWidgets.QFrame(self.page_3)
        self.frame.setGeometry(QtCore.QRect(320, 0, 370, 80))
        self.frame.setStyleSheet("border: none;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(20, 13, 210, 54))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n"
            "color: rgb(119, 127, 255);\n"
            "padding: 6px 0;\n"
            "border-top-left-radius: 10px;\n"
            "border-bottom-left-radius: 10px;\n"
            "border: 2px solid #777FFF;"
        )
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(230, 13, 120, 54))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(
            "color: rgb(255, 255, 255);\n"
            "background-color: rgb(119, 127, 255);\n"
            "padding: 10px 0;\n"
            "border-top-right-radius: 10px;\n"
            "border-bottom-right-radius: 10px;"
        )
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.page_3)
        self.label_8.setGeometry(QtCore.QRect(870, 530, 100, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(
            "QLabel {\n"
            "    color: rgb(114, 159, 207);\n"
            "    border-radius: 10px;\n"
            "}\n"
            "\n"
            "QLabel:hover {\n"
            "    background-color: rgba(64, 147, 191, 50);\n"
            "}"
        )
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setOpenExternalLinks(True)
        self.label_8.setObjectName("label_8")
        self.screen.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.frame_2 = QtWidgets.QFrame(self.page_4)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 1010, 60))
        self.frame_2.setStyleSheet(
            "border-bottom: 1px solid lightgrey;\n"
            "border-top: none;\n"
            "border-left: none;\n"
            "border-right: none;"
        )
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.toggle_theme = QtWidgets.QPushButton(self.frame_2)
        self.toggle_theme.setGeometry(QtCore.QRect(8, 6, 45, 45))
        self.toggle_theme.setToolTip("")
        self.toggle_theme.setToolTipDuration(-1)
        self.toggle_theme.setStyleSheet(
            "QPushButton {\n"
            "    border-top-left-radius: 22px;\n"
            "    border-bottom-left-radius: 22px;\n"
            "    border: 1px solid lightgrey;\n"
            "    padding: 10px;\n"
            "    background-color: rgba(119, 127, 255, 10);\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: rgba(255, 255, 255, 100);\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-color: rgba(119, 127, 255, 30);\n"
            "}\n"
            "\n"
            ""
        )
        self.toggle_theme.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap(":/assets/bulb-1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        self.toggle_theme.setIcon(icon1)
        self.toggle_theme.setIconSize(QtCore.QSize(30, 30))
        self.toggle_theme.setObjectName("toggle_theme")
        self.search_input = QtWidgets.QLineEdit(self.frame_2)
        self.search_input.setGeometry(QtCore.QRect(109, 6, 591, 44))
        font = QtGui.QFont()
        font.setFamily("Open Sans Light")
        font.setPointSize(12)
        self.search_input.setFont(font)
        self.search_input.setStyleSheet(
            "QLineEdit {\n"
            "    border: 1px solid lightgrey;\n"
            "    border-top-left-radius: 22px;\n"
            "    border-bottom-left-radius: 22px;\n"
            "    border-right: none;\n"
            "    padding-left: 20px;\n"
            "    padding-right: 20px;\n"
            "}\n"
            ""
        )
        self.search_input.setObjectName("search_input")
        self.search_button = QtWidgets.QPushButton(self.frame_2)
        self.search_button.setGeometry(QtCore.QRect(700, 6, 195, 44))
        font = QtGui.QFont()
        font.setFamily("Open Sans Light")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.search_button.setFont(font)
        self.search_button.setStyleSheet(
            "QPushButton {\n"
            "    border: 1px solid lightgrey;\n"
            "    border-top-right-radius: 22px;\n"
            "    border-bottom-right-radius: 22px;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: rgba(255, 255, 255, 100);\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-color: rgba(119, 127, 255, 30);\n"
            "}\n"
            ""
        )
        self.search_button.setObjectName("search_button")
        self.about = QtWidgets.QPushButton(self.frame_2)
        self.about.setGeometry(QtCore.QRect(52, 6, 45, 45))
        self.about.setStyleSheet(
            "QPushButton {\n"
            "    border-top-right-radius: 22px;\n"
            "    border-bottom-right-radius: 22px;\n"
            "    border: 1px solid lightgrey;\n"
            "    padding: 10px;\n"
            "    background-color: rgba(119, 127, 255, 10);\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: rgba(255, 255, 255, 100);\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-color: rgba(119, 127, 255, 30);\n"
            "}\n"
            "\n"
            ""
        )
        self.about.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(
            QtGui.QPixmap(":/assets/info.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        self.about.setIcon(icon2)
        self.about.setIconSize(QtCore.QSize(30, 30))
        self.about.setObjectName("about")
        self.search_exit = QtWidgets.QPushButton(self.frame_2)
        self.search_exit.setGeometry(QtCore.QRect(955, 6, 45, 45))
        self.search_exit.setStyleSheet(
            "QPushButton {\n"
            "    border-top-right-radius: 22px;\n"
            "    border-bottom-right-radius: 22px;\n"
            "    border: 1px solid lightgrey;\n"
            "    padding: 10px;\n"
            "    background-color: rgba(119, 127, 255, 10);\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: rgba(255, 255, 255, 100);\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-color: rgba(119, 127, 255, 30);\n"
            "}\n"
            "\n"
            ""
        )
        self.search_exit.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(
            QtGui.QPixmap(":/assets/logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        self.search_exit.setIcon(icon3)
        self.search_exit.setIconSize(QtCore.QSize(30, 30))
        self.search_exit.setObjectName("search_exit")
        self.reset_search = QtWidgets.QPushButton(self.frame_2)
        self.reset_search.setGeometry(QtCore.QRect(911, 6, 45, 45))
        self.reset_search.setStyleSheet(
            "QPushButton {\n"
            "    border-top-left-radius: 22px;\n"
            "    border-bottom-left-radius: 22px;\n"
            "    border: 1px solid lightgrey;\n"
            "    padding: 10px;\n"
            "    background-color: rgba(119, 127, 255, 10);\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: rgba(255, 255, 255, 100);\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-color: rgba(119, 127, 255, 30);\n"
            "}\n"
            "\n"
            ""
        )
        self.reset_search.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(
            QtGui.QPixmap(":/assets/clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        self.reset_search.setIcon(icon4)
        self.reset_search.setIconSize(QtCore.QSize(30, 30))
        self.reset_search.setObjectName("reset_search")
        self.search_response = QtWidgets.QTextEdit(self.page_4)
        self.search_response.setGeometry(QtCore.QRect(269, 59, 741, 521))
        self.search_response.setStyleSheet("")
        self.search_response.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.search_response.setReadOnly(True)
        self.search_response.setObjectName("search_response")
        self.frame_3 = QtWidgets.QFrame(self.page_4)
        self.frame_3.setGeometry(QtCore.QRect(0, 59, 270, 521))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.history_view = QtWidgets.QListWidget(self.frame_3)
        self.history_view.setGeometry(QtCore.QRect(0, 40, 270, 481))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.history_view.setFont(font)
        self.history_view.setStyleSheet("")
        self.history_view.setObjectName("history_view")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setGeometry(QtCore.QRect(40, 0, 190, 41))
        font = QtGui.QFont()
        font.setFamily("Open Sans Light")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("border: 1px solid #AAAAAA;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.filter_button = QtWidgets.QPushButton(self.frame_3)
        self.filter_button.setGeometry(QtCore.QRect(230, 0, 40, 41))
        self.filter_button.setToolTip("")
        self.filter_button.setToolTipDuration(2)
        self.filter_button.setStyleSheet(
            "QPushButton {\n"
            "    border: 1px solid lightgrey;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: rgba(255, 255, 255, 100);\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-color: rgba(119, 127, 255, 30);\n"
            "}\n"
            ""
        )
        self.filter_button.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(
            QtGui.QPixmap(":/assets/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        self.filter_button.setIcon(icon5)
        self.filter_button.setIconSize(QtCore.QSize(30, 30))
        self.filter_button.setObjectName("filter_button")
        self.reset_history = QtWidgets.QPushButton(self.frame_3)
        self.reset_history.setGeometry(QtCore.QRect(0, 0, 40, 41))
        self.reset_history.setToolTip("")
        self.reset_history.setToolTipDuration(2)
        self.reset_history.setStyleSheet(
            "QPushButton {\n"
            "    border: 1px solid lightgrey;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: rgba(255, 255, 255, 100);\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-color: rgba(119, 127, 255, 30);\n"
            "}\n"
            ""
        )
        self.reset_history.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(
            QtGui.QPixmap(":/assets/delete.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        self.reset_history.setIcon(icon6)
        self.reset_history.setIconSize(QtCore.QSize(20, 20))
        self.reset_history.setObjectName("reset_history")
        self.screen.addWidget(self.page_4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.screen.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FRENCH-DEF"))
        self.started.setText(_translate("MainWindow", "GO TO SEARCH"))
        self.label_3.setText(_translate("MainWindow", "135 000 définitions..."))
        self.label_4.setText(_translate("MainWindow", "90 000 articles..."))
        self.label_5.setText(_translate("MainWindow", "92 000 synonymes..."))
        self.label_6.setText(_translate("MainWindow", "FRENCH"))
        self.label_7.setText(_translate("MainWindow", "DEF"))
        self.label_8.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p><a style="text-decoration:none" href="https://www.larousse.fr/"><span style=" color:#777fff;">LAROUSSE.FR</span></a></p></body></html>',
            )
        )
        self.search_input.setPlaceholderText(
            _translate("MainWindow", "Entrez le mot à définir")
        )
        self.search_button.setText(_translate("MainWindow", "DÉFINITION"))
        self.search_response.setHtml(
            _translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'Noto Sans'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                '<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p></body></html>',
            )
        )
        self.label.setText(_translate("MainWindow", "HISTORIQUE"))
