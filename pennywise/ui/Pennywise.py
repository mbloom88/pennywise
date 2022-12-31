# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Pennywise.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Pennywise(object):
    def setupUi(self, Pennywise):
        Pennywise.setObjectName("Pennywise")
        Pennywise.resize(1131, 783)
        self.centralwidget = QtWidgets.QWidget(Pennywise)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.expense_table = QtWidgets.QTableWidget(self.centralwidget)
        self.expense_table.setObjectName("expense_table")
        self.expense_table.setColumnCount(4)
        self.expense_table.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.expense_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.expense_table.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.expense_table.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.expense_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.expense_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.expense_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.expense_table.setHorizontalHeaderItem(3, item)
        self.horizontalLayout.addWidget(self.expense_table)
        self.verticalLayout.addLayout(self.horizontalLayout)
        Pennywise.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Pennywise)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1131, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        Pennywise.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Pennywise)
        self.statusbar.setObjectName("statusbar")
        Pennywise.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(Pennywise)
        QtCore.QMetaObject.connectSlotsByName(Pennywise)

    def retranslateUi(self, Pennywise):
        _translate = QtCore.QCoreApplication.translate
        Pennywise.setWindowTitle(_translate("Pennywise", "Pennywise"))
        self.pushButton.setText(_translate("Pennywise", "Add New Expense"))
        item = self.expense_table.verticalHeaderItem(0)
        item.setText(_translate("Pennywise", "1"))
        item = self.expense_table.verticalHeaderItem(1)
        item.setText(_translate("Pennywise", "2"))
        item = self.expense_table.verticalHeaderItem(2)
        item.setText(_translate("Pennywise", "3"))
        item = self.expense_table.horizontalHeaderItem(0)
        item.setText(_translate("Pennywise", "Frequency"))
        item = self.expense_table.horizontalHeaderItem(1)
        item.setText(_translate("Pennywise", "Name"))
        item = self.expense_table.horizontalHeaderItem(2)
        item.setText(_translate("Pennywise", "Amount ($)"))
        item = self.expense_table.horizontalHeaderItem(3)
        item.setText(_translate("Pennywise", "Comments"))
        self.menuFile.setTitle(_translate("Pennywise", "File"))
        self.menuHelp.setTitle(_translate("Pennywise", "Help"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Pennywise = QtWidgets.QMainWindow()
    ui = Ui_Pennywise()
    ui.setupUi(Pennywise)
    Pennywise.show()
    sys.exit(app.exec_())
