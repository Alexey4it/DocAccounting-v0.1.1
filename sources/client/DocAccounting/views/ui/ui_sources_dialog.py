# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DocAccounting/views/ui/SourcesDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SourcesDialog(object):
    def setupUi(self, SourcesDialog):
        SourcesDialog.setObjectName("SourcesDialog")
        SourcesDialog.resize(658, 348)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        SourcesDialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SourcesDialog.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(SourcesDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(SourcesDialog)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        item.setFont(font)
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
        self.tableWidget.setItem(0, 0, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(160)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(62)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(37)
        self.tableWidget.verticalHeader().setMinimumSectionSize(32)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 5)
        self.delButton = QtWidgets.QPushButton(SourcesDialog)
        self.delButton.setObjectName("delButton")
        self.gridLayout.addWidget(self.delButton, 1, 2, 1, 1)
        self.label = QtWidgets.QLabel(SourcesDialog)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.addButton = QtWidgets.QPushButton(SourcesDialog)
        self.addButton.setObjectName("addButton")
        self.gridLayout.addWidget(self.addButton, 1, 1, 1, 1)
        self.cancelButton = QtWidgets.QPushButton(SourcesDialog)
        self.cancelButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cancelButton.setObjectName("cancelButton")
        self.gridLayout.addWidget(self.cancelButton, 1, 4, 1, 1)
        self.updateButton = QtWidgets.QPushButton(SourcesDialog)
        self.updateButton.setObjectName("updateButton")
        self.gridLayout.addWidget(self.updateButton, 1, 3, 1, 1)

        self.retranslateUi(SourcesDialog)
        QtCore.QMetaObject.connectSlotsByName(SourcesDialog)

    def retranslateUi(self, SourcesDialog):
        _translate = QtCore.QCoreApplication.translate
        SourcesDialog.setWindowTitle(_translate("SourcesDialog", "??????????????????"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("SourcesDialog", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("SourcesDialog", "??????"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("SourcesDialog", "????????????????????????"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.delButton.setText(_translate("SourcesDialog", "??????????????"))
        self.addButton.setText(_translate("SourcesDialog", "????????????????"))
        self.cancelButton.setText(_translate("SourcesDialog", "????????????"))
        self.updateButton.setText(_translate("SourcesDialog", "????????????????"))
import res_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SourcesDialog = QtWidgets.QWidget()
    ui = Ui_SourcesDialog()
    ui.setupUi(SourcesDialog)
    SourcesDialog.show()
    sys.exit(app.exec_())
