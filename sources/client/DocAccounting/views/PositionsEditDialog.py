from PyQt5 import QtWidgets
from PyQt5.Qt import Qt
from DocAccounting.views.ui.ui_positions_edit_dialog import Ui_PositionsEditDialog
from DocAccounting.views.Dialogs import EditDialog
class PositionsEditDialog(QtWidgets.QWidget):
    """
    Класс диалога Должности - Редактирование
    """
    def __init__(self):
        """
        Конструктор
        """
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_PositionsEditDialog()
        # Start UI
        self.ui.setupUi(self)
        self.setup()
    def setup(self):
        self.ui.cancelButton.clicked.connect(self.close)
    def showEvent(self, event):
        EditDialog(self, "Должности").show()


