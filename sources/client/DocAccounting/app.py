from PyQt5 import QtWidgets, QtCore
from DocAccounting.views.MainWindow import MainWindowView
from DocAccounting.views.Globals import Globals
import sqlalchemy.sql.default_comparator
import sys
def my_excepthook(type, value, traceback):
    """Обработка исключений"""
    print('Unhandled error:', type, value)
def DocAccountingApplication():
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_UseSoftwareOpenGL)
    # Создание приложения
    application = QtWidgets.QApplication(sys.argv)
    # Перехват всех исключений
    sys.excepthook = my_excepthook
    # Создание главного окна
    MainWindow = MainWindowView(application)
    MainWindow.show()
    sys.exit(application.exec_())
