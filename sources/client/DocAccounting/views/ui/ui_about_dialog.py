# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DocAccounting/views/ui/AboutDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        AboutDialog.setObjectName("AboutDialog")
        AboutDialog.resize(611, 379)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        AboutDialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AboutDialog.setWindowIcon(icon)
        AboutDialog.setModal(True)
        self.gridLayout = QtWidgets.QGridLayout(AboutDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(AboutDialog)
        self.label.setMaximumSize(QtCore.QSize(200, 200))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icons/icon.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.okButton = QtWidgets.QPushButton(AboutDialog)
        self.okButton.setObjectName("okButton")
        self.gridLayout.addWidget(self.okButton, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(AboutDialog)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.aboutLabel = QtWidgets.QLabel(AboutDialog)
        self.aboutLabel.setMaximumSize(QtCore.QSize(16777215, 40))
        self.aboutLabel.setStyleSheet("color:blue;")
        self.aboutLabel.setText("")
        self.aboutLabel.setObjectName("aboutLabel")
        self.gridLayout.addWidget(self.aboutLabel, 1, 1, 1, 1)

        self.retranslateUi(AboutDialog)
        QtCore.QMetaObject.connectSlotsByName(AboutDialog)

    def retranslateUi(self, AboutDialog):
        _translate = QtCore.QCoreApplication.translate
        AboutDialog.setWindowTitle(_translate("AboutDialog", "О программе ..."))
        self.okButton.setText(_translate("AboutDialog", "OK"))
        self.label_2.setText(_translate("AboutDialog", "<html><head/><body><p>Информационная система учёта документов</p></body></html>"))
import res_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AboutDialog = QtWidgets.QDialog()
    ui = Ui_AboutDialog()
    ui.setupUi(AboutDialog)
    AboutDialog.show()
    sys.exit(app.exec_())
