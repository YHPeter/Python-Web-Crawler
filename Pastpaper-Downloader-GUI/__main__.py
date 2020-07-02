# -*- coding: utf-8 -*-

from pastpaper import Pastpaper
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from functools import partial
import windows

class actions():
    def __init__(self):
        super(actions).__init__()
        self.info_model = QStandardItemModel()
        self.display_table(pa.current_display)
        
    def display_table(self,info):
        """"Display infomation in the table"""
        self.info_model.clear
        for row in range(len(info)):
            item_checked = QStandardItem()
            item_checked.setCheckState(Qt.Unchecked)
            item_checked.setCheckable(True)
            item_checked.isDropEnabled()
            self.info_model.setItem(row,1, item_checked)
            item = QStandardItem(info[row][0])
            self.info_model.setItem(row,0,item)
        ui.info.setModel(self.info_model)
        ui.info.setColumnWidth(1,1)
        ui.info.setColumnWidth(0,426)


    def table_item_clicked_open(self):
        """Return List of items checked"""
        print('checked open')


    def table_item_clicked_download(self):
        """Return List of items checked"""
        pass

    def tb_open_choose(self):
        pa.dir_content('sdf')
        self.display_table(pa.current_display)
    def tb_choose_reverse(self):
        pass
    def tb_choossae_all(self):
        # r = self.player_tabview.currentIndex().row()
        # item = self.player_model.index(r,0)
        for i in range(len(pa.current_display)):
            # if not self.info_model.index(i,0).isChecked():
            #     self.info_model.index(i,0).setCheckState(Qt.checked)
            
            print(self.table_item_clicked(ui.info))

        # self.connect(self.table, QtCore.SIGNAL("itemClicked(QTableWidgetItem*)"), self.table_item_clicked)
    def tb_choose_all(self):
        checked_list = []
        for i in range(ui.info.rowCount()):
            #print(self.tableWidget.rowCount())
            if ui.info.item(i, 1).isChecked():
                checked_list.append([i,1])
            elif ui.info.cellWidget(i, 2).isChecked():
                checked_list.append([i,2])
            else:
                pass
        print(checked_list)
                    
    def serach_clicked(self):
        pass
    def exam_office_clicked(self):
        pass
    def grade_clicked(self):
        print('grade_clicked')
        pass
    def subject_clicked(self):
        pass
    def year_clicked(self):
        pass
    def month_clicked(self):
        pass
    def component_clicked(self):
        print('component')
        pass
    def download_clicked(self):
        reply = QMessageBox.question(self, '确认', '确定下载?',QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            pass
    def store_place(self):
        pass


    
if __name__ == '__main__':
    pa = Pastpaper()
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = windows.Ui_MainWindow()
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
