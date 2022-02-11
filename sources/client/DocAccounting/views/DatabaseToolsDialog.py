from PyQt5 import QtWidgets, QtGui
from DocAccounting.views.ui.ui_docs_database_tools_dialog import Ui_DatabaseToolsDialog
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from PyQt5.QtWidgets import QMessageBox
import os
import pickle
class DatabaseToolsDialog(QtWidgets.QWidget):
    """
    Класс диалога Настроек базы данных
    """
    def __init__(self):
        """
        Конструктор
        """
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_DatabaseToolsDialog()
        # Start UI
        self.ui.setupUi(self)
        self.setup()
    def setup(self):
        self.ui.cancelButton.clicked.connect(self.close)
        self.dialect = "mysql+mysqlconnector"
        self.username = "root"
        self.password = "root"
        self.host = "localhost"
        self.port = "3306"
        self.database = "DocAccountingDB"
        self.ui.dialectEdit.setText(self.dialect)
        self.ui.userNameEdit.setText(self.username)
        self.ui.passwordEdit.setText(self.password)
        self.ui.hostEdit.setText(self.host)
        self.ui.portEdit.setText(self.port)
        self.ui.databaseEdit.setText(self.database)
        self.showEvent(None)
        self.connection = '{0}://{1}:{2}@{3}:{4}/{5}'.format(
            self.ui.dialectEdit.text(),
            self.ui.userNameEdit.text(),
            self.ui.passwordEdit.text(),
            self.ui.hostEdit.text(),
            self.ui.portEdit.text(),
            self.ui.databaseEdit.text()
        )
        self.ui.testConnectionButton.clicked.connect(self.connectToDatabase)
        self.ui.saveButton.clicked.connect(self.saveButtonClicked)
    def saveButtonClicked(self):
        """
        Сохранение настроек в файл
        :return:
        """
        dbTools = [
            self.ui.dialectEdit.text(),
            self.ui.userNameEdit.text(),
            self.ui.passwordEdit.text(),
            self.ui.hostEdit.text(),
            self.ui.portEdit.text(),
            self.ui.databaseEdit.text()
        ]
        fp = open('tools.bin', 'wb')
        pickle.dump(dbTools, fp)
        fp.close()
        self.msgBox = QMessageBox()
        self.msgBox.setWindowIcon(QtGui.QIcon(':/icons/icon.png'))
        self.msgBox.setIcon(QMessageBox.Information)
        self.msgBox.setWindowTitle("Успешно")
        self.msgBox.setText("Настройки сохранены")
        self.msgBox.show()
    def connectToDatabase(self):
        """
        Подключение к базе данных
        :return:
        """
        self.connection = '{0}://{1}:{2}@{3}:{4}/{5}'.format(
            self.ui.dialectEdit.text(),
            self.ui.userNameEdit.text(),
            self.ui.passwordEdit.text(),
            self.ui.hostEdit.text(),
            self.ui.portEdit.text(),
            self.ui.databaseEdit.text()
        )
        self.msgBox = QMessageBox()
        self.msgBox.setWindowIcon(QtGui.QIcon(':/icons/icon.png'))
        self.msgBox.setIcon(QMessageBox.Information)
        try:
            engine = create_engine(self.connection)
            Session = sessionmaker(bind=engine)
            engine.connect()
            self.msgBox.setWindowTitle("Успешно")
            self.msgBox.setText("Подключение установлено...")
        except Exception as e:
            self.msgBox.setWindowTitle("Ошибка")
            self.msgBox.setText("Нет подключения к базе данных")
        self.msgBox.show()
    def showEvent(self,event):
        """
        Показ формы на экране
        :param event:
        :return:
        """
        if os.path.exists('tools.bin'): # Загрузка настроек из файла
            fp = open('tools.bin', 'rb')
            dbTools = pickle.load(fp)
            self.ui.dialectEdit.setText(dbTools[0]),
            self.ui.userNameEdit.setText(dbTools[1]),
            self.ui.passwordEdit.setText(dbTools[2]),
            self.ui.hostEdit.setText(dbTools[3]),
            self.ui.portEdit.setText(dbTools[4]),
            self.ui.databaseEdit.setText(dbTools[5])

