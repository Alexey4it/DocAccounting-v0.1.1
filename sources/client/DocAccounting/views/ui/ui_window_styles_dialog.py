# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DocAccounting/views/ui/WindowStylesDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WindowStylesDialog(object):
    def setupUi(self, WindowStylesDialog):
        WindowStylesDialog.setObjectName("WindowStylesDialog")
        WindowStylesDialog.resize(525, 374)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        WindowStylesDialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        WindowStylesDialog.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(WindowStylesDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.systemRadioButton = QtWidgets.QRadioButton(WindowStylesDialog)
        self.systemRadioButton.setMinimumSize(QtCore.QSize(0, 0))
        self.systemRadioButton.setChecked(True)
        self.systemRadioButton.setObjectName("systemRadioButton")
        self.gridLayout.addWidget(self.systemRadioButton, 1, 0, 1, 1)
        self.okButton = QtWidgets.QPushButton(WindowStylesDialog)
        self.okButton.setObjectName("okButton")
        self.gridLayout.addWidget(self.okButton, 9, 1, 1, 1)
        self.label = QtWidgets.QLabel(WindowStylesDialog)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 9, 0, 1, 1)
        self.cancelButton = QtWidgets.QPushButton(WindowStylesDialog)
        self.cancelButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cancelButton.setObjectName("cancelButton")
        self.gridLayout.addWidget(self.cancelButton, 9, 2, 1, 1)
        self.lightRadioButton = QtWidgets.QRadioButton(WindowStylesDialog)
        self.lightRadioButton.setMinimumSize(QtCore.QSize(0, 0))
        self.lightRadioButton.setObjectName("lightRadioButton")
        self.gridLayout.addWidget(self.lightRadioButton, 8, 0, 1, 1)
        self.darkRadioButton = QtWidgets.QRadioButton(WindowStylesDialog)
        self.darkRadioButton.setMinimumSize(QtCore.QSize(0, 0))
        self.darkRadioButton.setObjectName("darkRadioButton")
        self.gridLayout.addWidget(self.darkRadioButton, 2, 0, 1, 1)

        self.retranslateUi(WindowStylesDialog)
        QtCore.QMetaObject.connectSlotsByName(WindowStylesDialog)

    def retranslateUi(self, WindowStylesDialog):
        _translate = QtCore.QCoreApplication.translate
        WindowStylesDialog.setWindowTitle(_translate("WindowStylesDialog", "Стиль окна"))
        self.systemRadioButton.setText(_translate("WindowStylesDialog", "Системный"))
        self.okButton.setText(_translate("WindowStylesDialog", "OK"))
        self.cancelButton.setText(_translate("WindowStylesDialog", "Отмена"))
        self.lightRadioButton.setText(_translate("WindowStylesDialog", "Светлый"))
        self.darkRadioButton.setText(_translate("WindowStylesDialog", "Темный"))
import res_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WindowStylesDialog = QtWidgets.QWidget()
    ui = Ui_WindowStylesDialog()
    ui.setupUi(WindowStylesDialog)
    WindowStylesDialog.show()
    sys.exit(app.exec_())
