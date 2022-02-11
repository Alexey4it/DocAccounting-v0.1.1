from PyQt5 import QtWidgets
from PyQt5.Qt import Qt
from DocAccounting.views.ui.ui_view_docs_dialog import Ui_ViewDocsDialog
from DocAccounting.views.ViewDocsEditDialog import ViewDocsEditDialog
from DocAccounting.views.Dialogs import MainDialog
from DocAccounting.database.docaccounting_db_classes import ViewDoc
from DocAccounting.models.DatabaseModel import DatabaseModel
from DocAccounting.views.Dialogs import DatabaseDialog
class ViewDocsDialog(QtWidgets.QWidget):
    """
    Класс диалога Вид документа
    """
    def __init__(self):
        """
        Конструктор
        """
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_ViewDocsDialog()
        self.viewDocsEditDialog = ViewDocsEditDialog()
        # Start UI
        self.ui.setupUi(self)
        self.editDialog = MainDialog(self, self.viewDocsEditDialog)
        self.setup()
    def setup(self):
        self.ui.cancelButton.clicked.connect(self.close)
        self.dbModel = DatabaseModel()
    def showEvent(self, event):
        self.Clazz = ViewDoc
        self.attribs = ["code", "title", "description"]
        self.databaseDialog = DatabaseDialog(self)
        self.databaseDialog.show()



