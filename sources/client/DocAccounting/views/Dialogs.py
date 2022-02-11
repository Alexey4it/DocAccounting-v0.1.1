from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QDateTime
from DocAccounting.views.Globals import Globals
from PyQt5.QtWidgets import QMessageBox

class MainDialog(object):
    """ Класс"""
    def __init__(self, mainDialog, dialog):
        """
        Конструктор
        :param mainDialog:Диалог отображения таблиц
        :param dialog: Диалог (add, update, delete)
        """
        self.dialog = dialog
        self.mainDialog = mainDialog
        if hasattr(self.mainDialog.ui, "addButton"):# если атрибут существует
            self.mainDialog.ui.addButton.clicked.connect(self.addButtonEvent)# Привязка событий к методам обработки
        if hasattr(self.mainDialog.ui, "updateButton"):
            self.mainDialog.ui.updateButton.clicked.connect(self.updateButtonEvent)# Привязка событий к методам обработки
        if hasattr(self.dialog.ui, "okButton"):# если атрибут существует
            # Привязка событий к методам обработки
            self.dialog.ui.okButton.clicked.connect(self.okButtonEvent)# Привязка событий к методам обработки
        if hasattr(self.mainDialog.ui, "delButton"):# если атрибут существует
            # Привязка событий к методам обработки
            self.mainDialog.ui.delButton.clicked.connect(self.delButtonEvent)# Привязка событий к методам обработки
        if hasattr(self.mainDialog.ui, "readButton"):# если атрибут существует
            # Привязка событий к методам обработки
            self.mainDialog.ui.readButton.clicked.connect(self.updateButtonEvent)# Привязка событий к методам обработки
    def delButtonEvent(self):
        """
        Обработка кнопки удаление
        :return:
        """
        items = self.mainDialog.ui.tableWidget.selectedItems() # Значения выделенной строки в таблице
        code = int(items[0].text()) # Значения кода
        self.databaseDialog = DatabaseDialog(self.mainDialog) # Создание объекта класса "База данных - диалог"
        try: # Обработка исключения
            result = self.databaseDialog.delData(code) # Удаление записи в базе данных
        except Exception as e:
            return
        if result == "del": # Если успешно удалено выводим сообщение
            self.msgBox = QMessageBox()
            self.msgBox.setWindowIcon(QtGui.QIcon(':/icons/icon.png'))
            self.msgBox.setIcon(QMessageBox.Information)
            self.msgBox.setWindowTitle("Успешно")
            self.msgBox.setText("Удалено")
            self.msgBox.show()
            self.dialog.close()
            self.databaseDialog.show()
    def addButtonEvent(self):
        """
        Обработка кнопки добавление
        :return:
        """
        self.dialog.ev = "Add" # Строка, показывающая что происходит добавление в таблицу БД
        self.dialog.ui.codeEdit.setEnabled(False) # Компонент код в диалоге делаем неактивным
        for attrib in self.mainDialog.attribs: # Перебираем атрибуты класса таблиц базы данных
            if hasattr(self.dialog.ui, attrib + "Edit"): # Если атрибут в диалоге существует
                value = getattr(self.dialog.ui, attrib + "Edit") # Получаем значение
                value.setText("") # Очищаем компонент, сохраняя значение пустой строки
        self.dialog.show() # Показываем диалог на экране
    def updateButtonEvent(self):
        self.dialog.ev = "Update"# Строка, показывающая что происходит добавление в таблицу БД
        self.dialog.ui.codeEdit.setEnabled(False)# Компонент код в диалоге делаем неактивным
        try: # Обработки исключения
            items = self.mainDialog.ui.tableWidget.selectedItems()# Значения выделенной строки в таблице
            if len(items) == 0:
                return
        except Exception as e:
            print(e)
            return
        count = 0
        for attrib in self.mainDialog.attribs:# Перебираем атрибуты класса таблиц базы данных
            # Заполняем диалог значенями из строки таблиц в диалоге
            if hasattr(self.dialog.ui, attrib + "Edit"):
                value = getattr(self.dialog.ui, attrib + "Edit")
                value.setText(items[count].text())
            if hasattr(self.dialog.ui, attrib + "DateTimeEdit"):
                value = getattr(self.dialog.ui, attrib + "DateTimeEdit")
                dateTime = QDateTime.fromString(items[count].text(), "yyyy-MM-dd HH:mm:ss")
                value.setDateTime(dateTime)
            if hasattr(self.dialog.ui, attrib + "SpinBox"):
                value = getattr(self.dialog.ui, attrib + "SpinBox")
                value.setValue(int(items[count].text()))
            if hasattr(self.dialog.ui, attrib + "ComboBox"):
                value = getattr(self.dialog.ui, attrib + "ComboBox")
                for index in range(value.count()):
                    value.setCurrentIndex(index)
                    comboBoxValue = value.currentText().split('-')[0]
                    if int(comboBoxValue) == int(items[count].text()):
                        break
            count += 1
        self.dialog.show()
    def okButtonEvent(self):
        """
        Обработка клика по кнопке OK
        :return:
        """
        self.databaseDialog = DatabaseDialog(self.mainDialog) # Создание объекта класса "База данных - диалог"
        if self.dialog.ev == "Add": # Если выбранод добавить
            values = []
            # Смотрим атрибуты, сохраняя значения в values
            for attrib in self.mainDialog.attribs:
                if hasattr(self.dialog.ui, attrib + "Edit"):
                    at = getattr(self.dialog.ui, attrib + "Edit")
                    values += [[attrib, at.text()]]
                if hasattr(self.dialog.ui, attrib + "ComboBox"):
                    at = getattr(self.dialog.ui, attrib + "ComboBox")
                    values += [[attrib, int(at.currentText().split('-')[0])]]
                if hasattr(self.dialog.ui, attrib + "SpinBox"):
                    at = getattr(self.dialog.ui, attrib + "SpinBox")
                    values += [[attrib, at.text()]]
                if hasattr(self.dialog.ui, attrib + "DateTimeEdit"):
                    at = getattr(self.dialog.ui, attrib + "DateTimeEdit")
                    values += [[attrib, at.text()]]
                if attrib == "docs":
                    values += [[attrib, self.mainDialog.fileBytes]]
            # Добавляем значения в базу данных
            result = self.databaseDialog.addData(values)
            if result == "add": # Если успешно, то выводим сообщение
                self.msgBox = QMessageBox()
                self.msgBox.setWindowIcon(QtGui.QIcon(':/icons/icon.png'))
                self.msgBox.setIcon(QMessageBox.Information)
                self.msgBox.setWindowTitle("Успешно")
                self.msgBox.setText("Данные добавлены")
                self.msgBox.show()
                self.dialog.close()
                self.databaseDialog.show()

        if self.dialog.ev == "Update": # Если выбрано в диалоге обновить, то перебираем
            # все значения и обновляем выбранную запись в базу данных согласно изменным значениям
            values = []
            for attrib in self.mainDialog.attribs:
                if hasattr(self.dialog.ui, attrib + "Edit"):
                    at = getattr(self.dialog.ui, attrib + "Edit")
                    values += [[attrib, at.text()]]
                if hasattr(self.dialog.ui, attrib + "ComboBox"):
                    at = getattr(self.dialog.ui, attrib + "ComboBox")
                    values += [[attrib, int(at.currentText().split('-')[0])]]
                if hasattr(self.dialog.ui, attrib + "SpinBox"):
                    at = getattr(self.dialog.ui, attrib + "SpinBox")
                    values += [[attrib, at.text()]]
                if hasattr(self.dialog.ui, attrib + "DateTimeEdit"):
                    at = getattr(self.dialog.ui, attrib + "DateTimeEdit")
                    values += [[attrib, at.text()]]
            result = self.databaseDialog.updateData(values)
            if result == "update": # Если успешно, то выводим сообщение
                self.msgBox = QMessageBox()
                self.msgBox.setWindowIcon(QtGui.QIcon(':/icons/icon.png'))
                self.msgBox.setIcon(QMessageBox.Information)
                self.msgBox.setWindowTitle("Успешно")
                self.msgBox.setText("Данные добавлены")
                self.msgBox.show()
                self.dialog.close()
                self.databaseDialog.show()
