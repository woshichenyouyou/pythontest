# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/cyy/Test/ImageTools/ImageViewer.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(700, 558)
        self.pushButton_OpenImage = QtWidgets.QPushButton(Form)
        self.pushButton_OpenImage.setGeometry(QtCore.QRect(10, 530, 80, 22))
        self.pushButton_OpenImage.setObjectName("pushButton_OpenImage")
        self.graphicsView__Image = QtWidgets.QGraphicsView(Form)
        self.graphicsView__Image.setGeometry(QtCore.QRect(10, 10, 681, 511))
        self.graphicsView__Image.setObjectName("graphicsView__Image")
        self.pushButton_Close = QtWidgets.QPushButton(Form)
        self.pushButton_Close.setGeometry(QtCore.QRect(610, 530, 80, 22))
        self.pushButton_Close.setObjectName("pushButton_Close")
        self.label_Path = QtWidgets.QLabel(Form)
        self.label_Path.setGeometry(QtCore.QRect(110, 530, 241, 16))
        self.label_Path.setObjectName("label_Path")

        self.retranslateUi(Form)
        self.pushButton_Close.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "ImageViewer"))
        self.pushButton_OpenImage.setText(_translate("Form", "Open"))
        self.pushButton_Close.setText(_translate("Form", "Close"))
        self.label_Path.setText(_translate("Form", "NA"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

