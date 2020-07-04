from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.x_input = QtWidgets.QLineEdit(self.centralwidget)
        self.x_input.setGeometry(QtCore.QRect(30, 10, 61, 21))
        self.x_input.setObjectName("x_input")
        self.z_input = QtWidgets.QLineEdit(self.centralwidget)
        self.z_input.setGeometry(QtCore.QRect(30, 70, 61, 21))
        self.z_input.setObjectName("z_input")
        self.y_input = QtWidgets.QLineEdit(self.centralwidget)
        self.y_input.setGeometry(QtCore.QRect(30, 40, 61, 21))
        self.y_input.setObjectName("y_input")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(110, 10, 311, 161))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(20, 100, 75, 23))
        self.addButton.setObjectName("addButton")
        self.ydisp = QtWidgets.QLineEdit(self.centralwidget)
        self.ydisp.setGeometry(QtCore.QRect(540, 50, 61, 21))
        self.ydisp.setObjectName("ydisp")
        self.xdisp = QtWidgets.QLineEdit(self.centralwidget)
        self.xdisp.setGeometry(QtCore.QRect(470, 50, 61, 21))
        self.xdisp.setObjectName("xdisp")
        self.zdisp = QtWidgets.QLineEdit(self.centralwidget)
        self.zdisp.setGeometry(QtCore.QRect(620, 50, 61, 21))
        self.zdisp.setObjectName("zdisp")
        self.sumColButton = QtWidgets.QPushButton(self.centralwidget)
        self.sumColButton.setGeometry(QtCore.QRect(460, 20, 75, 23))
        self.sumColButton.setObjectName("sumColButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "x"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "y"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "z"))
        self.addButton.setText(_translate("MainWindow", "Add Row"))
        self.sumColButton.setText(_translate("MainWindow", "Sum Column"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())










    # def cellButtonClicked(self):
    #     print("Cell Button Clicked", self.sender().index)



    # # 列表内添加按钮
    # def buttonForRow(self,id):
    #     widget=QWidget()
    #     # 修改
    #     updateBtn = QPushButton('修改')
    #     updateBtn.setStyleSheet(''' text-align : center;
    #                                       background-color : NavajoWhite;
    #                                       height : 30px;
    #                                       border-style: outset;
    #                                       font : 13px  ''')

    #     updateBtn.clicked.connect(lambda: print(id))

    #     # 查看
    #     viewBtn = QPushButton('查看')
    #     viewBtn.setStyleSheet(''' text-align : center;
    #                               background-color : DarkSeaGreen;
    #                               height : 30px;
    #                               border-style: outset;
    #                               font : 13px; ''')

    #     viewBtn.clicked.connect(lambda: print(id))

    #     # 删除
    #     deleteBtn = QPushButton('删除')
    #     deleteBtn.setStyleSheet(''' text-align : center;
    #                                 background-color : LightCoral;
    #                                 height : 30px;
    #                                 border-style: outset;
    #                                 font : 13px; ''')


    #     hLayout = QHBoxLayout()
    #     hLayout.addWidget(updateBtn)
    #     hLayout.addWidget(viewBtn)
    #     hLayout.addWidget(deleteBtn)
    #     hLayout.setContentsMargins(5,2,5,2)
    #     widget.setLayout(hLayout)
    #     return widget
    # def GenerateBtn(self,dir_url):
    #     widget=QWidget()
    #     viewBtn = QPushButton('查看')
    #     viewBtn.setStyleSheet(''' text-align : center;
    #                           background-color : DarkSeaGreen;
    #                           height : 30px;
    #                           border-style: outset;
    #                           color:white;
    #                           font : 13px; ''')
    #     viewBtn.clicked.connect(lambda: print(1))
    #     hLayout = QHBoxLayout()
    #     hLayout.addWidget(viewBtn)
    #     hLayout.setContentsMargins(5,2,5,2)
    #     return widget