class EditDialog(object):
    """
    Класс редактирования (один для всех диалогов)
    """
    def __init__(self, dialog, tableName):
        """
        Конструктор
        :param dialog: объект диалога редактирования
        :param tableName: Название таблицы
        """
        self.dialog = dialog
        self.tableName = tableName
    def show(self):
        self.dialog.tableName = self.tableName
        # Редактируем название диалога
        if self.dialog.ev == "Add":
            self.dialog.setWindowTitle(self.tableName + " - Добавление")
        if self.dialog.ev == "Update":
            self.dialog.setWindowTitle(self.tableName + " - Обновление")

class DatabaseDialog(object):
    """Класс база данных - диалог"""
    def __init__(self, parent):
        """
        Конструктор
        :param parent: объект диалога отображения таблиц
        """
        self.parent = parent
        self.Clazz = parent.Clazz
        self.attribs = parent.attribs
        self.dbModel = parent.dbModel
    def show(self):
        if self.dbModel.connectionToDatabase(# Подключаемся к базе данных
                Globals.databaseToolsDialog.ui.dialectEdit.text(),
                Globals.databaseToolsDialog.ui.userNameEdit.text(),
                Globals.databaseToolsDialog.ui.passwordEdit.text(),
                Globals.databaseToolsDialog.ui.hostEdit.text(),
                Globals.databaseToolsDialog.ui.portEdit.text(),
                Globals.databaseToolsDialog.ui.databaseEdit.text()
        ) == "connected":
            clazzs = self.dbModel.showTables(self.Clazz) # Получаем все значения определенного класса таблиц базы данных
            self.showTables(clazzs) # Отображаем значения в таблице диалога
            return "connected"
        else:
            return "disconnected"
    def showTables(self, results):
        """
        Вывод таблиц из базы данных в таблицы диалога
        :param results:
        :return:
        """
        if hasattr(self.parent.ui, "tableWidget"):
            self.parent.ui.tableWidget.setRowCount(0)
            for result in results:
                row_position = self.parent.ui.tableWidget.rowCount()
                self.parent.ui.tableWidget.insertRow(row_position)
                count = 0
                for attrib in self.attribs:
                    self.parent.ui.tableWidget.setItem(row_position, count,
                                                QtWidgets.QTableWidgetItem(str(getattr(result, attrib))))
                    count += 1
    def addData(self, values):
        """
        Добавление данных из диалога в базу данных
        :param values:
        :return:
        """
        result = self.dbModel.addData(self.Clazz, values)
        if result == "error":
            self.msgBox = QMessageBox()
            self.msgBox.setWindowIcon(QtGui.QIcon(':/icons/icon.png'))
            self.msgBox.setIcon(QMessageBox.Information)
            self.msgBox.setWindowTitle("Ошибка")
            self.msgBox.setText("Ошибка добавления таблиц в базу данных")
            self.msgBox.show()
        return result
    def updateData(self, values):
        """
        Обновление данных из диалога в базу данных
        :param values:
        :return:
        """
        result = self.dbModel.updateData(self.Clazz, values)
        if result == "error":
            self.msgBox = QMessageBox()
            self.msgBox.setWindowIcon(QtGui.QIcon(':/icons/icon.png'))
            self.msgBox.setIcon(QMessageBox.Information)
            self.msgBox.setWindowTitle("Ошибка")
            self.msgBox.setText("Ошибка добавления таблиц в базу данных")
            self.msgBox.show()
        return result
    def delData(self, code):
        """
        Удаление записи базы данных
        :param code:
        :return:
        """
        result = self.dbModel.delData(self.Clazz, code)
        if result == "error":
            self.msgBox = QMessageBox()
            self.msgBox.setWindowIcon(QtGui.QIcon(':/icons/icon.png'))
            self.msgBox.setIcon(QMessageBox.Information)
            self.msgBox.setWindowTitle("Ошибка")
            self.msgBox.setText("Ошибка удаления таблиц из базы данных")
            self.msgBox.show()
        return result
    def searchData(self, code):
        """
        Поиск записи в базе данных
        :param code:
        :return:
        """
        result = self.dbModel.searchData(self.Clazz, code)
        return result