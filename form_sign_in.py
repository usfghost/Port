# Imports
import requests
from ui.Ui_form_sign_in import Ui_Form
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc

class SignInWindow(qtw.QWidget, Ui_Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # passing any arguments

        self.setupUi(self)
        self.buttonSubmit.clicked.connect(self.authenticate)

    def authenticate(self):
        username = self.editUsername.text()
        password = self.editPassword.text()

        loginres = self.authenticateCreds(username, password)
        if loginres == '-1':
            qtw.QMessageBox.critical(self, 'Error', 'Failed to login')
        else:
            userid = loginres
            qtw.QMessageBox.information(self, 'Success', 'You are now logged in, UserID: ' + userid)

    def authenticateCreds(self, username, password):
        url = 'http://localhost:3000/php/user_authorize.php'
        usercreds = { 'username': username, 'password': password }
        result = requests.post(url, data = usercreds)
        # qtw.QMessageBox.information(self, 'look at this', result.text)
        return result.text

if __name__ == '__main__':
    app = qtw.QApplication([])

    widget = SignInWindow()
    widget.show()

    app.exec_()