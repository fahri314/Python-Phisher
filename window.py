# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

__author__ = 'Fahri Güreşçi'
__version__ = '1.0'

# The Python Phisher application sends a spoofed mail to the destination, allowing it to point to the desired fake url address.
# Copyright (C) (2017)

# Python Phisher is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.

# Python Phisher is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301  USA

# WARNING
# This was written for educational purpose and pentest only. Use it at your own risk.
# Please remember... your action will be logged in target system...
# Author will not be responsible for any damage !!
# Use it with your own risk

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import sys
from view import Ui_MainWindow
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QFileDialog

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def view(self):
        self.viewWindow = QtGui.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.viewWindow)
        self.ui.textEdit.setStyleSheet("background-color: #FFFFDD;")
        self.ui.textEdit.setText(self.worker.html)
        self.viewWindow.show()

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.setFixedSize(423, 221)
        Form.setStyleSheet(_fromUtf8("plastique"))
        self.tabWidget = QtGui.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 401, 201))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(0, 20, 391, 51))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 141, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.groupBox_2 = QtGui.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 70, 391, 51))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 20, 141, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(200, 20, 81, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(300, 20, 91, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.radioButton = QtGui.QRadioButton(self.tab)
        self.radioButton.setGeometry(QtCore.QRect(20, 180, 82, 17))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.checkBox = QtGui.QCheckBox(self.tab)
        self.checkBox.setGeometry(QtCore.QRect(330, 140, 70, 17))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.groupBox_3 = QtGui.QGroupBox(self.tab)
        self.groupBox_3.setGeometry(QtCore.QRect(0, 120, 161, 51))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.lineEdit_3 = QtGui.QLineEdit(self.groupBox_3)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 20, 141, 20))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.groupBox_7 = QtGui.QGroupBox(self.tab)
        self.groupBox_7.setGeometry(QtCore.QRect(160, 120, 161, 51))
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.lineEdit_4 = QtGui.QLineEdit(self.groupBox_7)
        self.lineEdit_4.setGeometry(QtCore.QRect(10, 20, 141, 20))
        self.lineEdit_4.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.groupBox_4 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_4.setGeometry(QtCore.QRect(0, 20, 391, 51))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.lineEdit_5 = QtGui.QLineEdit(self.groupBox_4)
        self.lineEdit_5.setGeometry(QtCore.QRect(10, 20, 141, 20))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.groupBox_5 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_5.setGeometry(QtCore.QRect(0, 70, 391, 51))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.lineEdit_6 = QtGui.QLineEdit(self.groupBox_5)
        self.lineEdit_6.setGeometry(QtCore.QRect(10, 20, 141, 20))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.groupBox_6 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_6.setGeometry(QtCore.QRect(0, 120, 391, 51))
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.lineEdit_7 = QtGui.QLineEdit(self.groupBox_6)
        self.lineEdit_7.setGeometry(QtCore.QRect(10, 20, 141, 20))
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.pushButton_2 = QtGui.QPushButton(self.tab_3)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 60, 81, 41))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.tab_3)
        self.pushButton_3.setGeometry(QtCore.QRect(240, 60, 91, 41))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.pushButton_4 = QtGui.QPushButton(self.tab_4)
        self.pushButton_4.setGeometry(QtCore.QRect(140, 40, 111, 51))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.label_2 = QtGui.QLabel(self.tab_4)
        self.label_2.setGeometry(QtCore.QRect(170, 110, 111, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))

        ui.lineEdit.setText("smtp.gmail.com") # change another services
        ui.lineEdit_2.setText("587")          # change another your service port
        ui.lineEdit_3.setText("")             # your mail
        ui.lineEdit_4.setText("")             # your password
        ui.lineEdit_5.setText("")             # sender
        ui.lineEdit_6.setText("")             # receiver
        ui.lineEdit_7.setText("")             # mail subject

        self.worker = Worker()

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)
        ######################### Button Event ##############################
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.worker.authenticate)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.worker.selectFile)
        self.pushButton_3.clicked.connect(self.view)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.worker.send)
        self.checkBox.setChecked(True)
        #####################################################################

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Python Phisher", None))
        self.groupBox.setTitle(_translate("Form", "Smtp Server", None))
        self.groupBox_2.setTitle(_translate("Form", "Port", None))
        self.pushButton.setText(_translate("Form", "Authenticate", None))
        self.radioButton.setText(_translate("Form", "start-tls", None))
        self.checkBox.setText(_translate("Form", "Start Tls", None))
        self.groupBox_3.setTitle(_translate("Form", "Username", None))
        self.groupBox_7.setTitle(_translate("Form", "Password", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Sending Profiles", None))
        self.groupBox_4.setTitle(_translate("Form", "Sender", None))
        self.groupBox_5.setTitle(_translate("Form", "Receiver", None))
        self.groupBox_6.setTitle(_translate("Form", "Subject", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "E-Mail Tampletes", None))
        self.pushButton_2.setToolTip(_translate("Form", "<html><head/><body><p><br/></p></body></html>", None))
        self.pushButton_2.setText(_translate("Form", "Select File", None))
        self.pushButton_3.setText(_translate("Form", "View", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "Html File Upload", None))
        self.pushButton_4.setText(_translate("Form", "Start", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Form", "Start", None))

class Worker(QtCore.QThread):
    def __init__(self):
        QtCore.QThread.__init__(self)
        self.html = ""

    def authenticate(self):
        server = str(ui.lineEdit.text())
        port = int(ui.lineEdit_2.text())
        try:
            connection = smtplib.SMTP(server, port)
            connection.ehlo()
            ui.label.setText("Success")
        except:  
            ui.label.setText("Fail")

    def selectFile(self):
        filename = QFileDialog.getOpenFileName()
        with open(filename, 'r') as f:
            self.html = f.read()

    def send(self):
        server = str(ui.lineEdit.text())
        port = int(ui.lineEdit_2.text())
        username = str(ui.lineEdit_3.text())
        password = str(ui.lineEdit_4.text())
        sender = str(ui.lineEdit_5.text())
        receiver = str(ui.lineEdit_6.text())
        subject = str(ui.lineEdit_7.text())
        msg = MIMEMultipart('alternative')   
        msg['To'] = receiver
        msg['From'] = sender
        msg['Subject'] = subject
        message1 = MIMEText(self.html, 'html')
        msg.attach(message1)
        message = msg.as_string()

        s = smtplib.SMTP(server, port)
        if ui.checkBox.isChecked():
            s.starttls()
        s.ehlo()
        if server != None and port != None and username != None and password != None and sender != None and receiver != None and subject != None and message != None and self.html != None:
            try:
                s.login(username, password)
                s.sendmail(sender, receiver, message)
                s.quit()
                ui.label_2.setText("Success")
            except:
                ui.label_2.setText("Fail")
        else:
            ui.label_2.setText("Fail")

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("Cleanlooks"))
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

