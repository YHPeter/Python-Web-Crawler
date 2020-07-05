# -*- utf-8 -*-
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import re,requests,os,sys,queue,time
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
ua = UserAgent()


all_header_checkbox = []
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(617, 901)
        MainWindow.setMinimumSize(QtCore.QSize(617, 901))
        MainWindow.setMaximumSize(QtCore.QSize(617, 901))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.layoutWidget = QtWidgets.QWidget(MainWindow)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 581, 871))
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
        self.back = QtWidgets.QToolButton(self.splitter)
        self.back.setObjectName("back")
        self.open = QtWidgets.QToolButton(self.splitter)
        self.open.setObjectName("open")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.splitter)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.current_dir = QtWidgets.QLabel(self.layoutWidget)
        self.current_dir.setObjectName("current_dir")
        self.gridLayout_2.addWidget(self.current_dir, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setEnabled(False)
        self.gridLayout_2.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.toolButton = QtWidgets.QToolButton(self.layoutWidget)
        self.toolButton.setObjectName("toolButton")
        self.gridLayout_2.addWidget(self.toolButton, 0, 2, 1, 1)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.SpanningRole, self.gridLayout_2)
        self.single_progressBar = QtWidgets.QProgressBar(self.layoutWidget)
        self.single_progressBar.setProperty("value", 0)
        self.single_progressBar.setObjectName("single_progressBar")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.single_progressBar)
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
        self.back.setText(_translate("MainWindow", "上一级文件夹"))
        self.open.setText(_translate("MainWindow", "打开文件夹"))
        self.current_dir.setText(_translate("MainWindow", "当前文件夹"))
        self.lineEdit.setText(_translate("MainWindow", "Search component"))
        self.toolButton.setText(_translate("MainWindow", "多选功能"))
        self.download.setText(_translate("MainWindow", "下载所选文件、文件夹"))
        self.store_place.setText(_translate("MainWindow", "文件储存位置"))
        menu = QMenu()
        self.choose_reverse = QAction(QIcon("menu.ico"),'反选',menu)
        self.choose_all = QAction(QIcon("menu.ico"),'全选',menu)
        self.clean_all = QAction(QIcon("menu.ico"),'全不选',menu)
        menu.addActions([self.choose_reverse,self.choose_all,self.clean_all])
        self.toolButton.setMenu(menu)
        self.toolButton.setPopupMode(QToolButton.MenuButtonPopup)

    def download_files_start(self):
        self.single_progressBar.setValue(0)
        self.download.setText("下载完成！")
        self.download.setText("继续下载所选文件")
        self.download.setDisabled(False)
        self.download.setText("正在下载...")
        self.download.setDisabled(True)
        self.workthread = WorkThread()
        self.workthread.progressBarValue.connect(ui.single_progressBar.setValue)
        self.workthread.start()
        

