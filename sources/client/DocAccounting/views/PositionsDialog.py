from PyQt5 import QtWidgets
from PyQt5.Qt import Qt
from DocAccounting.views.ui.ui_positions_dialog import Ui_PositionsDialog
from DocAccounting.views.PositionsEditDialog import PositionsEditDialog
from DocAccounting.views.Dialogs import MainDialog
from DocAccounting.database.docaccounting_db_classes import Position
from DocAccounting.models.DatabaseModel import DatabaseModel
from DocAccounting.views.Dialogs import DatabaseDialog
class PositionsDialog(QtWidgets.QWidget):
    """
    Класс диалога Должности
    """
    def __init__(self):
        """
        Конструктор
        """
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_PositionsDialog()
        self.positionsEditDialog = PositionsEditDialog()
        # Start UI
        self.ui.setupUi(self)
        self.editDialog = MainDialog(self, self.positionsEditDialog)
        self.setup()
    def setup(self):
        self.ui.cancelButton.clicked.connect(self.close)
        self.dbModel = DatabaseModel()
    def showEvent(self, event):
        self.Clazz = Position
        self.attribs = ["code", "title"]
        self.databaseDialog = DatabaseDialog(self)
        self.databaseDialog.show()



