from PyQt5 import QtWidgets, QtGui
from DocAccounting.views.ui.ui_window_styles_dialog import Ui_WindowStylesDialog
from qt_material import apply_stylesheet
from PyQt5.QtWidgets import QMessageBox
import pickle
class WindowStylesDialog(QtWidgets.QWidget):
    """
    Класс диалога Стили окон
    """
    def __init__(self, app):
        """
        Конструктор
        """
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_WindowStylesDialog()
        self.app = app
        # Start UI
        self.ui.setupUi(self)
        self.setup()

    def setup(self):
        self.ui.cancelButton.clicked.connect(self.close)
        self.ui.okButton.clicked.connect(self.okButtonClicked)
    def changeStyle(self):
        """
        Изменение стиля диалога
        :return:
        """
        self.styles = []
        if self.ui.systemRadioButton.isChecked():
            self.styles += ['system', self.ui.systemRadioButton.isChecked()]
        if self.ui.darkRadioButton.isChecked():
            apply_stylesheet(self.app, theme='dark_red.xml')
            self.styles += ['dark', self.ui.darkRadioButton.isChecked()]
        if self.ui.lightRadioButton.isChecked():
            apply_stylesheet(self.app, theme='light_red.xml')
            self.styles += ['light', self.ui.lightRadioButton.isChecked()]
    def okButtonClicked(self):
        self.changeStyle()
        fp = open('styles.bin', 'wb')
        pickle.dump(self.styles, fp)# Сохранение настроек стилей окон в файл
        fp.close()
        if self.styles[0] == "system":
            self.msgBox = QMessageBox()
            self.msgBox.setWindowIcon(QtGui.QIcon(':/icons/icon.png'))
            self.msgBox.setIcon(QMessageBox.Information)
            self.msgBox.setWindowTitle("Изменение стиля окна")
            self.msgBox.setText("Системный стиль будет применен после перезапуска программы")
            self.msgBox.show()
        self.close()



