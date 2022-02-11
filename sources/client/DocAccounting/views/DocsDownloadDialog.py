from PyQt5 import QtWidgets
from PyQt5.Qt import Qt
from DocAccounting.views.ui.ui_docs_download_dialog import Ui_DocsDownloadDialog
from DocAccounting.views.DocsAccDialog import DocsAccDialog
from DocAccounting.views.Dialogs import MainDialog
import os
class DocsDownloadDialog(QtWidgets.QWidget):
    """
    Класс диалога Учёт документов - Загрузить документ
    """
    def __init__(self):
        """
        Конструктор
        """
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_DocsDownloadDialog()
        # Start UI
        self.ui.setupUi(self)
        self.dialog = DocsAccDialog()
        self.setup()
    def setup(self):
        self.ui.cancelButton.clicked.connect(self.close)
        self.ui.pathButton.clicked.connect(self.pathButtonEvent)
        self.ui.okButton.clicked.connect(self.okButtonClicked)
    def showEvent(self, event):
        self.dialog.showEvent(None)
        if self.dialog.databaseDialogResult == "connected":
            self.dialog.setValues(self)
            self.ui.codeEdit.setEnabled(False)
    def pathButtonEvent(self):
        filePath = QtWidgets.QFileDialog.getOpenFileName(self, 'Select Folder')
        if filePath[0] != '':
            self.ui.pathEdit.setText(filePath[0])
            size = os.path.getsize(filePath[0]) / (1024 * 1024)
            self.ui.sizeMBEdit.setText(str(size))
            filename, file_extension = os.path.splitext(filePath[0])
            self.ui.docs_extEdit.setText(file_extension[1:])
            file = open(filePath[0], "rb")
            self.fileBytes = file.read()
    def okButtonClicked(self):
        self.Clazz = self.dialog.Clazz
        self.attribs = self.dialog.attribs
        self.dbModel = self.dialog.dbModel
        self.dialog.editDialog = MainDialog(self, self)
        self.ev = "Add"
        self.dialog.editDialog.okButtonEvent()
        self.close()


