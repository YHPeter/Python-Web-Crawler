from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from pastpaper import Pastpaper
import sys

all_header_checkbox = []
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(517, 801)
        MainWindow.setMinimumSize(QtCore.QSize(517,801))
        MainWindow.setMaximumSize(QtCore.QSize(517,801))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.layoutWidget = QtWidgets.QWidget(MainWindow)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 481, 771))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setMouseTracking(True)
        self.label.setTabletTracking(False)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label)
        self.splitter = QtWidgets.QSplitter(self.layoutWidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.exam_office = QtWidgets.QToolButton(self.splitter)
        self.exam_office.setObjectName("exam_office")
        self.grade = QtWidgets.QToolButton(self.splitter)
        self.grade.setObjectName("grade")
        self.subject = QtWidgets.QToolButton(self.splitter)
        self.subject.setObjectName("subject")
        self.year = QtWidgets.QToolButton(self.splitter)
        self.year.setObjectName("year")
        self.month = QtWidgets.QToolButton(self.splitter)
        self.month.setObjectName("month")
        self.component = QtWidgets.QToolButton(self.splitter)
        self.component.setObjectName("component")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.splitter)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.start_search = QtWidgets.QPushButton(self.layoutWidget)
        self.start_search.setObjectName("start_search")
        self.gridLayout_2.addWidget(self.start_search, 0, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.toolButton = QtWidgets.QToolButton(self.layoutWidget)
        self.toolButton.setObjectName("toolButton")
        self.gridLayout_2.addWidget(self.toolButton, 0, 2, 1, 1)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.SpanningRole, self.gridLayout_2)
        self.progressBar = QtWidgets.QProgressBar(self.layoutWidget)
        self.progressBar.setProperty("value", 100)
        self.progressBar.setObjectName("progressBar")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.progressBar)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.info = QTableView(self.layoutWidget)
        self.info.setEnabled(True)
        self.info.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.info.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)#纵向滚轮
        self.info.setObjectName("info")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.info.setFont(font)        
        self.info.horizontalHeader().setVisible(False)#横向表头无
        self.info.verticalHeader().setVisible(False)#纵向表头无
        self.info.horizontalHeader().setStretchLastSection(True)
        self.horizontalLayout.addWidget(self.info)
        self.formLayout.setLayout(3, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout)
        self.download = QtWidgets.QPushButton(self.layoutWidget)
        self.download.setObjectName("download")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.download)
        self.store_place = QtWidgets.QPushButton(self.layoutWidget)
        self.store_place.setObjectName("store_place")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.store_place)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Pastpaper 下载器"))
        self.exam_office.setText(_translate("MainWindow", "考试局"))
        self.grade.setText(_translate("MainWindow", "年级"))
        self.subject.setText(_translate("MainWindow", "科目"))
        self.year.setText(_translate("MainWindow", "年份"))
        self.month.setText(_translate("MainWindow", "月份"))
        self.component.setText(_translate("MainWindow", "卷号"))
        self.start_search.setText(_translate("MainWindow", "GO"))
        self.lineEdit.setText(_translate("MainWindow", "Search component"))
        self.toolButton.setText(_translate("MainWindow", "多选功能"))
        self.download.setText(_translate("MainWindow", "下载所选文件、文件夹"))
        self.store_place.setText(_translate("MainWindow", "文件储存位置"))
        menu = QMenu()
        self.open_choose = QAction(QIcon("menu.ico"),"打开",menu)
        self.choose_reverse = QAction(QIcon("menu.ico"),'反选',menu)
        self.choose_all = QAction(QIcon("menu.ico"),'全选',menu)
        self.clean_choose = QAction(QIcon("menu.ico"),'全不选',menu)
        menu.addActions([self.open_choose,self.choose_reverse,self.choose_all,self.clean_choose])
        self.toolButton.setMenu(menu)
        self.toolButton.setPopupMode(QToolButton.MenuButtonPopup)


