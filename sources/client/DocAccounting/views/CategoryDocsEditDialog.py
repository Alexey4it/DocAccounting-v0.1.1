from PyQt5 import QtWidgets
from PyQt5.Qt import Qt
from DocAccounting.views.ui.ui_category_docs_edit_dialog import Ui_CategoryDocsEditDialog
from DocAccounting.views.Dialogs import EditDialog
class CategoryDocsEditDialog(QtWidgets.QWidget):
    """
    Класс диалога Категории документа - Редактирование
    """
    def __init__(self):
        """
        Конструктор
        """
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_CategoryDocsEditDialog()
        # Start UI
        self.ui.setupUi(self)
        self.setup()
    def setup(self):
        self.ui.cancelButton.clicked.connect(self.close)
    def showEvent(self, event):
        EditDialog(self, "Категории документов").show()

