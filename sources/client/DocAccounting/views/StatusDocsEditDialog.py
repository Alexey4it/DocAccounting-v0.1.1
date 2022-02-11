from PyQt5 import QtWidgets
from PyQt5.Qt import Qt
from DocAccounting.views.ui.ui_statusdocs_edit_dialog import Ui_StatusDocsEditDialog
from DocAccounting.views.Dialogs import EditDialog
class StatusDocsEditDialog(QtWidgets.QWidget):
    """
    Класс диалога Статус документа - Редактирование
    """
    def __init__(self):
        """
        Конструктор
        """
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_StatusDocsEditDialog()
        # Start UI
        self.ui.setupUi(self)
        self.setup()
    def setup(self):
        self.ui.cancelButton.clicked.connect(self.close)
    def showEvent(self, event):
        EditDialog(self, "Статус документа").show()


