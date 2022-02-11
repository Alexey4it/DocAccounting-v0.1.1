from PyQt5 import QtWidgets
from PyQt5.Qt import Qt
from DocAccounting.views.ui.ui_departments_edit_dialog import Ui_DepartmentsEditDialog
from DocAccounting.views.Dialogs import EditDialog
class DepartmentsEditDialog(QtWidgets.QWidget):
    """
    Класс диалога Отдел - Редактирование
    """
    def __init__(self):
        """
        Конструктор
        """
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_DepartmentsEditDialog()
        # Start UI
        self.ui.setupUi(self)
        self.setup()
    def setup(self):
        self.ui.cancelButton.clicked.connect(self.close)
    def showEvent(self, event):
        EditDialog(self, "Отделы").show()


