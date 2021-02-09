# Imports
from ui.Ui_form_sign_in import Ui_Form
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from URequests import URequests

class SignInWindow(qtw.QWidget, Ui_Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # passing any arguments

        self.setupUi(self)
        self.styleLineEdits()
        self.buttonSubmit.clicked.connect(self.authenticate)

    def styleLineEdits(self):
        self.editEmail.setAttribute(qtc.Qt.WA_MacShowFocusRect, 0)
        self.editPassword.setAttribute(qtc.Qt.WA_MacShowFocusRect, 0)

    def authenticate(self):
        email = self.editEmail.text()
        password = self.editPassword.text()
        userid = getUserId(email, password)
        if userid == -1:
            
            return

if __name__ == '__main__':
    app = qtw.QApplication([])

    widget = SignInWindow()
    widget.show()

    app.exec_()