class actions(object):
    def __init__(self):
        super().__init__()
        self.display()
        self.current = 'Home'
        ui.lineEdit.setText(self.current)

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
        ui.info.setColumnWidth(1,1)
        ui.info.setColumnWidth(0,526)

    def open_clicked(self):
        total,open = 0,0
        for i in range(len(all_header_checkbox)):
            if all_header_checkbox[i].checkState():
                if not (pa.current_display[0][0][-3:]=='pdf' or pa.current_display[0][0][-3:]=='PDF'):
                    total,open = total+1,i
                else:
                    QMessageBox.question(None,'注意','PDF文件无法打开哦！', QMessageBox.Ok)
        if total==1:
            cur = pa.current_display[open][1]
            if pa.dir_content(pa.current_display[open][1]):
                self.current = cur
                self.display()
                ui.lineEdit.setText(self.current.replace('?dir=',''))
            else: QMessageBox.question(None,'注意','此目录下没有文件！', QMessageBox.Ok)
        elif total>1:
            reply = QMessageBox.question(None,'注意','只能选择一个文件夹打开,是否清除已选？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply==QMessageBox.Yes: self.tb_clean_all()
        elif total==0:
            QMessageBox.question(None,'注意','需要选择一个文件夹打开', QMessageBox.Ok)

    def back_clicked(self):
        home_urls = ['/cie/?dir=A-Level','/cie/?dir=IGCSE','/cie/?dir=O-Level',
        '/cie/?dir=Pre-U','/aqa/?dir=A-Level','/aqa/?dir=GCSE','/ccea/?dir=GCSE',
        '/ccea/?dir=GCE-A-Level','/ocr/?dir=A-Level','/ocr/?dir=GCSE']
        if self.current=='Home': return None
        if self.current in home_urls:
            pa.current_display = sorted(pa.home_choose)
            self.display()
            self.current = 'Home'
            ui.lineEdit.setText(self.current)
        else:
            self.current = '/'.join(self.current.split('/')[:-1])
            pa.dir_content(self.current)
            ui.lineEdit.setText(self.current.replace('?dir=',''))
            self.display()
            
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
        pa.files_pools.clear
        if pa.current_display[0][0][-3:]=='pdf' or pa.current_display[0][0][-3:]=='PDF':
            if pa.store_place=="":
                self.store_place()
            reply = QMessageBox.question(None,'确认', '确定下载?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                for i in range(len(pa.current_display)):
                    if all_header_checkbox[i].checkState():
                        pa.files_pools.append(pa.current_display[i])
                ui.download_files_start()
        else:
            QMessageBox.question(None,'警告', '无法下载！不是PDF文件！',QMessageBox.Ok)

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


class Pastpaper(object):
    def __init__(self):
        """Initial Pastaper Project"""
        super(Pastpaper).__init__()
        self.domain_url = "https://pastpapers.co"
        self.store_place = ""
        self.files_pools = []
        # self.office,self.grade,self.year,self.month,self.component = '','','','',''
        self.exam_office = {"cie":["A-Level","IGCSE","O-Level","Pre-U"], "aqa":["A-Level",'GCSE'], "cces":["GCE-A-Level","GCSE"], "ocr":["A-Level",'GCSE']}
        self.home_choose = [['CIE: A-Level','/cie/?dir=A-Level'],['CIE: IGCSE','/cie/?dir=IGCSE'],['CIE: O-Level','/cie/?dir=O-Level'],['CIE: Pre-U','/cie/?dir=Pre-U'],
                    ['AQA: A-Level','/aqa/?dir=A-Level'],['AQA: IGCSE','/aqa/?dir=GCSE'],['CCEA: GCSE','/ccea/?dir=GCSE'],['CCEA: GCE-A-Level','/ccea/?dir=GCE-A-Level'],
                    ['OCR: A-Level','/ocr/?dir=A-Level'],['OCR: IGCSE','/ocr/?dir=GCSE']]
        self.current_display = sorted(self.home_choose)

    def dir_content(self,dir):
        """ Get content of dir; --> List[contents]"""
        current_url = self.domain_url+dir
        headers = {'User-Agent': ua.random}
        proxy = {"http": "127.0.0.1:7890","https": "127.0.0.1:7890"}     
        r = requests.get(current_url,headers)# ,proxies = proxy
        options = []
        soup = BeautifulSoup(r.text.replace('%2F','/').replace('%26','&').replace('%20',' '),'lxml')
        soup_find = soup.find_all(True, {"class":["item _blank pdf","item _blank PDF", "item dir"]})
        for i in soup_find:
            options.append([i.get_text().strip(),i['href']])
        if options!=[]:
            self.current_display = options
            return 1
        else: return 0
        del r


class WorkThread(QThread):
    progressBarValue = pyqtSignal(int)
    def __init__(self):
        super(WorkThread, self).__init__()
    def run(self):
        print("thread run..")
        start = time.time()
        self.finished = 0
        self.total_ = len(pa.files_pools)
        for i in pa.files_pools:
            file_name = i[0]
            file_path = pa.store_place+i[1].replace('view.php?id=','').replace(i[0],'')
            file_url = pa.domain_url+i[1]
            if not os.path.isdir(file_path):
                os.makedirs(file_path)
            else:
                if os.path.isfile(file_path+file_name):
                    print(file_name,'has downloaded previously!')
                    self.finished+=1
                    self.progressBarValue.emit(int(self.finished * 100 / self.total_ ))
                else:
                    headers = {'User-Agent': ua.random}
                    proxy = {"http": "127.0.0.1:7890","https": "127.0.0.1:7890"}  
                    with open(file_path+file_name,'wb') as f:
                        r = requests.get(file_url, headers)
                        f.write(r.content)
                    self.finished+=1
                    self.progressBarValue.emit(int(self.finished * 100 / self.total_ ))
            print("\r" + "[下载进度]：%s%.2f%%" % ( ">" * int(self.finished * 50 / self.total_), float(self.finished / self.total_ * 100)), end="")
        end = time.time() 
        print("\n" + "全部下载完成！用时%.2f秒" % (end - start))

        
if __name__ == '__main__':
    pa = Pastpaper()
    
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    act = actions()

    ui.choose_all.triggered.connect(act.tb_choose_all)
    ui.clean_all.triggered.connect(act.tb_clean_all)
    # ui.current_dir.clicked.connect(act.serach_clicked)
    ui.exam_office.clicked.connect(act.exam_office_clicked)
    ui.grade.clicked.connect(act.grade_clicked)
    ui.subject.clicked.connect(act.subject_clicked)
    ui.year.clicked.connect(act.year_clicked)
    ui.back.clicked.connect(act.back_clicked)
    ui.open.clicked.connect(act.open_clicked)
    ui.download.clicked.connect(act.download_clicked)
    ui.store_place.clicked.connect(act.store_place)

    sys.exit(app.exec_())