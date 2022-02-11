from PyQt5 import QtWidgets
from DocAccounting.views.ui.ui_docs_change_dialog import Ui_DocsChangeDialog
from DocAccounting.views.DocsAccDialog import DocsAccDialog
from DocAccounting.views.Dialogs import MainDialog
from PyQt5.QtCore import QDateTime
import os
class DocsChangeDialog(QtWidgets.QWidget):
    """
    Класс диалога Учет документов - Изменение документа
    """
    def __init__(self):
        """
        Конструктор
        """
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_DocsChangeDialog()
        # Start UI
        self.ui.setupUi(self)
        self.dialog = DocsAccDialog()
        self.setup()
    def setup(self):
        self.ui.cancelButton.clicked.connect(self.close)
        self.ui.okButton.clicked.connect(self.okButtonClicked)
        self.ui.codeEdit.textChanged.connect(self.codeEditChanged)

    def showEvent(self, event):
        self.dialog.showEvent(None)
        if self.dialog.databaseDialogResult == "connected":
            self.dialog.setValues(self)
            self.Clazz = self.dialog.Clazz
            self.attribs = self.dialog.attribs
            self.dbModel = self.dialog.dbModel
    def codeEditChanged(self):
        try:
            items = self.dbModel.searchData(self.Clazz, self.ui.codeEdit.text())
        except Exception as e:
            return
        count = 0
        for attrib in self.attribs:
            if hasattr(self.ui, attrib + "Edit"):
                value = getattr(self.ui, attrib + "Edit")
                value.setText(str(getattr(items, attrib)))
            if hasattr(self.ui, attrib + "DateTimeEdit"):
                value = getattr(self.ui, attrib + "DateTimeEdit")
                dateTime = QDateTime.fromString(str(getattr(items, attrib)), "yyyy-MM-dd HH:mm:ss")
                value.setDateTime(dateTime)
            if hasattr(self.ui, attrib + "SpinBox"):
                value = getattr(self.ui, attrib + "SpinBox")
                value.setValue(getattr(items, attrib))
            if hasattr(self.ui, attrib + "ComboBox"):
                value = getattr(self.ui, attrib + "ComboBox")
                for index in range(value.count()):
                    value.setCurrentIndex(index)
                    comboBoxValue = value.currentText().split('-')[0]
                    if int(comboBoxValue) == int(getattr(items, attrib)):
                        break

            count += 1

    def okButtonClicked(self):
        self.dialog.editDialog = MainDialog(self, self)
        self.ev = "Update"
        self.dialog.editDialog.okButtonEvent()
        self.close()


