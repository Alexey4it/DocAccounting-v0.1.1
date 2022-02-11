from PyQt5 import QtWidgets
from PyQt5.Qt import Qt
from DocAccounting.views.ui.ui_statusdocs_dialog import Ui_StatusDocsDialog
from DocAccounting.views.StatusDocsEditDialog import StatusDocsEditDialog
from DocAccounting.views.Dialogs import MainDialog
from DocAccounting.database.docaccounting_db_classes import StatusDoc
from DocAccounting.models.DatabaseModel import DatabaseModel
from DocAccounting.views.Dialogs import DatabaseDialog
class StatusDocsDialog(QtWidgets.QWidget):
    """
    Класс диалога Статус документа
    """
    def __init__(self):
        """
        Конструктор
        """
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_StatusDocsDialog()
        self.statusDocsEditDialog = StatusDocsEditDialog()
        # Start UI
        self.ui.setupUi(self)
        self.editDialog = MainDialog(self, self.statusDocsEditDialog)
        self.setup()
    def setup(self):
        self.ui.cancelButton.clicked.connect(self.close)
        self.dbModel = DatabaseModel()

    def showEvent(self, event):
        self.Clazz = StatusDoc
        self.attribs = ["code", "title", "description"]
        self.databaseDialog = DatabaseDialog(self)
        self.databaseDialog.show()


