from PyQt5 import QtWidgets
from PyQt5.Qt import Qt
from DocAccounting.views.ui.ui_about_dialog import Ui_AboutDialog
from DocAccounting.settings import getVersion
class AboutDialog(QtWidgets.QDialog):
    """
    Класс диалога "О программе"
    """
    def __init__(self):
        """
        Конструктор
        """
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_AboutDialog()
        # Start UI
        self.ui.setupUi(self)
        self.setup()
    def setup(self):
        self.ui.aboutLabel.setText("DocAccounting.\nВерсия {0}. {1}.".format(getVersion(), "2022 г"))
        self.ui.okButton.clicked.connect(self.close)

