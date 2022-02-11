# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DocAccounting/views/ui/EmployeesDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EmployeesDialog(object):
    def setupUi(self, EmployeesDialog):
        EmployeesDialog.setObjectName("EmployeesDialog")
        EmployeesDialog.resize(658, 348)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        EmployeesDialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        EmployeesDialog.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(EmployeesDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.delButton = QtWidgets.QPushButton(EmployeesDialog)
        self.delButton.setObjectName("delButton")
        self.gridLayout.addWidget(self.delButton, 1, 2, 1, 1)
        self.cancelButton = QtWidgets.QPushButton(EmployeesDialog)
        self.cancelButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cancelButton.setObjectName("cancelButton")
        self.gridLayout.addWidget(self.cancelButton, 1, 4, 1, 1)
        self.addButton = QtWidgets.QPushButton(EmployeesDialog)
        self.addButton.setObjectName("addButton")
        self.gridLayout.addWidget(self.addButton, 1, 1, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(EmployeesDialog)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setItem(0, 0, item)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 5)
        self.label = QtWidgets.QLabel(EmployeesDialog)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.updateButton = QtWidgets.QPushButton(EmployeesDialog)
        self.updateButton.setObjectName("updateButton")
        self.gridLayout.addWidget(self.updateButton, 1, 3, 1, 1)

        self.retranslateUi(EmployeesDialog)
        QtCore.QMetaObject.connectSlotsByName(EmployeesDialog)

    def retranslateUi(self, EmployeesDialog):
        _translate = QtCore.QCoreApplication.translate
        EmployeesDialog.setWindowTitle(_translate("EmployeesDialog", "Сотрудники"))
        self.delButton.setText(_translate("EmployeesDialog", "Удалить"))
        self.cancelButton.setText(_translate("EmployeesDialog", "Отмена"))
        self.addButton.setText(_translate("EmployeesDialog", "Добавить"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("EmployeesDialog", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("EmployeesDialog", "Код"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("EmployeesDialog", "Должность"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("EmployeesDialog", "Отдел"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("EmployeesDialog", "ФИО"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("EmployeesDialog", "Email"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("EmployeesDialog", "Логин"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("EmployeesDialog", "Пароль"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.updateButton.setText(_translate("EmployeesDialog", "Обновить"))
import res_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EmployeesDialog = QtWidgets.QWidget()
    ui = Ui_EmployeesDialog()
    ui.setupUi(EmployeesDialog)
    EmployeesDialog.show()
    sys.exit(app.exec_())
