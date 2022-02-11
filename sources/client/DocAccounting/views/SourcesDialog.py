from PyQt5 import QtWidgets
from PyQt5.Qt import Qt
from DocAccounting.views.ui.ui_sources_dialog import Ui_SourcesDialog
from DocAccounting.settings import getVersion
from DocAccounting.views.SourcesEditDialog import SourcesEditDialog
from DocAccounting.views.Dialogs import MainDialog
from DocAccounting.database.docaccounting_db_classes import Source
from DocAccounting.models.DatabaseModel import DatabaseModel
from DocAccounting.views.Dialogs import DatabaseDialog
class SourcesDocsDialog(QtWidgets.QWidget):
    """
    Класс диалога Источинки документа
    """
    def __init__(self):
        """
        Конструктор
        """
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_SourcesDialog()
        # Start UI
        self.ui.setupUi(self)
        self.sourcesEditDialog = SourcesEditDialog()
        self.editDialog = MainDialog(self, self.sourcesEditDialog)
        self.setup()
    def setup(self):
        self.ui.cancelButton.clicked.connect(self.close)
        self.dbModel = DatabaseModel()

    def showEvent(self, event):
        self.Clazz = Source
        self.attribs = ["code", "title"]
        self.databaseDialog = DatabaseDialog(self)
        self.databaseDialog.show()
