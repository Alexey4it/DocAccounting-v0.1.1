from PyQt5 import QtWidgets
from PyQt5.Qt import Qt
from DocAccounting.views.ui.ui_docs_regulation_edit_dialog import Ui_DocsRegulationEditDialog
from DocAccounting.views.Dialogs import EditDialog
import os
class DocsRegulationEditDialog(QtWidgets.QWidget):
    """
    Класс диалога Нормативные документы - Редактирование
    """
    def __init__(self):
        """
        Конструктор
        """
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_DocsRegulationEditDialog()
        # Start UI
        self.ui.setupUi(self)
        self.setup()
    def setup(self):
        self.ui.cancelButton.clicked.connect(self.close)
    def showEvent(self, event):
        EditDialog(self, "Нормативные документы").show()


