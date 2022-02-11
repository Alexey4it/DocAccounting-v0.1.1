from PyQt5 import QtWidgets
from PyQt5.Qt import Qt
from DocAccounting.views.ui.ui_docs_regulation_dialog import Ui_DocsRegulationDialog
from DocAccounting.views.DocsRegulationEditDialog import DocsRegulationEditDialog
from DocAccounting.views.Dialogs import MainDialog
from DocAccounting.database.docaccounting_db_classes import Regulation
from DocAccounting.models.DatabaseModel import DatabaseModel
from DocAccounting.views.Dialogs import DatabaseDialog
import os
class DocsRegulationDialog(QtWidgets.QWidget):
    """
    Класс диалога Нормативные документы
    """
    def __init__(self):
        """
        Конструктор
        """
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_DocsRegulationDialog()
        self.docsRegulationEditDialog = DocsRegulationEditDialog()
        # Start UI
        self.ui.setupUi(self)
        self.editDialog = MainDialog(self, self.docsRegulationEditDialog)
        self.setup()
    def setup(self):
        self.fileBytes = bytes("", encoding='utf-8')
        self.ui.cancelButton.clicked.connect(self.close)
        self.docsRegulationEditDialog.ui.pathButton.clicked.connect(self.pathButtonEvent)
        self.dbModel = DatabaseModel()

    def showEvent(self, event):
        self.Clazz = Regulation
        self.attribs = ["code", "category", "title", "docs", "docs_ext", "url"]

        self.databaseDialog = DatabaseDialog(self)
        self.databaseDialog.show()

    def pathButtonEvent(self):
        if self.docsRegulationEditDialog.ev == "Add" or self.docsRegulationEditDialog.ev == "Update":
            filePath = QtWidgets.QFileDialog.getOpenFileName(self, 'Select Folder')
            if filePath[0] != '':
                self.docsRegulationEditDialog.ui.pathEdit.setText(filePath[0])
                filename, file_extension = os.path.splitext(filePath[0])
                self.docsRegulationEditDialog.ui.docs_extEdit.setText(file_extension[1:])
                file = open(filePath[0], "rb")
                self.fileBytes = file.read()




