from PyQt5 import QtWidgets
from PyQt5.Qt import Qt
from DocAccounting.views.ui.ui_sources_edit_dialog import Ui_SourcesEditDialog
from DocAccounting.views.Dialogs import EditDialog
class SourcesEditDialog(QtWidgets.QWidget):
    """
    Класс диалога Источники документа - Редактирование
    """
    def __init__(self):
        """
        Конструктор
        """
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_SourcesEditDialog()
        # Start UI
        self.ui.setupUi(self)
        self.setup()
    def setup(self):
        self.ui.cancelButton.clicked.connect(self.close)
    def showEvent(self, event):
        EditDialog(self, "Источники").show()


