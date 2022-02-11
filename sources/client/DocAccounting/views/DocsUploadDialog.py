from PyQt5 import QtWidgets
from DocAccounting.views.ui.ui_docs_upload_dialog import Ui_DocsUploadDialog
from DocAccounting.views.Dialogs import DatabaseDialog
from DocAccounting.database.docaccounting_db_classes import Doc
from DocAccounting.views.DocsAccDialog import DocsAccDialog
import os
class DocsUploadDialog(QtWidgets.QWidget):
    """
    Класс диалога Учёт документов - Выгрузить документ
    """
    def __init__(self):
        """
        Конструктор
        """
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_DocsUploadDialog()
        # Start UI
        self.ui.setupUi(self)
        self.dialog = DocsAccDialog()
        self.setup()
        self.ui.okButton.clicked.connect(self.okButtonClicked)
        self.ui.pathButton.clicked.connect(self.pathButtonEvent)
    def setup(self):
        self.ui.cancelButton.clicked.connect(self.close)
    def showEvent(self, event):
        self.dialog.showEvent(None)
        if self.dialog.databaseDialogResult == "connected":
            self.dialog.setValues(self)

    def okButtonClicked(self):
        if hasattr(self, "filePath") and self.filePath[0] != '':
            file = open(self.filePath[0], "wb")
            self.fileBytes = file.write(self.result.docs)
        self.close()

    def pathButtonEvent(self):
        try:
            self.result = self.dialog.databaseDialog.searchData(self.ui.codeEdit.text())
        except Exception as e:
            return
        self.ui.titleEdit.setText(self.result.title)
        self.filePath = QtWidgets.QFileDialog.getSaveFileName(self, 'Select Folder', directory = "{0}.{1}".format(
            self.result.title,
            self.result.docs_ext
        ))
        if self.filePath[0] != '':
            self.ui.pathEdit.setText(self.filePath[0])







