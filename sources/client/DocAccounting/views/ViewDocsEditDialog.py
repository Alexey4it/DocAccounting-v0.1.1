from PyQt5 import QtWidgets
from PyQt5.Qt import Qt
from DocAccounting.views.ui.ui_view_docs_edit_dialog import Ui_ViewDocsEditDialog
from DocAccounting.views.Dialogs import EditDialog
class ViewDocsEditDialog(QtWidgets.QWidget):
    """
    Класс диалога Вид документа - Редактирование
    """
    def __init__(self):
        """
        Конструктор
        """
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_ViewDocsEditDialog()
        # Start UI
        self.ui.setupUi(self)
        self.setup()
    def setup(self):
        self.ui.cancelButton.clicked.connect(self.close)
    def showEvent(self, event):
        EditDialog(self, "Вид документа").show()


