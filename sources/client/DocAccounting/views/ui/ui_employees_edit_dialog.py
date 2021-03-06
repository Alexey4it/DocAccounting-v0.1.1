# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DocAccounting/views/ui/EmployeesEditDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EmployeesEditDialog(object):
    def setupUi(self, EmployeesEditDialog):
        EmployeesEditDialog.setObjectName("EmployeesEditDialog")
        EmployeesEditDialog.resize(658, 348)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        EmployeesEditDialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        EmployeesEditDialog.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(EmployeesEditDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.allnamesEdit = QtWidgets.QLineEdit(EmployeesEditDialog)
        self.allnamesEdit.setObjectName("allnamesEdit")
        self.gridLayout.addWidget(self.allnamesEdit, 3, 2, 1, 1)
        self.codeEdit = QtWidgets.QLineEdit(EmployeesEditDialog)
        self.codeEdit.setObjectName("codeEdit")
        self.gridLayout.addWidget(self.codeEdit, 0, 2, 1, 1)
        self.loginEdit = QtWidgets.QLineEdit(EmployeesEditDialog)
        self.loginEdit.setObjectName("loginEdit")
        self.gridLayout.addWidget(self.loginEdit, 5, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(EmployeesEditDialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.okButton = QtWidgets.QPushButton(EmployeesEditDialog)
        self.okButton.setObjectName("okButton")
        self.gridLayout.addWidget(self.okButton, 7, 3, 1, 1)
        self.label = QtWidgets.QLabel(EmployeesEditDialog)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 7, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(EmployeesEditDialog)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(EmployeesEditDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.passwordEdit = QtWidgets.QLineEdit(EmployeesEditDialog)
        self.passwordEdit.setObjectName("passwordEdit")
        self.gridLayout.addWidget(self.passwordEdit, 6, 2, 1, 1)
        self.emailEdit = QtWidgets.QLineEdit(EmployeesEditDialog)
        self.emailEdit.setObjectName("emailEdit")
        self.gridLayout.addWidget(self.emailEdit, 4, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(EmployeesEditDialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.cancelButton = QtWidgets.QPushButton(EmployeesEditDialog)
        self.cancelButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cancelButton.setObjectName("cancelButton")
        self.gridLayout.addWidget(self.cancelButton, 7, 4, 1, 1)
        self.label_5 = QtWidgets.QLabel(EmployeesEditDialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(EmployeesEditDialog)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(EmployeesEditDialog)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 0, 1, 1)
        self.positions_codeComboBox = QtWidgets.QComboBox(EmployeesEditDialog)
        self.positions_codeComboBox.setObjectName("positions_codeComboBox")
        self.gridLayout.addWidget(self.positions_codeComboBox, 1, 2, 1, 1)
        self.departments_codeComboBox = QtWidgets.QComboBox(EmployeesEditDialog)
        self.departments_codeComboBox.setObjectName("departments_codeComboBox")
        self.gridLayout.addWidget(self.departments_codeComboBox, 2, 2, 1, 1)

        self.retranslateUi(EmployeesEditDialog)
        QtCore.QMetaObject.connectSlotsByName(EmployeesEditDialog)

    def retranslateUi(self, EmployeesEditDialog):
        _translate = QtCore.QCoreApplication.translate
        EmployeesEditDialog.setWindowTitle(_translate("EmployeesEditDialog", "????????????????????"))
        self.label_3.setText(_translate("EmployeesEditDialog", "??????"))
        self.okButton.setText(_translate("EmployeesEditDialog", "OK"))
        self.label_6.setText(_translate("EmployeesEditDialog", "????????????"))
        self.label_2.setText(_translate("EmployeesEditDialog", "??????"))
        self.label_4.setText(_translate("EmployeesEditDialog", "Email"))
        self.cancelButton.setText(_translate("EmployeesEditDialog", "????????????"))
        self.label_5.setText(_translate("EmployeesEditDialog", "??????????"))
        self.label_7.setText(_translate("EmployeesEditDialog", "??????????????????"))
        self.label_8.setText(_translate("EmployeesEditDialog", "??????????"))
import res_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EmployeesEditDialog = QtWidgets.QWidget()
    ui = Ui_EmployeesEditDialog()
    ui.setupUi(EmployeesEditDialog)
    EmployeesEditDialog.show()
    sys.exit(app.exec_())
