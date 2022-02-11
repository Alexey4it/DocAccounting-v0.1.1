from PyQt5 import QtWidgets
from PyQt5.Qt import Qt
from DocAccounting.views.ui.ui_employees_dialog import Ui_EmployeesDialog
from DocAccounting.views.Dialogs import MainDialog
from DocAccounting.views.EmployeesEditDialog import EmployeesEditDialog
from DocAccounting.models.DatabaseModel import DatabaseModel
from DocAccounting.database.docaccounting_db_classes import Employee, Position, Department
from DocAccounting.views.Globals import Globals
from DocAccounting.views.Dialogs import DatabaseDialog
class EmployeesDialog(QtWidgets.QWidget):
    """
    Класс диалога Сотрудники
    """
    def __init__(self):
        """
        Конструктор
        """
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_EmployeesDialog()
        self.employeesEditDialog = EmployeesEditDialog()
        # Start UI
        self.ui.setupUi(self)
        self.editDialog = MainDialog(self, self.employeesEditDialog)
        self.ui.addButton.clicked.connect(self.addButtonEvent)
        self.ui.updateButton.clicked.connect(self.updateButtonEvent)
        self.setup()
    def setValues(self):
        positions = self.dbModel.showTables(Position)
        values = ["{0} - {1}".format(position.code, position.title) for position in positions]
        self.employeesEditDialog.ui.positions_codeComboBox.clear()
        for value in values:
            self.employeesEditDialog.ui.positions_codeComboBox.addItem(value)
        departments = self.dbModel.showTables(Department)
        values = ["{0} - {1}".format(department.code, department.title) for department in departments]
        self.employeesEditDialog.ui.departments_codeComboBox.clear()
        for value in values:
            self.employeesEditDialog.ui.departments_codeComboBox.addItem(value)

    def addButtonEvent(self):
        self.setValues()
        self.editDialog.addButtonEvent()
    def updateButtonEvent(self):
        self.setValues()
        self.editDialog.updateButtonEvent()
    def setup(self):
        self.ui.cancelButton.clicked.connect(self.close)
        self.dbModel = DatabaseModel()
    def showEvent(self, event):
        self.Clazz = Employee
        self.attribs = ["code", "positions_code",
                        "departments_code", "allnames", "email", "login",
                        "password", "editable", "reading"]
        self.databaseDialog = DatabaseDialog(self)
        self.databaseDialog.show()





