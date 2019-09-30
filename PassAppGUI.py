import sys
from PyQt5 import QtWidgets,QtGui
import json
import os

class PassGUI(QtWidgets.QWidget):

    def __init__(self):
        super().__init__() #call the constructor of QtWidgets

        self.init_ui() #constructor for our UI
        

    def init_ui(self): #everything inside the window
        self.setGeometry(50,50,600,150)
        font = QtGui.QFont()
        font.setPointSize(16)

        #create username field
        self.usernameEdit = QtWidgets.QLineEdit()
        self.usernameLabel = QtWidgets.QLabel('Username')
        self.usernameLabel.setFont(font)
        self.usernameEdit.move(150,20)

        #create password field
        self.passwordEdit = QtWidgets.QLineEdit()
        self.passwordLabel = QtWidgets.QLabel('Password')
        self.passwordLabel.setFont(font)

        #create website/app field
        self.websiteEdit = QtWidgets.QLineEdit()
        self.websiteLabel = QtWidgets.QLabel('Website/App')
        self.websiteLabel.setFont(font)

        self.submit = QtWidgets.QPushButton('Submit')
        
        #lay out the username fields
        h_box_username = QtWidgets.QHBoxLayout()
        h_box_username.addStretch()
        h_box_username.addWidget(self.usernameEdit)
        h_box_username.addWidget(self.usernameLabel)
        h_box_username.addStretch()

        #layout the password fields
        h_box_password = QtWidgets.QHBoxLayout()
        h_box_password.addStretch()
        h_box_password.addWidget(self.passwordEdit)
        h_box_password.addWidget(self.passwordLabel)
        h_box_password.addStretch()

        #layout the website fields
        h_box_website = QtWidgets.QHBoxLayout()
        h_box_website.addStretch()
        h_box_website.addWidget(self.websiteEdit)
        h_box_website.addWidget(self.websiteLabel)
        h_box_website.addStretch()

        h_box_submit = QtWidgets.QHBoxLayout()
        h_box_submit.addStretch()
        h_box_submit.addWidget(self.submit)
        h_box_submit.addStretch()

        #create vertical alignment for inputs
        v_box_input = QtWidgets.QVBoxLayout()
        v_box_input.addLayout(h_box_username)
        v_box_input.addLayout(h_box_password)
        v_box_input.addLayout(h_box_website)
        v_box_input.addLayout(h_box_submit)

        self.setLayout(v_box_input)
        
        self.setWindowTitle('Passwords')
        
        information = self.read_passwords('passwords.json')
        self.convert_to_labels(information,v_box_input)

        self.submit.clicked.connect(lambda:self.btn_click(v_box_input,information))
        

    def get_information(self,info):
        username = self.usernameEdit.text()
        password = self.passwordEdit.text()
        website = self.websiteEdit.text()
        if username == '' or password == '' or website == '':
            return None
        else:
            info[website] = [username,password]
            return username,password,website

    def add_label(self,user_info):
        self.usernameLabel = QtWidgets.QLabel('Username: %s ' % (user_info[0]))
        self.passwordLabel = QtWidgets.QLabel('Password: %s' % (user_info[1]))
        self.websiteLabel = QtWidgets.QLabel('Website: %s' % (user_info[2]))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.usernameLabel.setFont(font)
        self.passwordLabel.setFont(font)
        self.websiteLabel.setFont(font)
        h_box = QtWidgets.QHBoxLayout()
        h_box.addWidget(self.usernameLabel)
        h_box.addWidget(self.passwordLabel)
        h_box.addWidget(self.websiteLabel)
        return h_box

    def btn_click(self,vertical_box,info):
        try:
            h_box=self.add_label(self.get_information(info))
            vertical_box.addLayout(h_box)
            self.save_passwords(info,'passwords.json')
        except TypeError:
            pass
        self.usernameEdit.setText('')
        self.passwordEdit.setText('')
        self.websiteEdit.setText('')
        


    def read_passwords(self,filename):
        if os.path.exists(filename):
            with open(filename) as file:
                return json.load(file)
        else:
            data = {}
            with open(filename,'w') as outfile:
                json.dump(data,outfile)
            return data
    
    def save_passwords(self,data,filename):
        with open(filename,'w') as file:
            json.dump(data,file)
    
    def convert_to_labels(self,info,vertical_box):
        try:
            for k,v in info.items():
                user_data = (v[0],v[1],k)
                h_box = self.add_label(user_data)
                vertical_box.addLayout(h_box)
        except:
            pass




app = QtWidgets.QApplication(sys.argv)
a_window = PassGUI()
a_window.show()
sys.exit(app.exec_())



