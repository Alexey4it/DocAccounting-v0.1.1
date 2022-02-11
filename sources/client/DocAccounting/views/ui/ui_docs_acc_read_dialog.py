# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DocAccounting/views/ui/DocsAccReadDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DocsAccReadDialog(object):
    def setupUi(self, DocsAccReadDialog):
        DocsAccReadDialog.setObjectName("DocsAccReadDialog")
        DocsAccReadDialog.resize(582, 721)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        DocsAccReadDialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DocsAccReadDialog.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(DocsAccReadDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.date_changeDateTimeEdit = QtWidgets.QDateTimeEdit(DocsAccReadDialog)
        self.date_changeDateTimeEdit.setObjectName("date_changeDateTimeEdit")
        self.gridLayout.addWidget(self.date_changeDateTimeEdit, 10, 2, 1, 2)
        self.label_11 = QtWidgets.QLabel(DocsAccReadDialog)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 11, 0, 1, 1)
        self.keywordsEdit = QtWidgets.QLineEdit(DocsAccReadDialog)
        self.keywordsEdit.setObjectName("keywordsEdit")
        self.gridLayout.addWidget(self.keywordsEdit, 12, 2, 1, 2)
        self.label_8 = QtWidgets.QLabel(DocsAccReadDialog)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 8, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(DocsAccReadDialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(DocsAccReadDialog)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 17, 0, 1, 1)
        self.date_loadingDateTimeEdit = QtWidgets.QDateTimeEdit(DocsAccReadDialog)
        self.date_loadingDateTimeEdit.setObjectName("date_loadingDateTimeEdit")
        self.gridLayout.addWidget(self.date_loadingDateTimeEdit, 9, 2, 1, 2)
        self.source_codeComboBox = QtWidgets.QComboBox(DocsAccReadDialog)
        self.source_codeComboBox.setObjectName("source_codeComboBox")
        self.gridLayout.addWidget(self.source_codeComboBox, 7, 2, 1, 2)
        self.label_2 = QtWidgets.QLabel(DocsAccReadDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(DocsAccReadDialog)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 16, 0, 1, 1)
        self.copy_nSpinBox = QtWidgets.QSpinBox(DocsAccReadDialog)
        self.copy_nSpinBox.setObjectName("copy_nSpinBox")
        self.gridLayout.addWidget(self.copy_nSpinBox, 15, 2, 1, 2)
        self.label_10 = QtWidgets.QLabel(DocsAccReadDialog)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 10, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(DocsAccReadDialog)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 15, 0, 1, 1)
        self.cupboardEdit = QtWidgets.QLineEdit(DocsAccReadDialog)
        self.cupboardEdit.setObjectName("cupboardEdit")
        self.gridLayout.addWidget(self.cupboardEdit, 16, 2, 1, 2)
        self.view_codeComboBox = QtWidgets.QComboBox(DocsAccReadDialog)
        self.view_codeComboBox.setObjectName("view_codeComboBox")
        self.gridLayout.addWidget(self.view_codeComboBox, 2, 2, 1, 2)
        self.status_codeComboBox = QtWidgets.QComboBox(DocsAccReadDialog)
        self.status_codeComboBox.setObjectName("status_codeComboBox")
        self.gridLayout.addWidget(self.status_codeComboBox, 5, 2, 1, 2)
        self.label_14 = QtWidgets.QLabel(DocsAccReadDialog)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 13, 0, 1, 1)
        self.employee_codeComboBox = QtWidgets.QComboBox(DocsAccReadDialog)
        self.employee_codeComboBox.setObjectName("employee_codeComboBox")
        self.gridLayout.addWidget(self.employee_codeComboBox, 4, 2, 1, 2)
        self.developer_codeComboBox = QtWidgets.QComboBox(DocsAccReadDialog)
        self.developer_codeComboBox.setObjectName("developer_codeComboBox")
        self.gridLayout.addWidget(self.developer_codeComboBox, 6, 2, 1, 2)
        self.pagesSpinBox = QtWidgets.QSpinBox(DocsAccReadDialog)
        self.pagesSpinBox.setObjectName("pagesSpinBox")
        self.gridLayout.addWidget(self.pagesSpinBox, 14, 2, 1, 2)
        self.label_13 = QtWidgets.QLabel(DocsAccReadDialog)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 12, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(DocsAccReadDialog)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 7, 0, 1, 1)
        self.label = QtWidgets.QLabel(DocsAccReadDialog)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 20, 0, 1, 1)
        self.section_numberSpinBox = QtWidgets.QSpinBox(DocsAccReadDialog)
        self.section_numberSpinBox.setObjectName("section_numberSpinBox")
        self.gridLayout.addWidget(self.section_numberSpinBox, 13, 2, 1, 2)
        self.pathEdit = QtWidgets.QLineEdit(DocsAccReadDialog)
        self.pathEdit.setObjectName("pathEdit")
        self.gridLayout.addWidget(self.pathEdit, 19, 2, 1, 1)
        self.category_codeComboBox = QtWidgets.QComboBox(DocsAccReadDialog)
        self.category_codeComboBox.setObjectName("category_codeComboBox")
        self.gridLayout.addWidget(self.category_codeComboBox, 1, 2, 1, 2)
        self.pushButton = QtWidgets.QPushButton(DocsAccReadDialog)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 19, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(DocsAccReadDialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(DocsAccReadDialog)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 14, 0, 1, 1)
        self.descriptionEdit = QtWidgets.QLineEdit(DocsAccReadDialog)
        self.descriptionEdit.setObjectName("descriptionEdit")
        self.gridLayout.addWidget(self.descriptionEdit, 18, 2, 1, 2)
        self.label_3 = QtWidgets.QLabel(DocsAccReadDialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(DocsAccReadDialog)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 9, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(DocsAccReadDialog)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 19, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(DocsAccReadDialog)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 18, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(DocsAccReadDialog)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)
        self.titleEdit = QtWidgets.QLineEdit(DocsAccReadDialog)
        self.titleEdit.setObjectName("titleEdit")
        self.gridLayout.addWidget(self.titleEdit, 8, 2, 1, 2)
        self.rackEdit = QtWidgets.QLineEdit(DocsAccReadDialog)
        self.rackEdit.setObjectName("rackEdit")
        self.gridLayout.addWidget(self.rackEdit, 17, 2, 1, 2)
        self.cancelButton = QtWidgets.QPushButton(DocsAccReadDialog)
        self.cancelButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cancelButton.setObjectName("cancelButton")
        self.gridLayout.addWidget(self.cancelButton, 20, 3, 1, 1)
        self.label_21 = QtWidgets.QLabel(DocsAccReadDialog)
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 0, 0, 1, 1)
        self.codeEdit = QtWidgets.QLineEdit(DocsAccReadDialog)
        self.codeEdit.setObjectName("codeEdit")
        self.gridLayout.addWidget(self.codeEdit, 0, 2, 1, 2)
        self.barcodeEdit = QtWidgets.QLineEdit(DocsAccReadDialog)
        self.barcodeEdit.setObjectName("barcodeEdit")
        self.gridLayout.addWidget(self.barcodeEdit, 11, 2, 1, 2)

        self.retranslateUi(DocsAccReadDialog)
        QtCore.QMetaObject.connectSlotsByName(DocsAccReadDialog)

    def retranslateUi(self, DocsAccReadDialog):
        _translate = QtCore.QCoreApplication.translate
        DocsAccReadDialog.setWindowTitle(_translate("DocsAccReadDialog", "Просмотр документа"))
        self.date_changeDateTimeEdit.setDisplayFormat(_translate("DocsAccReadDialog", "yyyy-MM-dd HH:mm:ss"))
        self.label_11.setText(_translate("DocsAccReadDialog", "Штрих-код"))
        self.label_8.setText(_translate("DocsAccReadDialog", "Наименование"))
        self.label_5.setText(_translate("DocsAccReadDialog", "Статус документа"))
        self.label_18.setText(_translate("DocsAccReadDialog", "Полка"))
        self.date_loadingDateTimeEdit.setDisplayFormat(_translate("DocsAccReadDialog", "yyyy-MM-dd HH:mm:ss"))
        self.label_2.setText(_translate("DocsAccReadDialog", "Категория"))
        self.label_17.setText(_translate("DocsAccReadDialog", "Шкаф"))
        self.label_10.setText(_translate("DocsAccReadDialog", "Дата изменения"))
        self.label_16.setText(_translate("DocsAccReadDialog", "Копия N"))
        self.label_14.setText(_translate("DocsAccReadDialog", "Номер секции"))
        self.label_13.setText(_translate("DocsAccReadDialog", "Ключевые слова"))
        self.label_7.setText(_translate("DocsAccReadDialog", "Источник"))
        self.pushButton.setText(_translate("DocsAccReadDialog", "..."))
        self.label_4.setText(_translate("DocsAccReadDialog", "Сотрудник"))
        self.label_15.setText(_translate("DocsAccReadDialog", "Страницы"))
        self.label_3.setText(_translate("DocsAccReadDialog", "Вид документа"))
        self.label_9.setText(_translate("DocsAccReadDialog", "Дата загрузки"))
        self.label_20.setText(_translate("DocsAccReadDialog", "Путь к документу"))
        self.label_19.setText(_translate("DocsAccReadDialog", "Описание"))
        self.label_6.setText(_translate("DocsAccReadDialog", "Разработчик"))
        self.cancelButton.setText(_translate("DocsAccReadDialog", "Отмена"))
        self.label_21.setText(_translate("DocsAccReadDialog", "Код"))
import res_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DocsAccReadDialog = QtWidgets.QWidget()
    ui = Ui_DocsAccReadDialog()
    ui.setupUi(DocsAccReadDialog)
    DocsAccReadDialog.show()
    sys.exit(app.exec_())