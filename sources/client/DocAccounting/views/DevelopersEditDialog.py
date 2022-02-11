from PyQt5 import QtWidgets
from PyQt5.Qt import Qt
from DocAccounting.views.ui.ui_developers_edit_dialog import Ui_DevelopersEditDialog
from DocAccounting.views.Dialogs import EditDialog
class DevelopersEditDialog(QtWidgets.QWidget):
    """
    Класс диалога Разработчики документа - Редактирование
    """
    def __init__(self):
        """
        Конструктор
        """
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_DevelopersEditDialog()
        # Start UI
        self.ui.setupUi(self)
        self.setup()
    def setup(self):
        self.ui.cancelButton.clicked.connect(self.close)
    def showEvent(self, event):
        EditDialog(self, "Разработчики").show()


