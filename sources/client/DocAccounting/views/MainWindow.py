from PyQt5 import QtWidgets, QtGui
from DocAccounting.views.ui.ui_main_window import Ui_MainWindow
from DocAccounting.views.AboutDialog import AboutDialog
from DocAccounting.views.EmployeesDialog import EmployeesDialog
from DocAccounting.views.StatusDocsDialog import StatusDocsDialog
from DocAccounting.views.PositionsDialog import PositionsDialog
from DocAccounting.views.DevelopersDialog import DevelopersDialog
from DocAccounting.views.SourcesDialog import SourcesDocsDialog
from DocAccounting.views.CategoryDocsDialog import CategoryDocsDialog
from DocAccounting.views.DocsAccDialog import DocsAccDialog
from DocAccounting.views.DocsDownloadDialog import DocsDownloadDialog
from DocAccounting.views.DocsUploadDialog import DocsUploadDialog
from DocAccounting.views.DatabaseToolsDialog import DatabaseToolsDialog
from DocAccounting.views.DocsRegulationDialog import DocsRegulationDialog
from DocAccounting.views.DepartmentsDialog import DepartmentsDialog
from DocAccounting.views.ViewDocsDialog import ViewDocsDialog
from DocAccounting.views.DocsChangeDialog import DocsChangeDialog
from DocAccounting.settings import getVersion
from PyQt5.QtWidgets import QMessageBox
from DocAccounting.views.Globals import Globals
from DocAccounting.models.DatabaseModel import DatabaseModel
from DocAccounting.views.WindowStylesDialog import WindowStylesDialog
import os.path
import pickle
class MainWindowView(QtWidgets.QMainWindow):

    """Главное окно приложения"""
    def __init__(self, app):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_MainWindow()
        self.databaseToolsDialog = DatabaseToolsDialog()
        Globals.databaseToolsDialog = self.databaseToolsDialog
        self.aboutDialog = AboutDialog()
        self.employeesDialog = EmployeesDialog()
        self.statusDocsDialog = StatusDocsDialog()
        self.positionsDialog = PositionsDialog()
        self.developersDialog = DevelopersDialog()
        self.sourcesDialog = SourcesDocsDialog()
        self.categoryDocsDialog = CategoryDocsDialog()
        self.docsAccDialog = DocsAccDialog()
        self.docsDownloadDialog = DocsDownloadDialog()
        self.docsUploadDialog = DocsUploadDialog()
        self.docsRegulationDialog = DocsRegulationDialog()
        self.windowStylesDialog = WindowStylesDialog(app)
        self.departmentsDialog = DepartmentsDialog()
        self.viewDocsDialog = ViewDocsDialog()
        self.docsChangeDialog = DocsChangeDialog()
        if os.path.exists('styles.bin'):
            fp = open('styles.bin', 'rb')
            styles = pickle.load(fp)
            if styles[0] == "system":
                self.windowStylesDialog.ui.systemRadioButton.setChecked(True)
            if styles[0] == "dark":
                self.windowStylesDialog.ui.darkRadioButton.setChecked(True)
            if styles[0] == "light":
                self.windowStylesDialog.ui.lightRadioButton.setChecked(True)
            fp.close()
            self.windowStylesDialog.changeStyle()

        # Start UI
        self.ui.setupUi(self)
        self.setup()
    def setup(self):
        self.setWindowTitle("DocAccounting (ИС учёта документов) - Версия " + getVersion())
        self.ui.appLabel.setText("DocAccounting (ИС учёта документов)\nВерсия " + getVersion())
        self.ui.closeAction.triggered.connect(self.close)
        self.ui.aboutAction.triggered.connect(self.aboutDialog.show)
        self.ui.employeeAction.triggered.connect(self.employeesDialog.show)
        self.ui.positionsAction.triggered.connect(self.positionsDialog.show)
        self.ui.developersAction.triggered.connect(self.developersDialog.show)
        self.ui.statusDocAction.triggered.connect(self.statusDocsDialog.show)
        self.ui.sourcesAction.triggered.connect(self.sourcesDialog.show)
        self.ui.categoryDocsAction.triggered.connect(self.categoryDocsDialog.show)
        self.ui.docsAccAction.triggered.connect(self.docsAccDialog.show)
        self.ui.docsDownloadAction.triggered.connect(self.docsDownloadDialog.show)
        self.ui.docsUploadAction.triggered.connect(self.docsUploadDialog.show)
        self.ui.databaseToolsAction.triggered.connect(self.databaseToolsDialog.show)
        self.ui.docsRegulationAction.triggered.connect(self.docsRegulationDialog.show)
        self.ui.valuesDatabaseAction.triggered.connect(self.valuesDatabase)
        self.ui.windowStyleAction.triggered.connect(self.windowStylesDialog.show)
        self.ui.departmentAction.triggered.connect(self.departmentsDialog.show)
        self.ui.viewDocsAction.triggered.connect(self.viewDocsDialog.show)
        self.ui.docsChangeAction.triggered.connect(self.docsChangeDialog.show)

    def showEvent(self, event):
        pass
    def closeEvent(self, event):
        pass
    def valuesDatabase(self):
        self.msgBox = QMessageBox()
        self.msgBox.setWindowIcon(QtGui.QIcon(':/icons/icon.png'))
        self.msgBox.setIcon(QMessageBox.Question)
        self.msgBox.setWindowTitle("Успешно")
        self.msgBox.setText("Таблицы заполнены")
        result = self.msgBox.question(self, "Очистка и заполнение таблиц", "Очистить и заполнить таблицы БД ?", self.msgBox.Yes | self.msgBox.No)
        if result == self.msgBox.Yes:
            self.dbModel = DatabaseModel()
            result = self.dbModel.connectionToDatabase(
                Globals.databaseToolsDialog.ui.dialectEdit.text(),
                Globals.databaseToolsDialog.ui.userNameEdit.text(),
                Globals.databaseToolsDialog.ui.passwordEdit.text(),
                Globals.databaseToolsDialog.ui.hostEdit.text(),
                Globals.databaseToolsDialog.ui.portEdit.text(),
                Globals.databaseToolsDialog.ui.databaseEdit.text()
            )
            if result == "error connecting":
                QMessageBox().information(self, "Ошибка подключения", "Ошибка подключения")
                return
            self.dbModel.setValuesDatabase()
        else:
            pass
        self.msgBox.show()
