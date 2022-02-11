from PyQt5 import QtWidgets
from PyQt5.Qt import Qt
from DocAccounting.views.ui.ui_docs_acc_read_dialog import Ui_DocsAccReadDialog
class DocsAccReadDialog(QtWidgets.QWidget):
    """
    Класс диалога Учет документов - Просмотр
    """
    def __init__(self):
        """
        Конструктор
        """
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_DocsAccReadDialog()
        # Start UI
        self.ui.setupUi(self)
        self.setup()

    def setup(self):
        self.ui.cancelButton.clicked.connect(self.close)



