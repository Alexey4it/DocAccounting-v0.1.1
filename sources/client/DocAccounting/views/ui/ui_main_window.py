# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DocAccounting/views/ui/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(500, 500))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(200, 200))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icons/icon.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.appLabel = QtWidgets.QLabel(self.centralwidget)
        self.appLabel.setText("")
        self.appLabel.setObjectName("appLabel")
        self.gridLayout.addWidget(self.appLabel, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 28))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.menu.setFont(font)
        self.menu.setTearOffEnabled(False)
        self.menu.setSeparatorsCollapsible(False)
        self.menu.setToolTipsVisible(False)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.menu_2.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu_2.setIcon(icon1)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.menu_3.setFont(font)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menu_3)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.menu_4.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/files.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu_4.setIcon(icon2)
        self.menu_4.setObjectName("menu_4")
        self.menu_5 = QtWidgets.QMenu(self.menu_3)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.menu_5.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/db.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu_5.setIcon(icon3)
        self.menu_5.setObjectName("menu_5")
        self.menu_6 = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.menu_6.setFont(font)
        self.menu_6.setObjectName("menu_6")
        self.menu_7 = QtWidgets.QMenu(self.menubar)
        self.menu_7.setObjectName("menu_7")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.aboutAction = QtWidgets.QAction(MainWindow)
        self.aboutAction.setIcon(icon1)
        self.aboutAction.setObjectName("aboutAction")
        self.closeAction = QtWidgets.QAction(MainWindow)
        self.closeAction.setObjectName("closeAction")
        self.employeeAction = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/employees.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.employeeAction.setIcon(icon4)
        self.employeeAction.setObjectName("employeeAction")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.docsAccAction = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/docs.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.docsAccAction.setIcon(icon5)
        self.docsAccAction.setObjectName("docsAccAction")
        self.docsDownloadAction = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/download.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.docsDownloadAction.setIcon(icon6)
        self.docsDownloadAction.setObjectName("docsDownloadAction")
        self.docsUploadAction = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/upload.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.docsUploadAction.setIcon(icon7)
        self.docsUploadAction.setObjectName("docsUploadAction")
        self.docsChangeAction = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/exchange.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.docsChangeAction.setIcon(icon8)
        self.docsChangeAction.setObjectName("docsChangeAction")
        self.action_9 = QtWidgets.QAction(MainWindow)
        self.action_9.setEnabled(False)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_9.setIcon(icon9)
        self.action_9.setObjectName("action_9")
        self.barcodeAction = QtWidgets.QAction(MainWindow)
        self.barcodeAction.setEnabled(False)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icons/codebar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.barcodeAction.setIcon(icon10)
        self.barcodeAction.setObjectName("barcodeAction")
        self.helpDocsAction = QtWidgets.QAction(MainWindow)
        self.helpDocsAction.setEnabled(False)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icons/doc_help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.helpDocsAction.setIcon(icon11)
        self.helpDocsAction.setObjectName("helpDocsAction")
        self.positionsAction = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/icons/position.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.positionsAction.setIcon(icon12)
        self.positionsAction.setObjectName("positionsAction")
        self.developersAction = QtWidgets.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/icons/developer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.developersAction.setIcon(icon13)
        self.developersAction.setObjectName("developersAction")
        self.statusDocAction = QtWidgets.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/icons/status.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.statusDocAction.setIcon(icon14)
        self.statusDocAction.setObjectName("statusDocAction")
        self.sourcesAction = QtWidgets.QAction(MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/icons/sourcing.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sourcesAction.setIcon(icon15)
        self.sourcesAction.setObjectName("sourcesAction")
        self.categoryDocsAction = QtWidgets.QAction(MainWindow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/icons/category.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.categoryDocsAction.setIcon(icon16)
        self.categoryDocsAction.setObjectName("categoryDocsAction")
        self.docsRegulationAction = QtWidgets.QAction(MainWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/icons/regulatory.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.docsRegulationAction.setIcon(icon17)
        self.docsRegulationAction.setObjectName("docsRegulationAction")
        self.databaseToolsAction = QtWidgets.QAction(MainWindow)
        self.databaseToolsAction.setObjectName("databaseToolsAction")
        self.valuesDatabaseAction = QtWidgets.QAction(MainWindow)
        self.valuesDatabaseAction.setObjectName("valuesDatabaseAction")
        self.windowStyleAction = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.windowStyleAction.setFont(font)
        self.windowStyleAction.setObjectName("windowStyleAction")
        self.departmentAction = QtWidgets.QAction(MainWindow)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(":/icons/department.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.departmentAction.setIcon(icon18)
        self.departmentAction.setObjectName("departmentAction")
        self.viewDocsAction = QtWidgets.QAction(MainWindow)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(":/icons/view.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.viewDocsAction.setIcon(icon19)
        self.viewDocsAction.setObjectName("viewDocsAction")
        self.menu.addAction(self.closeAction)
        self.menu_2.addAction(self.aboutAction)
        self.menu_4.addAction(self.docsAccAction)
        self.menu_4.addAction(self.docsDownloadAction)
        self.menu_4.addAction(self.docsUploadAction)
        self.menu_4.addAction(self.docsChangeAction)
        self.menu_4.addAction(self.action_9)
        self.menu_5.addAction(self.positionsAction)
        self.menu_5.addAction(self.developersAction)
        self.menu_5.addAction(self.statusDocAction)
        self.menu_5.addAction(self.sourcesAction)
        self.menu_5.addAction(self.categoryDocsAction)
        self.menu_5.addAction(self.docsRegulationAction)
        self.menu_5.addAction(self.departmentAction)
        self.menu_5.addAction(self.viewDocsAction)
        self.menu_3.addAction(self.employeeAction)
        self.menu_3.addAction(self.menu_4.menuAction())
        self.menu_3.addAction(self.barcodeAction)
        self.menu_3.addAction(self.helpDocsAction)
        self.menu_3.addAction(self.menu_5.menuAction())
        self.menu_6.addAction(self.databaseToolsAction)
        self.menu_6.addAction(self.valuesDatabaseAction)
        self.menu_7.addAction(self.windowStyleAction)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_6.menuAction())
        self.menubar.addAction(self.menu_7.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DocAccounting (???? ?????????? ????????????????????) - ???????????? 0.0.1"))
        self.menu.setTitle(_translate("MainWindow", "????????"))
        self.menu_2.setTitle(_translate("MainWindow", "??????????????"))
        self.menu_3.setTitle(_translate("MainWindow", "????????????"))
        self.menu_4.setTitle(_translate("MainWindow", "??????????????????"))
        self.menu_5.setTitle(_translate("MainWindow", "?????????????? ????"))
        self.menu_6.setTitle(_translate("MainWindow", "??????????????????"))
        self.menu_7.setTitle(_translate("MainWindow", "????????"))
        self.aboutAction.setText(_translate("MainWindow", "?? ??????????????????"))
        self.aboutAction.setShortcut(_translate("MainWindow", "F1"))
        self.closeAction.setText(_translate("MainWindow", "??????????"))
        self.employeeAction.setText(_translate("MainWindow", "???????? ??????????????????????"))
        self.action_3.setText(_translate("MainWindow", "???????????? ???????????????? ??????????????????"))
        self.action_4.setText(_translate("MainWindow", "???????????? ???????????????? ??????????????????"))
        self.docsAccAction.setText(_translate("MainWindow", "????????"))
        self.docsDownloadAction.setText(_translate("MainWindow", "????????????????"))
        self.docsUploadAction.setText(_translate("MainWindow", "????????????????"))
        self.docsChangeAction.setText(_translate("MainWindow", "??????????????????"))
        self.action_9.setText(_translate("MainWindow", "??????????"))
        self.barcodeAction.setText(_translate("MainWindow", "???????????? ???? ??????????????????????"))
        self.helpDocsAction.setText(_translate("MainWindow", "???????????????????? ????????????????????"))
        self.positionsAction.setText(_translate("MainWindow", "??????????????????"))
        self.developersAction.setText(_translate("MainWindow", "????????????????????????"))
        self.statusDocAction.setText(_translate("MainWindow", "???????????? ??????????????????"))
        self.sourcesAction.setText(_translate("MainWindow", "??????????????????"))
        self.categoryDocsAction.setText(_translate("MainWindow", "?????????????????? ????????????????????"))
        self.docsRegulationAction.setText(_translate("MainWindow", "?????????????????????? ??????????????????"))
        self.databaseToolsAction.setText(_translate("MainWindow", "?????????????????? ????"))
        self.valuesDatabaseAction.setText(_translate("MainWindow", "?????????????????? ?????????????? ???????? ???????????? ????????????????????"))
        self.windowStyleAction.setText(_translate("MainWindow", "?????????? ????????"))
        self.departmentAction.setText(_translate("MainWindow", "????????????"))
        self.viewDocsAction.setText(_translate("MainWindow", "?????? ??????????????????"))
import res_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
