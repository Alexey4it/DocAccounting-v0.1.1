from PyQt5 import QtWidgets
from PyQt5.Qt import Qt
from DocAccounting.views.ui.ui_developers_dialog import Ui_DevelopersDialog
from DocAccounting.views.DevelopersEditDialog import DevelopersEditDialog
from DocAccounting.views.Dialogs import MainDialog
from DocAccounting.views.Dialogs import DatabaseDialog
from DocAccounting.database.docaccounting_db_classes import Developer
from DocAccounting.models.DatabaseModel import DatabaseModel
class DevelopersDialog(QtWidgets.QWidget):
    """
    Класс диалога Разработчики документа
    """
    def __init__(self):
        """
        Конструктор
        """
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_DevelopersDialog()
        self.developersEditDialog = DevelopersEditDialog()
        # Start UI
        self.ui.setupUi(self)
        self.editDialog = MainDialog(self, self.developersEditDialog)
        self.setup()
    def setup(self):
        self.ui.cancelButton.clicked.connect(self.close)
        self.dbModel = DatabaseModel()
    def showEvent(self, event):
        self.Clazz = Developer
        self.attribs = ["code", "title", "comments"]
        self.databaseDialog = DatabaseDialog(self)
        self.databaseDialog.show()
