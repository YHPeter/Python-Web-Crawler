    # -*- utf-8 -*-
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import re,requests,os,sys,queue,time,subprocess
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import threading
ua = UserAgent()


all_header_checkbox = []
class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(617, 931)
        MainWindow.setMinimumSize(QtCore.QSize(617, 931))
        MainWindow.setMaximumSize(QtCore.QSize(617, 931))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.layoutWidget = QtWidgets.QWidget(MainWindow)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 40, 581, 871))
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
        font.setFamily("Microsoft YaHei self")
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
        self.lineEdit.setReadOnly(True)
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
        self.info = QTableWidget(self.layoutWidget)
        self.info.setEnabled(True)
        self.info.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.info.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)#纵向滚轮
        self.info.setObjectName("info")     
        self.info.horizontalHeader().setVisible(False)#横向表头无
        self.info.verticalHeader().setVisible(False)#纵向表头无
        self.info.horizontalHeader().setStretchLastSection(True)
        self.info.setItem(0,0, QTableWidgetItem("Name")) 
        self.horizontalLayout.addWidget(self.info)
        self.formLayout.setLayout(3, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout)
        self.download = QtWidgets.QPushButton(self.layoutWidget)
        self.download.setObjectName("download")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.download)
        self.store_place_bt = QtWidgets.QPushButton(self.layoutWidget)
        self.store_place_bt.setObjectName("store_place_bt")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.store_place_bt)
        self.retranslateself(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.domain_url = "https://pastpapers.co"
        self.store_place = ""
        self.files_pools = []
        self.exam_office_dic = {"cie":["A-Level","IGCSE","O-Level","Pre-U"], "aqa":["A-Level",'GCSE'], "cces":["GCE-A-Level","GCSE"], "ocr":["A-Level",'GCSE']}
        self.home_choose = [['CIE: A-Level','/cie/?dir=A-Level'],['CIE: IGCSE','/cie/?dir=IGCSE'],['CIE: O-Level','/cie/?dir=O-Level'],['CIE: Pre-U','/cie/?dir=Pre-U'],
                    ['AQA: A-Level','/aqa/?dir=A-Level'],['AQA: IGCSE','/aqa/?dir=GCSE'],['CCEA: GCSE','/ccea/?dir=GCSE'],['CCEA: GCE-A-Level','/ccea/?dir=GCE-A-Level'],
                    ['OCR: A-Level','/ocr/?dir=A-Level'],['OCR: IGCSE','/ocr/?dir=GCSE']]
        self.url_visited = {'Home':self.home_choose}
        self.proxy = None#{"http": "127.0.0.1:7890","https": "127.0.0.1:7890"} 
        self.current_display = sorted(self.home_choose)
        self.display()
        self.flag_thread = True
        self.current = 'Home'
        self.lineEdit.setText(self.current)
        self.choose_all.triggered.connect(self.tb_choose_all)
        self.clean_all.triggered.connect(self.tb_clean_all)
        self.choose_inverse.triggered.connect(self.tb_choose_inverse)
        self.back.clicked.connect(self.back_clicked)
        self.open.clicked.connect(self.open_clicked)
        self.download.clicked.connect(self.download_clicked)
        self.store_place_bt.clicked.connect(self.store_place_clicked)
        # menubar setting
        '''
        menu:
            File
                open in browser
                opne in local
            System
                setting
                    proxy
                    thread
                exit
        '''
        menubar = self.menuBar()
        menu1 = menubar.addMenu("系统")
        menu1_sub1 = QAction( "退出软件", self)
        menu1_sub1.setShortcut("Ctrl+Q")
        menu1_sub1.setStatusTip("Exit Application")
        menu1_sub1.triggered.connect(self.exit)
        menu1.addActions([menu1_sub1])

        menu2 = menubar.addMenu("文件")
        menu2_sub1 = QAction("浏览器中打开",self)
        menu2_sub2 = QAction("默认程序打开",self)
        menu2_sub1.setStatusTip("在线预览文件")
        menu2_sub2.setStatusTip("保存文件后预览")
        menu2_sub1.setShortcut("Ctrl+O")
        menu2_sub2.setShortcut("Ctrl+S")
        menu2_sub1.triggered.connect(self.preview_browser_clicked)
        menu2_sub2.triggered.connect(self.preview_local_clicked)
        menu2.addActions([menu2_sub1,menu2_sub2])

        # Hotkey
        QShortcut(QKeySequence("Ctrl+D"), self, self.download_clicked)
        QShortcut(QKeySequence("Ctrl+H"), self, self.tips)
        
        self.tips()
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2.5)

    def tips(self):
        # Usage Tips
        tips = "<h2>快捷键介绍：</h2><h3>Ctrl+A 全选(All)<br>Ctrl+ I 反选(Inverse)<br>Ctrl+W 全不选<br>Ctrl+D 下载所选文件文件夹(Download)<br>Ctrl+O 浏览器中打开(Open Online)<br>Ctrl+S 默认程序中打开<br>Ctrl+C 终止多文件下载进程<br>Ctrl+H 帮助<br>Ctrl+Q 退出程序(Quit)<br>打开时不要过快点击，有1s延迟</h3>"
        QMessageBox.question(None,'帮助', tips, QMessageBox.Ok)

    def retranslateself(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pastpaper Downloader"))
        self.label.setText(_translate("MainWindow", "Pastpaper 下载器"))
        self.back.setText(_translate("MainWindow", "上一级文件夹"))
        self.open.setText(_translate("MainWindow", "打开文件夹"))
        self.current_dir.setText(_translate("MainWindow", "当前文件夹"))
        self.lineEdit.setText(_translate("MainWindow", "Search component"))
        self.toolButton.setText(_translate("MainWindow", "多选功能"))
        self.download.setText(_translate("MainWindow", "下载所选文件 Ctrl+D"))
        self.store_place_bt.setText(_translate("MainWindow", "文件储存位置"))
        menu = QMenu()
        self.choose_inverse = QAction(QIcon("menu.ico"),'反选',menu)
        self.choose_all = QAction(QIcon("menu.ico"),'全选',menu)
        self.clean_all = QAction(QIcon("menu.ico"),'全不选',menu)
        self.choose_all.setShortcut("Ctrl+A")
        self.choose_inverse.setShortcut("Ctrl+I")
        self.clean_all.setShortcut("Ctrl+W")
        menu.addActions([self.choose_inverse,self.choose_all,self.clean_all])
        self.toolButton.setMenu(menu)
        self.toolButton.setPopupMode(QToolButton.MenuButtonPopup)

    def display(self):
        global all_header_checkbox
        all_header_checkbox = []
        self.info.setRowCount(len(self.current_display))
        self.info.setColumnCount(3)
        for row in range(len(self.current_display)):
            font = QtGui.QFont()
            font.setPointSize(12)
            item_text = QTableWidgetItem(self.current_display[row][0])
            item_text.setFont(font)
            item_checked = QTableWidgetItem()
            item_checked.setCheckState(Qt.Unchecked)
            all_header_checkbox.append(item_checked)
            self.info.setItem(row,0,item_text)
            self.info.setItem(row,1,item_checked)
            if self.current_display[row][0][-3:]=='pdf' or self.current_display[row][0][-3:]=='PDF':
                item_download = QPushButton()
                item_download.clicked.connect(self.item_download_clicked)
                item_download.setShortcut("Ctrl+D")
                item_download.setText('下载')
                item_download.setStyleSheet(''' text-align : center;
                                        background-color : NavajoWhite;
                                        height : 50px;
                                        border-style: outset;
                                        font : 20px  ''')# DarkSeaGreen,LightCoral,NavajoWhite
                self.info.setCellWidget(row,2, item_download)
            else:
                item_open = QPushButton()
                item_open.clicked.connect(self.item_open_clicked)
                item_open.setText('打开')
                item_open.setStyleSheet(''' text-align : center;
                                        background-color : DarkSeaGreen;
                                        height : 50px;
                                        border-style: outset;
                                        font : 20px  ''')# DarkSeaGreen,LightCoral,NavajoWhite
                self.info.setCellWidget(row,2, item_open)
        self.info.setColumnWidth(1,0)
        self.info.setColumnWidth(0,456)
        self.info.setColumnWidth(2,40)
        
    def item_open_clicked(self):
        button = self.sender()
        if button:
            row = self.info.indexAt(button.pos()).row()
            self.update_current_page(self.current_display[row][1])

    def item_download_clicked(self):
        button = self.sender()
        if button:
            self.download.setEnabled(False)
            while self.store_place=='':
                self.store_place_clicked()
            row = self.info.indexAt(button.pos()).row()
            i = self.current_display[row]
            file_name = i[0]
            file_path = self.store_place+i[1].replace('view.php?id=','').replace(i[0],'')
            file_url = self.domain_url+i[1].replace('view.php?id=','')
            reply = QMessageBox.question(None,'确认', '确定下载?', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                print(file_path+file_name)
                if os.path.isfile(file_path+file_name):
                    print(file_name,'has downloaded previously!')
                    QMessageBox.question(None,'提示', '该文件已经下载过！Ctrl+S 可立即打开', QMessageBox.Ok)
                    return None
                if not os.path.isdir(file_path):
                    os.makedirs(file_path)
                self.download.setEnabled(False)
                self.store_place_bt.setEnable(False)
                self.download.setText("正在下载...")                
                self.workthread = SingleDownload(file_name,file_path,file_url)
                self.workthread.progressBarValue.connect(self.single_progressBar.setValue)#act.set_progressbar_value)
                self.workthread.start()
        self.download.setEnabled(True)
        self.download.setText("下载所选文件 Ctrl+D")
        self.store_place_bt.setEnable(True)

    def update_current_page(self,cur):
        options = self.dir_content(cur)
        if options:
            self.current_display = options
            self.current = cur
            self.display()
            self.lineEdit.setText(self.current.replace('?dir=',''))
        else: QMessageBox.question(None,'注意','此目录下没有文件！', QMessageBox.Ok)

    def open_clicked(self):
        total,open = 0,0
        for i in range(len(all_header_checkbox)):
            if all_header_checkbox[i].checkState():
                if not self.current_display[0][0][-3:]=='pdf' or self.current_display[0][0][-3:]=='PDF':
                    total,open = total+1,i
                else:
                    QMessageBox.question(None,'注意','PDF文件无法打开哦！', QMessageBox.Ok)
        if total==1:
            self.update_current_page(self.current_display[open][1])
        elif total>1:
            reply = QMessageBox.question(None,'注意','只能选择一个文件夹打开,是否清除已选？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply==QMessageBox.Yes: self.tb_clean_all()
        elif total==0:
            QMessageBox.question(None,'注意','需要选择一个文件夹打开！', QMessageBox.Ok)

    def back_clicked(self):
        home_urls = ['/cie/?dir=A-Level','/cie/?dir=IGCSE','/cie/?dir=O-Level',
        '/cie/?dir=Pre-U','/aqa/?dir=A-Level','/aqa/?dir=GCSE','/ccea/?dir=GCSE',
        '/ccea/?dir=GCE-A-Level','/ocr/?dir=A-Level','/ocr/?dir=GCSE']
        if self.current=='Home': return None
        if self.current in home_urls:
            self.current_display = sorted(self.home_choose)
            self.display()
            self.current = 'Home'
            self.lineEdit.setText(self.current)
        else:
            self.current = '/'.join(self.current.split('/')[:-1])
            options = self.dir_content(self.current)
            if options:
                self.current_display = options
            self.lineEdit.setText(self.current.replace('?dir=',''))
            self.display()
            
    def tb_choose_inverse(self):
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
        self.files_pools==[]
        selected = []
        while self.store_place=='':
            self.store_place_clicked()
        for i in range(len(self.current_display)):
            if all_header_checkbox[i].checkState():
                selected.append(self.current_display[i])
        if len(selected)==0:
            QMessageBox.question(None,'提醒', '请选择下载文件', QMessageBox.Ok)
            return None
        if QMessageBox.question(None,'确认', '确定下载?', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)==QMessageBox.No:
            return None
        if self.current_display[-1][0][-3:]=='pdf' or self.current_display[-1][0][-3:]=='PDF':
            if len(selected)==1:
                i = selected[0]
                file_name = i[0]
                file_path = self.store_place+i[1].replace('view.php?id=','').replace(i[0],'')
                file_url = self.domain_url+i[1].replace('view.php?id=','')
                print(file_path+file_name)
                if os.path.isfile(file_path+file_name):
                    print(file_name,'has downloaded previously!')
                    return None
                if not os.path.isdir(file_path):
                    os.makedirs(file_path)
                self.download.setText("正在下载...")                
                self.workthread = SingleDownload(file_name,file_path,file_url)
                self.workthread.progressBarValue.connect(self.single_progressBar.setValue)
                self.workthread.start()
            else:
                self.download_start(selected)
        else:
            if self.current == 'Home':
                QMessageBox.question(None,'警告', '不可以在主页批量下载，文件包含过多！', QMessageBox.Ok)
                return None
            self.mutifolder = MutiFolders(selected)
            self.mutifolder.start()
        
    def download_start(self,selected):
        if selected==[]: return None
        reply = QMessageBox.question(None,'确认', '确定下载?', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            if len(selected)>1000:
                MainWindow.download_files(self,selected[:300])
                MainWindow.download_files(self,selected[300:600])
                MainWindow.download_files(self,selected[600:900])
                MainWindow.download_files(self,selected[900:])
            else:
                MainWindow.download_files(self,selected)

    def store_place_clicked(self):
        self.store_place = QFileDialog.getExistingDirectory(None,'选择文件夹')
        self.store_place_bt.setText(self.store_place)
    
    # menubar clicked function
    def preview_browser_clicked(self):
        selected = []
        for i in range(len(self.current_display)):
            if all_header_checkbox[i].checkState():
                selected.append(self.current_display[i])
        if len(selected)==0:
            QDesktopServices.openUrl(QUrl(self.domain_url+self.current[1].replace('view.php?id=','')))
        elif len(selected)<=10: 
            for i in selected:
                QDesktopServices.openUrl(QUrl(self.domain_url+i[1].replace('view.php?id=','')))
        else:
            QMessageBox.question(None,'提醒', '选择文件过多（不可超过10个），请重新选择！', QMessageBox.Ok)

    def preview_local_clicked(self):
        selected = []
        while self.store_place=='':
            self.store_place_clicked()
        for i in range(len(self.current_display)):
            if all_header_checkbox[i].checkState():
                selected.append(self.current_display[i])
        if len(selected)==0:
            path = self.store_place+self.current.replace('view.php?id=','').replace("?dir=",'')
            if self.current == 'Home': path = self.store_place
            if os.path.isdir(path):
                print('Opne:',path)
                subprocess.Popen('explorer ' + os.path.normpath(path))
        elif len(selected)<=10: 
            for i in selected:
                path = self.store_place+i[1].replace('view.php?id=','').replace("?dir=",'')
                if os.path.isdir(path):
                    print('Opne:',path)
                    subprocess.Popen('explorer ' + os.path.normpath(path))
                elif os.path.isfile(path):
                    print('Opne:',path)
                    subprocess.Popen(path,shell=True)
        else: QMessageBox.question(None,'提醒', '选择文件过多（不可超过10个），请重新选择！', QMessageBox.Ok)

    def exit(self):
        qApp.exit()

    def stop(self):
        self.flag_thread = False
        print('thread stop')
        QMessageBox.question(None,'提醒', '已取消下载！请等待三秒！', QMessageBox.Ok)
        time.sleep(3)
        self.flag_thread = True
        self.single_progressBar.setValue(0)
        self.store_place_bt.setEnabled(True)
        self.store_place_bt.setText(self.store_place)

    def dir_content(self,dir):
        """ Get content of dir; --> List[contents]"""
        if not self.flag_thread: return []
        if str(dir) in self.url_visited.keys():
            return self.url_visited[str(dir)]
        current_url = self.domain_url+dir
        headers = {'User-Agent': ua.random}
        try:
            r = requests.get(current_url,headers,proxies = self.proxy) 
            options = []
            soup = BeautifulSoup(r.text.replace('%2F','/').replace('%20',' '),'lxml')
            soup_find = soup.find_all(True, {"class":["item _blank pdf","item _blank PDF", "item dir"]})
            for i in soup_find:
                options.append([i.get_text().strip().replace('%26','&').replace('%2F','/').replace('%20',' '),i['href']])
                self.url_visited[str(dir)] = options
            del r
            return options
        except:
            print('dir_content error!')
            return []
        

class SingleDownload(QThread):
    progressBarValue = pyqtSignal(int)
    def __init__(self,file_name,file_path,file_url):
        QThread.__init__(self)
        self.url = file_url.replace('view.phh','')
        self.path = file_path+file_name
        self.name = file_name
    def run(self):
        print("SingleDownload run..")
        print("Downloading file:" + self.url)
        start = time.time()
        size = 0
        r = requests.get(self.url, stream=True)
        chunk_size = 10240
        content_size = int(r.headers['content-length'])
        if r.status_code == 200:
            print("[文件大小]:%.2f MB" % (content_size / chunk_size / 1024))
            with open(self.path, "wb") as file:
                for data in r.iter_content(chunk_size=chunk_size):
                    file.write(data)
                    size += len(data)
                    num = int(size / content_size * 100)
                    self.progressBarValue.emit(num)
                    print("\r" + "[下载进度]：%s%.2f%%" % (">" * int(size * 50 / content_size), float(size / content_size * 100)), end="")
                    mainWindow.store_place_bt.setText('正在下载：'+ file_name)
            end = time.time()
            mainWindow.store_place_bt.setText("全部下载完成！用时%.2f秒" % (end - start))
            print("\n" + "全部下载完成！用时%.2f秒" % (end - start))


class Signal(QObject):
    update_pb = pyqtSignal(int)

class DownloadThread(QRunnable):
    def __init__(self, count, files_pools):
        super().__init__()
        self.count = count
        self.signal = Signal()
        self.files_pools = files_pools
    def run(self):
        print("Thread run..")
        start = time.time()
        self.finished = 0
        self.total_ = len(self.files_pools)
        mainWindow.store_place_bt.setEnabled(False)
        for i in self.files_pools:
            if not mainWindow.flag_thread: break
            file_name = i[0]
            file_path = mainWindow.store_place+i[1].replace('view.php?id=','').replace(i[0],'')
            file_url = mainWindow.domain_url+i[1].replace('view.php?id=','').replace('?id=','')
            if not os.path.isdir(file_path):
                os.makedirs(file_path)
            if os.path.isfile(file_path+file_name):
                text = file_name+' has downloaded previously!'
                self.finished+=1
                self.signal.update_pb.emit(int(self.finished * 100 / self.total_ ))
            else:
                text = file_name + ' is downloading...'
                headers = {'User-Agent': ua.random}
                with open(file_path+file_name,'wb') as f:
                    res = requests.get(file_url, headers, proxies = mainWindow.proxy)
                    f.write(res.content)
                self.finished+=1
                self.signal.update_pb.emit(int(self.finished * 100 / self.total_ ))
            
            print("\r" + "[下载进度]：%s%.2f%%" % ( ">" * int(self.finished * 50 / self.total_), float(self.finished / self.total_ * 100)) + text, end="")
            mainWindow.store_place_bt.setText('正在下载：'+ file_path + file_name)
        end = time.time() 
        print("\n" + "全部下载完成！用时%.2f秒" % (end - start))
        mainWindow.store_place_bt.setText("全部下载完成！用时%.2f秒" % (end - start))
        mainWindow.store_place_bt.setText(mainWindow.store_place)
        mainWindow.setEnabled(True)



class MutiFolders(QThread):
    def __init__(self,selected):
        super(MutiFolders, self).__init__()
        self.selected = selected
        self.files_pools = []
    def run(self):
        mainWindow.store_place_bt.setEnabled(False)
        mainWindow.store_place_bt.setText('正在递归获取三层文件夹以内的PDF链接。。。')
        print("MutiFolders thread run..")
        for i in self.selected:
            if not mainWindow.flag_thread: break
            optionsi = mainWindow.dir_content(i[1])
            if optionsi==[] or optionsi[0][0][-3:]=='pdf' or optionsi[0][0][-3:]=='PDF':
                self.files_pools+=optionsi
                continue
            for j in optionsi:
                if not mainWindow.flag_thread: break
                optionsj = mainWindow.dir_content(j[1])
                if optionsj==[] or optionsj[0][0][-3:]=='pdf' or optionsj[0][0][-3:]=='PDF':
                    self.files_pools+=optionsj
                    continue
                for k in optionsj:
                    if not mainWindow.flag_thread: break
                    optionsk = mainWindow.dir_content(k[1])
                    if optionsk==[] or optionsk[0][0][-3:]=='pdf' or optionsk[0][0][-3:]=='PDF':
                        self.files_pools+=optionsk
        if mainWindow.flag_thread:
            mainWindow.store_place_bt.setText('共计%d个文件'%len(self.files_pools))
            print(self.files_pools)
            MainWindow.download_files(mainWindow,self.files_pools)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.count = 0
        self.pool = QThreadPool()
        self.pool.globalInstance()
        self.pool.setMaxThreadCount(10)
        QtWidgets.QShortcut("Ctrl+C", self, activated=self.stop)

    def download_files(self,files_pools):
        thread = DownloadThread(self.count, files_pools)
        self.count += 1
        thread.signal.update_pb.connect(self.single_progressBar.setValue)
        self.pool.start(thread)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())