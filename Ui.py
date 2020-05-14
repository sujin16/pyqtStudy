# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_Files/calculator.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(380, 460)
        Dialog.setMinimumSize(QtCore.QSize(362, 460))
        Dialog.setMaximumSize(QtCore.QSize(380, 460))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../image/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout_3 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.a_lineEdit = QtWidgets.QLineEdit(self.widget)
        self.a_lineEdit.setMinimumSize(QtCore.QSize(362, 0))
        self.a_lineEdit.setStyleSheet("font: 20pt \"Arial\";")
        self.a_lineEdit.setFrame(False)
        self.a_lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.a_lineEdit.setObjectName("a_lineEdit")
        self.gridLayout.addWidget(self.a_lineEdit, 1, 0, 1, 2)
        self.q_lineEdit = QtWidgets.QLineEdit(self.widget)
        self.q_lineEdit.setMinimumSize(QtCore.QSize(0, 45))
        self.q_lineEdit.setStyleSheet("font: 15pt \"Arial\";")
        self.q_lineEdit.setFrame(False)
        self.q_lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.q_lineEdit.setObjectName("q_lineEdit")
        self.gridLayout.addWidget(self.q_lineEdit, 0, 0, 1, 2)
        self.del_pushButton = QtWidgets.QPushButton(self.widget)
        self.del_pushButton.setMinimumSize(QtCore.QSize(72, 50))
        self.del_pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 146, 96);")
        self.del_pushButton.setText("")
        self.del_pushButton.setObjectName("del_pushButton")
        self.gridLayout.addWidget(self.del_pushButton, 3, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(281, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        self.gridLayout_3.addWidget(self.widget, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setVerticalSpacing(15)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.p_close_pushButton = QtWidgets.QPushButton(Dialog)
        self.p_close_pushButton.setMinimumSize(QtCore.QSize(0, 45))
        self.p_close_pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 9pt \"Arial\";")
        self.p_close_pushButton.setObjectName("p_close_pushButton")
        self.gridLayout_2.addWidget(self.p_close_pushButton, 0, 2, 1, 1)
        self.sign_pushButton_1 = QtWidgets.QPushButton(Dialog)
        self.sign_pushButton_1.setMinimumSize(QtCore.QSize(0, 45))
        self.sign_pushButton_1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 9pt \"Arial\";")
        self.sign_pushButton_1.setObjectName("sign_pushButton_1")
        self.gridLayout_2.addWidget(self.sign_pushButton_1, 0, 3, 1, 1)
        self.num_pushButton_1 = QtWidgets.QPushButton(Dialog)
        self.num_pushButton_1.setMinimumSize(QtCore.QSize(0, 45))
        self.num_pushButton_1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 9pt \"Arial\";")
        self.num_pushButton_1.setObjectName("num_pushButton_1")
        self.gridLayout_2.addWidget(self.num_pushButton_1, 1, 0, 1, 1)
        self.num_pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.num_pushButton_2.setMinimumSize(QtCore.QSize(0, 45))
        self.num_pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 9pt \"Arial\";")
        self.num_pushButton_2.setObjectName("num_pushButton_2")
        self.gridLayout_2.addWidget(self.num_pushButton_2, 1, 1, 1, 1)
        self.reset_pushButton = QtWidgets.QPushButton(Dialog)
        self.reset_pushButton.setMinimumSize(QtCore.QSize(0, 45))
        self.reset_pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 9pt \"Arial\";")
        self.reset_pushButton.setObjectName("reset_pushButton")
        self.gridLayout_2.addWidget(self.reset_pushButton, 0, 0, 1, 1)
        self.p_open_pushButton = QtWidgets.QPushButton(Dialog)
        self.p_open_pushButton.setMinimumSize(QtCore.QSize(0, 45))
        self.p_open_pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 9pt \"Arial\";")
        self.p_open_pushButton.setObjectName("p_open_pushButton")
        self.gridLayout_2.addWidget(self.p_open_pushButton, 0, 1, 1, 1)
        self.num_pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.num_pushButton_3.setMinimumSize(QtCore.QSize(0, 45))
        self.num_pushButton_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 9pt \"Arial\";")
        self.num_pushButton_3.setObjectName("num_pushButton_3")
        self.gridLayout_2.addWidget(self.num_pushButton_3, 1, 2, 1, 1)
        self.num_pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.num_pushButton_4.setMinimumSize(QtCore.QSize(0, 45))
        self.num_pushButton_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 9pt \"Arial\";")
        self.num_pushButton_4.setObjectName("num_pushButton_4")
        self.gridLayout_2.addWidget(self.num_pushButton_4, 2, 0, 1, 1)
        self.num_pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.num_pushButton_5.setMinimumSize(QtCore.QSize(0, 45))
        self.num_pushButton_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 9pt \"Arial\";")
        self.num_pushButton_5.setObjectName("num_pushButton_5")
        self.gridLayout_2.addWidget(self.num_pushButton_5, 2, 1, 1, 1)
        self.num_pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.num_pushButton_6.setMinimumSize(QtCore.QSize(0, 45))
        self.num_pushButton_6.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 9pt \"Arial\";")
        self.num_pushButton_6.setObjectName("num_pushButton_6")
        self.gridLayout_2.addWidget(self.num_pushButton_6, 2, 2, 1, 1)
        self.sign_pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.sign_pushButton_3.setMinimumSize(QtCore.QSize(0, 45))
        self.sign_pushButton_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 9pt \"Arial\";")
        self.sign_pushButton_3.setObjectName("sign_pushButton_3")
        self.gridLayout_2.addWidget(self.sign_pushButton_3, 2, 3, 1, 1)
        self.num_pushButton_8 = QtWidgets.QPushButton(Dialog)
        self.num_pushButton_8.setMinimumSize(QtCore.QSize(0, 45))
        self.num_pushButton_8.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 9pt \"Arial\";")
        self.num_pushButton_8.setObjectName("num_pushButton_8")
        self.gridLayout_2.addWidget(self.num_pushButton_8, 3, 1, 1, 1)
        self.sign_pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.sign_pushButton_2.setMinimumSize(QtCore.QSize(0, 45))
        self.sign_pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 9pt \"Arial\";")
        self.sign_pushButton_2.setObjectName("sign_pushButton_2")
        self.gridLayout_2.addWidget(self.sign_pushButton_2, 1, 3, 1, 1)
        self.per_pushButton = QtWidgets.QPushButton(Dialog)
        self.per_pushButton.setMinimumSize(QtCore.QSize(0, 45))
        self.per_pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 9pt \"Arial\";")
        self.per_pushButton.setObjectName("per_pushButton")
        self.gridLayout_2.addWidget(self.per_pushButton, 4, 0, 1, 1)
        self.num_pushButton_9 = QtWidgets.QPushButton(Dialog)
        self.num_pushButton_9.setMinimumSize(QtCore.QSize(0, 45))
        self.num_pushButton_9.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 9pt \"Arial\";")
        self.num_pushButton_9.setObjectName("num_pushButton_9")
        self.gridLayout_2.addWidget(self.num_pushButton_9, 3, 2, 1, 1)
        self.sign_pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.sign_pushButton_4.setMinimumSize(QtCore.QSize(0, 45))
        self.sign_pushButton_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 9pt \"Arial\";")
        self.sign_pushButton_4.setObjectName("sign_pushButton_4")
        self.gridLayout_2.addWidget(self.sign_pushButton_4, 3, 3, 1, 1)
        self.dot_pushButton = QtWidgets.QPushButton(Dialog)
        self.dot_pushButton.setMinimumSize(QtCore.QSize(0, 45))
        self.dot_pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 9pt \"Arial\";")
        self.dot_pushButton.setObjectName("dot_pushButton")
        self.gridLayout_2.addWidget(self.dot_pushButton, 4, 2, 1, 1)
        self.num_pushButton_0 = QtWidgets.QPushButton(Dialog)
        self.num_pushButton_0.setMinimumSize(QtCore.QSize(0, 45))
        self.num_pushButton_0.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 9pt \"Arial\";")
        self.num_pushButton_0.setObjectName("num_pushButton_0")
        self.gridLayout_2.addWidget(self.num_pushButton_0, 4, 1, 1, 1)
        self.result_pushButton = QtWidgets.QPushButton(Dialog)
        self.result_pushButton.setMinimumSize(QtCore.QSize(0, 45))
        self.result_pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 9pt \"Arial\";")
        self.result_pushButton.setObjectName("result_pushButton")
        self.gridLayout_2.addWidget(self.result_pushButton, 4, 3, 1, 1)
        self.num_pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.num_pushButton_7.setMinimumSize(QtCore.QSize(0, 45))
        self.num_pushButton_7.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 9pt \"Arial\";")
        self.num_pushButton_7.setObjectName("num_pushButton_7")
        self.gridLayout_2.addWidget(self.num_pushButton_7, 3, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.a_lineEdit.setText(_translate("Dialog", "0"))
        self.p_close_pushButton.setText(_translate("Dialog", ")"))
        self.sign_pushButton_1.setText(_translate("Dialog", "/"))
        self.num_pushButton_1.setText(_translate("Dialog", "1"))
        self.num_pushButton_2.setText(_translate("Dialog", "2"))
        self.reset_pushButton.setText(_translate("Dialog", "C"))
        self.p_open_pushButton.setText(_translate("Dialog", "("))
        self.num_pushButton_3.setText(_translate("Dialog", "3"))
        self.num_pushButton_4.setText(_translate("Dialog", "4"))
        self.num_pushButton_5.setText(_translate("Dialog", "5"))
        self.num_pushButton_6.setText(_translate("Dialog", "6"))
        self.sign_pushButton_3.setText(_translate("Dialog", "-"))
        self.num_pushButton_8.setText(_translate("Dialog", "8"))
        self.sign_pushButton_2.setText(_translate("Dialog", "*"))
        self.per_pushButton.setText(_translate("Dialog", "%"))
        self.num_pushButton_9.setText(_translate("Dialog", "9"))
        self.sign_pushButton_4.setText(_translate("Dialog", "+"))
        self.dot_pushButton.setText(_translate("Dialog", "."))
        self.num_pushButton_0.setText(_translate("Dialog", "0"))
        self.result_pushButton.setText(_translate("Dialog", "="))
        self.num_pushButton_7.setText(_translate("Dialog", "7"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

