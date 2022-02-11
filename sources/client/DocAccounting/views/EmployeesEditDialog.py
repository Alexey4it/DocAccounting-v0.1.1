from PyQt5 import QtWidgets
from PyQt5.Qt import Qt
from DocAccounting.views.ui.ui_employees_edit_dialog import Ui_EmployeesEditDialog
from DocAccounting.views.Dialogs import EditDialog
class EmployeesEditDialog(QtWidgets.QWidget):
    """
    Класс диалога Сотрудники - Редактирование
    """
    def __init__(self):
        """
        Конструктор
        """
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_EmployeesEditDialog()
        # Start UI
        self.ui.setupUi(self)
        self.setup()
    def setup(self):
        self.ui.cancelButton.clicked.connect(self.close)
    def showEvent(self, event):
        EditDialog(self, "Сотрудники").show()


