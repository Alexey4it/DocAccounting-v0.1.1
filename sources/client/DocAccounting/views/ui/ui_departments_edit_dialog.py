# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DocAccounting/views/ui/DepartmentsEditDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DepartmentsEditDialog(object):
    def setupUi(self, DepartmentsEditDialog):
        DepartmentsEditDialog.setObjectName("DepartmentsEditDialog")
        DepartmentsEditDialog.resize(658, 348)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        DepartmentsEditDialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DepartmentsEditDialog.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(DepartmentsEditDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(DepartmentsEditDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.titleEdit = QtWidgets.QLineEdit(DepartmentsEditDialog)
        self.titleEdit.setObjectName("titleEdit")
        self.gridLayout.addWidget(self.titleEdit, 1, 1, 1, 1)
        self.cancelButton = QtWidgets.QPushButton(DepartmentsEditDialog)
        self.cancelButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cancelButton.setObjectName("cancelButton")
        self.gridLayout.addWidget(self.cancelButton, 2, 3, 1, 1)
        self.codeEdit = QtWidgets.QLineEdit(DepartmentsEditDialog)
        self.codeEdit.setObjectName("codeEdit")
        self.gridLayout.addWidget(self.codeEdit, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(DepartmentsEditDialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(DepartmentsEditDialog)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.okButton = QtWidgets.QPushButton(DepartmentsEditDialog)
        self.okButton.setObjectName("okButton")
        self.gridLayout.addWidget(self.okButton, 2, 2, 1, 1)

        self.retranslateUi(DepartmentsEditDialog)
        QtCore.QMetaObject.connectSlotsByName(DepartmentsEditDialog)

    def retranslateUi(self, DepartmentsEditDialog):
        _translate = QtCore.QCoreApplication.translate
        DepartmentsEditDialog.setWindowTitle(_translate("DepartmentsEditDialog", "??????????"))
        self.label_2.setText(_translate("DepartmentsEditDialog", "??????"))
        self.cancelButton.setText(_translate("DepartmentsEditDialog", "????????????"))
        self.label_3.setText(_translate("DepartmentsEditDialog", "????????????????????????"))
        self.okButton.setText(_translate("DepartmentsEditDialog", "OK"))
import res_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DepartmentsEditDialog = QtWidgets.QWidget()
    ui = Ui_DepartmentsEditDialog()
    ui.setupUi(DepartmentsEditDialog)
    DepartmentsEditDialog.show()
    sys.exit(app.exec_())
