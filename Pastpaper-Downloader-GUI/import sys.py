# # import sys
# # from PyQt5.QtCore import *
# # from PyQt5.QtWidgets import *
# # from PyQt5.QtGui import *

# # class Table(QWidget):
# #     def __init__(self,parent=None):
# #         super(Table, self).__init__(parent)
# #         #设置标题与初始大小
# #         self.setWindowTitle('QTableView表格复选框案例')
# #         self.resize(500,300)
# #         self.tableView=QTableView()
# #         self.model = QStandardItemModel(self.tableView)

# #         #设置数据层次结构，4行4列
# #         self.model=QStandardItemModel(4,4)
# #         t = QCheckBox(self)
# #         #设置水平方向四个头标签文本内容
# #         self.model.setHorizontalHeaderLabels(['状态','姓名','身份证','地址'])

# #         for row in range(4):
# #             for column in range(4):
# #                 item_checked = QStandardItem()
# #                 item_checked.setCheckState(Qt.Checked)
# #                 item_checked.setCheckable(True)
# #                 self.model.setItem(column,0, item_checked)
# #                 item=QStandardItem('row %s,column %s'%(row,column))
# #                 #设置每个位置的文本值
# #                 self.model.setItem(row,column,item)

# #         self.tableView.setModel(self.model)
# #         #设置布局
# #         layout=QVBoxLayout()
# #         layout.addWidget(self.tableView)
# #         self.setLayout(layout)

# # if __name__ == '__main__':
# #     app=QApplication(sys.argv)
# #     table=Table()
# #     table.show()
# #     sys.exit(app.exec_())
# from PyQt5.Qt import *
# import sys

# #0.创建一个APP
# app = QApplication(sys.argv)

# w = QWidget()
# w.setWindowTitle("QToolButton")
# w.resize(300,300)

# #创建菜单
# menu = QMenu()
# #创建子菜单
# sub_menu = QMenu(menu)
# sub_menu.setTitle("子菜单")
# sub_menu.setIcon(QIcon("menu.ico"))

# #在菜单中添加子菜单
# menu.addMenu(sub_menu)

# #创建action并添加到菜单中
# action = QAction(QIcon("menu.ico"),"行为",menu)
# menu.addAction(action)
# #响应action点击事件
# action.triggered.connect(lambda:print("点击了 action"))


# #创建一个 QToolButton
# tb = QToolButton(w)
# tb.setIcon(QIcon("menu.ico"))
# tb.setAutoRaise(True)

# #添加菜单 到 QToolBool
# tb.setMenu(menu)

# #设置菜单模式
# tb.setPopupMode(QToolButton.MenuButtonPopup)

# w.show()

# sys.exit(app.exec_())
import numpy
from PyQt5 import QtCore, QtWidgets, QtGui
Qt = QtCore.Qt


class NumpyModel(QtCore.QAbstractTableModel):
    def __init__(self, narray, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self._array = narray.point
        self.test = narray.enabled
        self.header_icon = None
        self.setHeaderIcon()

    def rowCount(self, _parent=None):
        return self._array.shape[0]

    def columnCount(self, _parent=None):
        return self._array.shape[1] + 1

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None
        if (index.column() == 3):
            value = ''
        else:
            value = QtCore.QVariant(
                "%.5f" % self._array[index.row(), index.column()])
        if role == QtCore.Qt.EditRole:
            return value
        elif role == QtCore.Qt.DisplayRole:
            return value
        elif role == QtCore.Qt.CheckStateRole:
            if index.column() == 3:
                if self.test[index.row()]:
                    return QtCore.Qt.Checked
                else:
                    return QtCore.Qt.Unchecked
        elif role == Qt.TextAlignmentRole:
            return Qt.AlignCenter

        return QtCore.QVariant()

    def setData(self, index, value, role=Qt.EditRole):
        if not index.isValid():
            return False
        if role == Qt.CheckStateRole and index.column() == 3:
            if value == Qt.Checked:
                self.test[index.row()] = True
            else:
                self.test[index.row()] = False
            self.setHeaderIcon()

        elif role == Qt.EditRole and index.column() != 3:
            row = index.row()
            col = index.column()
            if value.isdigit():
                self._array[row, col] = value
    
        return True

    def flags(self, index):
        if not index.isValid():
            return None

        if index.column() == 3:
            return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsUserCheckable
        else:
            return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable

    def headerData(self, index, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DecorationRole:
            if index == 3:
                return QtCore.QVariant(QtGui.QPixmap(self.header_icon).scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            if index != 3:
                return QtCore.QVariant(index+1)

        return QtCore.QVariant()

    def toggleCheckState(self, index):
        if index == 3:
            if numpy.all(self.test == False):
                self.test.fill(True)
            else:
                self.test.fill(False)
            
            topLeft =self.index(0, 3)
            bottomRight = self.index(self.rowCount(), 3)
            self.dataChanged.emit(topLeft, bottomRight)
            self.setHeaderIcon()

    def setHeaderIcon(self):
        if numpy.all(self.test == True):
            self.header_icon = 'checked.png'
        elif numpy.all(self.test == False):
            self.header_icon = 'unchecked.png'
        else:
            self.header_icon = 'intermediate.png'
        self.headerDataChanged.emit(Qt.Horizontal, 3, 3)

if __name__ == "__main__":
    a = QtWidgets.QApplication([])
    w = QtWidgets.QTableView()

    d = numpy.rec.array([([1., 2., 3.], True), ([4., 5., 6.], False), ([7., 8., 9.], True)],
                        dtype=[('point', 'f4', 3), ('enabled', '?')])
    m = NumpyModel(d)
    w.setModel(m)
    w.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
    w.setAlternatingRowColors(True)
    w.verticalHeader().setVisible(False)
    w.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
    w.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Fixed)
    w.horizontalHeader().setMinimumSectionSize(40)
    w.horizontalHeader().setDefaultSectionSize(40)

    header = w.horizontalHeader()
    header.sectionPressed.connect(m.toggleCheckState)
    w.show()
    a.exec_()