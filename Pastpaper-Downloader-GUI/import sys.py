import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Table(QWidget):
    def __init__(self,parent=None):
        super(Table, self).__init__(parent)
        #设置标题与初始大小
        self.setWindowTitle('QTableView表格复选框案例')
        self.resize(500,300)
        self.tableView=QTableView()
        self.model = QStandardItemModel(self.tableView)

        #设置数据层次结构，4行4列
        self.model=QStandardItemModel(4,4)
        t = QCheckBox(self)
        #设置水平方向四个头标签文本内容
        self.model.setHorizontalHeaderLabels(['状态','姓名','身份证','地址'])

        for row in range(4):
            for column in range(4):
                item_checked = QStandardItem()
                item_checked.setCheckState(Qt.Checked)
                item_checked.setCheckable(True)
                self.model.setItem(column,0, item_checked)
                item=QStandardItem('row %s,column %s'%(row,column))
                #设置每个位置的文本值
                self.model.setItem(row,column,item)

        self.tableView.setModel(self.model)
        #设置布局
        layout=QVBoxLayout()
        layout.addWidget(self.tableView)
        self.setLayout(layout)

if __name__ == '__main__':
    app=QApplication(sys.argv)
    table=Table()
    table.show()
    sys.exit(app.exec_())
