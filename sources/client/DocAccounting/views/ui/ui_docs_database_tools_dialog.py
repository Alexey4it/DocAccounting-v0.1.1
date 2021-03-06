# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DocAccounting/views/ui/DatabaseToolsDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DatabaseToolsDialog(object):
    def setupUi(self, DatabaseToolsDialog):
        DatabaseToolsDialog.setObjectName("DatabaseToolsDialog")
        DatabaseToolsDialog.resize(652, 374)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        DatabaseToolsDialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DatabaseToolsDialog.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(DatabaseToolsDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(DatabaseToolsDialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 1, 1, 1)
        self.dialectEdit = QtWidgets.QLineEdit(DatabaseToolsDialog)
        self.dialectEdit.setObjectName("dialectEdit")
        self.gridLayout.addWidget(self.dialectEdit, 0, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(DatabaseToolsDialog)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 4, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(DatabaseToolsDialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.userNameEdit = QtWidgets.QLineEdit(DatabaseToolsDialog)
        self.userNameEdit.setObjectName("userNameEdit")
        self.gridLayout.addWidget(self.userNameEdit, 1, 2, 1, 1)
        self.saveButton = QtWidgets.QPushButton(DatabaseToolsDialog)
        self.saveButton.setObjectName("saveButton")
        self.gridLayout.addWidget(self.saveButton, 8, 1, 1, 1)
        self.testConnectionButton = QtWidgets.QPushButton(DatabaseToolsDialog)
        self.testConnectionButton.setObjectName("testConnectionButton")
        self.gridLayout.addWidget(self.testConnectionButton, 7, 2, 1, 1)
        self.hostEdit = QtWidgets.QLineEdit(DatabaseToolsDialog)
        self.hostEdit.setObjectName("hostEdit")
        self.gridLayout.addWidget(self.hostEdit, 3, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(DatabaseToolsDialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(DatabaseToolsDialog)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(DatabaseToolsDialog)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 5, 1, 1, 1)
        self.label = QtWidgets.QLabel(DatabaseToolsDialog)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 9, 1, 1, 1)
        self.cancelButton = QtWidgets.QPushButton(DatabaseToolsDialog)
        self.cancelButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cancelButton.setObjectName("cancelButton")
        self.gridLayout.addWidget(self.cancelButton, 8, 2, 1, 1)
        self.databaseEdit = QtWidgets.QLineEdit(DatabaseToolsDialog)
        self.databaseEdit.setObjectName("databaseEdit")
        self.gridLayout.addWidget(self.databaseEdit, 5, 2, 1, 1)
        self.passwordEdit = QtWidgets.QLineEdit(DatabaseToolsDialog)
        self.passwordEdit.setObjectName("passwordEdit")
        self.gridLayout.addWidget(self.passwordEdit, 2, 2, 1, 1)
        self.portEdit = QtWidgets.QLineEdit(DatabaseToolsDialog)
        self.portEdit.setObjectName("portEdit")
        self.gridLayout.addWidget(self.portEdit, 4, 2, 1, 1)

        self.retranslateUi(DatabaseToolsDialog)
        QtCore.QMetaObject.connectSlotsByName(DatabaseToolsDialog)

    def retranslateUi(self, DatabaseToolsDialog):
        _translate = QtCore.QCoreApplication.translate
        DatabaseToolsDialog.setWindowTitle(_translate("DatabaseToolsDialog", "?????????????????? ?????????????????????? ?? ???????? ????????????"))
        self.label_5.setText(_translate("DatabaseToolsDialog", "????????????"))
        self.label_7.setText(_translate("DatabaseToolsDialog", "????????"))
        self.label_3.setText(_translate("DatabaseToolsDialog", "??????????????"))
        self.saveButton.setText(_translate("DatabaseToolsDialog", "??????????????????"))
        self.testConnectionButton.setText(_translate("DatabaseToolsDialog", "?????????????????? ????????????????????"))
        self.label_4.setText(_translate("DatabaseToolsDialog", "?????? ????????????????????????"))
        self.label_6.setText(_translate("DatabaseToolsDialog", "????????"))
        self.label_8.setText(_translate("DatabaseToolsDialog", "???????? ????????????"))
        self.cancelButton.setText(_translate("DatabaseToolsDialog", "????????????"))
import res_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DatabaseToolsDialog = QtWidgets.QWidget()
    ui = Ui_DatabaseToolsDialog()
    ui.setupUi(DatabaseToolsDialog)
    DatabaseToolsDialog.show()
    sys.exit(app.exec_())
