from PyQt5 import QtWidgets
from PyQt5.Qt import Qt
from DocAccounting.views.ui.ui_category_docs_dialog import Ui_CategoryDocsDialog
from DocAccounting.views.CategoryDocsEditDialog import CategoryDocsEditDialog
from DocAccounting.views.Dialogs import MainDialog
from DocAccounting.database.docaccounting_db_classes import CategoryDoc
from DocAccounting.models.DatabaseModel import DatabaseModel
from DocAccounting.views.Dialogs import DatabaseDialog
class CategoryDocsDialog(QtWidgets.QWidget):
    """
    Класс диалога Категории документа
    """
    def __init__(self):
        """
        Конструктор
        """
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_CategoryDocsDialog()
        self.categoryDocsEditDialog = CategoryDocsEditDialog()
        # Start UI
        self.ui.setupUi(self)
        self.editDialog = MainDialog(self, self.categoryDocsEditDialog)
        self.setup()
    def setup(self):
        self.ui.cancelButton.clicked.connect(self.close)
        self.dbModel = DatabaseModel()

    def showEvent(self, event):
        self.attribs = ["code", "title"]
        self.Clazz = CategoryDoc
        self.databaseDialog = DatabaseDialog(self)
        self.databaseDialog.show()


