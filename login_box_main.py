from login_box import Ui_Form
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc

class LoginWindow(qtw.QWidget, Ui_Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # passing any arguments

        self.setupUi(self)

        self.pushButton.clicked.connect(self.authenticate)

    def authenticate(self):
        username = self.lineEditUserName.text()
        password = self.lineEditPassword.text()

        if username == 'user' and password == 'pass':
            qtw.QMessageBox.information(self, 'Success', 'You are now logged in')
        else:
            qtw.QMessageBox.critical(self, 'Error', 'Failed to login')


if __name__ == '__main__':
    app = qtw.QApplication([])

    widget = LoginWindow()
    widget.show()

    app.exec_()
