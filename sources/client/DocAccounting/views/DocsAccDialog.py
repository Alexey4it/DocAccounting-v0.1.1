from PyQt5 import QtWidgets
from PyQt5.Qt import Qt
from DocAccounting.views.ui.ui_docs_acc_dialog import Ui_DocsAccDialog
from DocAccounting.views.DocsAccReadDialog import DocsAccReadDialog
from DocAccounting.views.Dialogs import DatabaseDialog
from DocAccounting.database.docaccounting_db_classes import Doc, CategoryDoc, ViewDoc, Employee, StatusDoc, Developer, Source
from DocAccounting.models.DatabaseModel import DatabaseModel
from DocAccounting.views.Dialogs import MainDialog
class DocsAccDialog(QtWidgets.QWidget):
    """
    Класс диалога Учет документов
    """
    def __init__(self):
        """
        Конструктор
        """
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_DocsAccDialog()
        self.docsAccReadDialog = DocsAccReadDialog()
        # Start UI
        self.ui.setupUi(self)
        self.editDialog = MainDialog(self, self.docsAccReadDialog)
        self.ui.readButton.clicked.connect(self.readButtonEvent)
        self.setup()

    def setValues(self, obj):
        categores = self.dbModel.showTables(CategoryDoc)
        values = ["{0} - {1}".format(category.code, category.title) for category in categores]
        obj.ui.category_codeComboBox.clear()
        for value in values:
            obj.ui.category_codeComboBox.addItem(value)
        viewCodes = self.dbModel.showTables(ViewDoc)
        values = ["{0} - {1}".format(viewCode.code, viewCode.title) for viewCode in viewCodes]
        obj.ui.view_codeComboBox.clear()
        for value in values:
            obj.ui.view_codeComboBox.addItem(value)
        employees = self.dbModel.showTables(Employee)
        values = ["{0} - {1}".format(employee.code, employee.allnames) for employee in employees]
        obj.ui.employee_codeComboBox.clear()
        for value in values:
            obj.ui.employee_codeComboBox.addItem(value)
        statuses = self.dbModel.showTables(StatusDoc)
        values = ["{0} - {1}".format(status.code, status.title) for status in statuses]
        obj.ui.status_codeComboBox.clear()
        for value in values:
            obj.ui.status_codeComboBox.addItem(value)
        developers = self.dbModel.showTables(Developer)
        values = ["{0} - {1}".format(developer.code, developer.title) for developer in developers]
        obj.ui.developer_codeComboBox.clear()
        for value in values:
            obj.ui.developer_codeComboBox.addItem(value)
        sources = self.dbModel.showTables(Source)
        values = ["{0} - {1}".format(source.code, source.title) for source in sources]
        obj.ui.source_codeComboBox.clear()
        for value in values:
            obj.ui.source_codeComboBox.addItem(value)
    def setup(self):
        self.ui.cancelButton.clicked.connect(self.close)
        self.dbModel = DatabaseModel()
    def showEvent(self, event):
        self.Clazz = Doc
        self.attribs = ["code", "category_code", "view_code", "employee_code", "status_code",
                    "developer_code", "source_code", "title", "date_loading", "date_change", "barcode",
                    "keywords", "section_number", "pages", "copy_n", "cupboard", "rack", "description",
                    "docs", "docs_ext", "sizeMB"]
        self.databaseDialog = DatabaseDialog(self)
        self.databaseDialogResult = self.databaseDialog.show()
    def readButtonEvent(self):
        self.setValues(self.docsAccReadDialog)
        self.editDialog.updateButtonEvent()


