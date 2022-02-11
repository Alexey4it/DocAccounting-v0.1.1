from PyQt5 import QtWidgets
from PyQt5.Qt import Qt
from DocAccounting.views.ui.ui_departments_dialog import Ui_DepartmentsDialog
from DocAccounting.views.DepartmentsEditDialog import DepartmentsEditDialog
from DocAccounting.views.Dialogs import MainDialog
from DocAccounting.database.docaccounting_db_classes import Department
from DocAccounting.models.DatabaseModel import DatabaseModel
from DocAccounting.views.Dialogs import DatabaseDialog
class DepartmentsDialog(QtWidgets.QWidget):
    """
    Класс диалога Отдел
    """
    def __init__(self):
        """
        Конструктор
        """
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_DepartmentsDialog()
        self.departmentsEditDialog = DepartmentsEditDialog()
        # Start UI
        self.ui.setupUi(self)
        self.editDialog = MainDialog(self, self.departmentsEditDialog)
        self.setup()
    def setup(self):
        self.ui.cancelButton.clicked.connect(self.close)
        self.dbModel = DatabaseModel()
    def showEvent(self, event):
        self.Clazz = Department
        self.attribs = ["code", "title"]
        self.databaseDialog = DatabaseDialog(self)
        self.databaseDialog.show()



