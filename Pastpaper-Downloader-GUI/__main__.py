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


def display_table(info):
    """"Display infomation in the table"""
    ui.model.clear
    for row in range(len(info)):
        item_checked = QStandardItem()
        item_checked.setCheckState(Qt.Unchecked)
        item_checked.setCheckable(True)
        item_checked.isDropEnabled()
        ui.model.setItem(row,1, item_checked)
        item = QStandardItem(info[row][0])
        ui.model.setItem(row,0,item)
    ui.info.setModel(ui.model)
    ui.info.setColumnWidth(1,1)
    ui.info.setColumnWidth(0,426)
    

def current_table():
    ui.start_search.clicked.connect(pa.dir_content)
    print(pa.current_display)
    display_table(pa.current_display)

def table_item_clicked_open():
    """Return List of items checked"""
    print('checked open')


def table_item_clicked_download():
    """Return List of items checked"""
    pass

def bt_init():
    ui.toolButton.setAutoRaise(True)

    menu = QMenu()
    ui.toolButton.open_choose = QAction('打开')
    ui.toolButton.choose_reverse = QAction('反选')
    ui.toolButton.choose_all = QAction('全选')

    menu.addAction(ui.toolButton.open_choose)
    menu.addSeparator()
    menu.addAction(ui.toolButton.choose_reverse)
    menu.addAction(ui.toolButton.choose_all)
    ui.toolButton.setMenu(menu)

    ui.toolButton.open_choose.triggered.connect(tb_on_click)
    ui.toolButton.choose_reverse.triggered.connect(tb_on_click)
    ui.toolButton.choose_all.triggered.connect(tb_on_click)

def tb_on_click():
    if ui.toolButton.sender() == ui.toolButton.open_choose:
        tb_open_choose()
    elif ui.toolButton.sender() == ui.toolButton.choose_reverse:
        tb_choose_reverse()
    elif ui.toolButton.sender() == ui.toolButton.choose_all:
        tb_choose_all()

def tb_open_choose():
    pass
def tb_choose_reverse():
    pass
def tb_choose_all():
    pass
def serach_clicked():
    pa.dir_content('sdf')
    display_table(pa.current_display)
if __name__ == '__main__':
    pa = Pastpaper()
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = windows.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    # bt_init()
    display_table(pa.current_display)

    ui.start_search.clicked.connect(serach_clicked)
    # ui.start_search.clicked.connect(pa.dir_content(1))
    # display_table(pa.current_display)
    # print(pa.current_display)


    sys.exit(app.exec_())