class actions(object):
    def __init__(self):
        super().__init__()
        self.display()


    def display(self):
        info_model = QStandardItemModel()
        global all_header_checkbox
        all_header_checkbox = []
        for row in range(len(pa.current_display)):
            item_checked = QStandardItem()
            item_checked.setCheckState(Qt.Unchecked)
            item_checked.setCheckable(True)
            item_checked.isDropEnabled()
            info_model.setItem(row,1, item_checked)
            all_header_checkbox.append(item_checked)
            item = QStandardItem(pa.current_display[row][0])
            info_model.setItem(row,0,item)
        ui.info.setModel(info_model)
        ui.info.setColumnWidth(1,10)
        ui.info.setColumnWidth(0,426)


    def tb_open_choose(self):
        total,open = 0,0
        print(all_header_checkbox)
        for i in range(len(all_header_checkbox)):
            print(all_header_checkbox[i].checkState())
            if all_header_checkbox[i].checkState():
                total,open = total+1,i
        if total==1:
            pa.dir_content(pa.current_display[open][1])
            print(pa.current_display)
            if pa.current_display!=[]: self.display()
            else: QMessageBox.question(None,'critical','此目录下没有文件！', QMessageBox.Ok)
        elif total>1:
            reply = QMessageBox.question(None,'critical','只能选择一个文件夹打开,是否清除已选？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply==QMessageBox.Yes: self.tb_clean_all()
        elif total==0:
            QMessageBox.question(None,'critical','需要选择一个文件夹打开', QMessageBox.Ok)

            
    def tb_choose_reverse(self):
        self.all_header_checkbox = all_header_checkbox
        for i in range(len(self.all_header_checkbox)):
            if not self.all_header_checkbox[i].checkState():
                self.all_header_checkbox[i].setCheckState(Qt.Checked)
            else:
                self.all_header_checkbox[i].setCheckState(Qt.Unchecked)


    def tb_choose_all(self):
        self.all_header_checkbox = all_header_checkbox
        for i in range(len(self.all_header_checkbox)):
            self.all_header_checkbox[i].setCheckState(Qt.Checked)


    def tb_clean_all(self):
        self.all_header_checkbox = all_header_checkbox
        for i in range(len(self.all_header_checkbox)):
            self.all_header_checkbox[i].setCheckState(Qt.Unchecked)


    def download_clicked(self):
        if pa.current_display[0][0][-3:]=='pdf':
            if pa.store_place=="":
                self.store_place()
            reply = QMessageBox.question(None,'确认', '确定下载?',QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                for i in range(len(pa.current_display)):
                    if all_header_checkbox[i].checkState():
                        pa.files_pools.append(pa.current_display[i])
                pa.single_file_urls()
        else:
            QMessageBox.question(None,'无法下载', '无法下载！不是PDF文件！',QMessageBox.Ok)


    def store_place(self):
        pa.store_place = QFileDialog.getExistingDirectory(None,'选择文件夹')
        ui.store_place.setText(pa.store_place)
    

    def serach_clicked(self):
        pass
    def exam_office_clicked(self):
        pass
    def grade_clicked(self):
        pass
    def subject_clicked(self):
        pass
    def year_clicked(self):
        pass
    def month_clicked(self):
        pass
    def component_clicked(self):
        pass

if __name__ == '__main__':
    pa = Pastpaper()
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    act = actions()
    ui.open_choose.triggered.connect(act.tb_open_choose)
    ui.choose_reverse.triggered.connect(act.tb_choose_reverse)
    ui.choose_all.triggered.connect(act.tb_choose_all)
    ui.start_search.clicked.connect(act.serach_clicked)
    ui.exam_office.clicked.connect(act.exam_office_clicked)
    ui.grade.clicked.connect(act.grade_clicked)
    ui.subject.clicked.connect(act.subject_clicked)
    ui.year.clicked.connect(act.year_clicked)
    ui.month.clicked.connect(act.month_clicked)
    ui.component.clicked.connect(act.component_clicked)
    ui.download.clicked.connect(act.download_clicked)
    ui.store_place.clicked.connect(act.store_place)

    sys.exit(app.exec_())