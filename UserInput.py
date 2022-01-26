# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UserInput.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!
import os

from sympy import *
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog


class Ui_UserInput(object):
    def __init__(self, mainWindow):
        self.UserInputWindow = mainWindow

    def setBackUi(self, backUi, outputUi):
        self.backUi = backUi
        self.outputUi = outputUi

    def setMethod(self, method: str):
        self.method = method

    def setupUi(self):
        self.UserInputWindow.setObjectName("UserInput")
        self.UserInputWindow.resize(400, 250)
        self.UserInputWindow.setMinimumSize(QtCore.QSize(400, 250))
        self.UserInputWindow.setMaximumSize(QtCore.QSize(400, 250))
        self.centralwidget = QtWidgets.QWidget(self.UserInputWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.function1Label = QtWidgets.QLabel(self.centralwidget)
        self.function1Label.setGeometry(QtCore.QRect(10, 20, 67, 25))
        self.function1Label.setObjectName("function1Label")

        self.function1Input = QtWidgets.QLineEdit(self.centralwidget)
        self.function1Input.setGeometry(QtCore.QRect(100, 20, 280, 25))
        self.function1Input.setObjectName("function1Input")

        self.function2Label = QtWidgets.QLabel(self.centralwidget)
        self.function2Label.setGeometry(QtCore.QRect(10, 60, 67, 25))
        self.function2Label.setObjectName("function2Label")

        self.function2Input = QtWidgets.QLineEdit(self.centralwidget)
        self.function2Input.setGeometry(QtCore.QRect(100, 60, 280, 25))
        self.function2Input.setObjectName("function2Input")

        self.function3Label = QtWidgets.QLabel(self.centralwidget)
        self.function3Label.setGeometry(QtCore.QRect(10, 100, 67, 25))
        self.function3Label.setObjectName("function3Label")

        self.function3Input = QtWidgets.QLineEdit(self.centralwidget)
        self.function3Input.setGeometry(QtCore.QRect(100, 100, 280, 25))
        self.function3Input.setObjectName("function3Input")

        self.evaluateButton = QtWidgets.QPushButton(self.centralwidget)
        self.evaluateButton.setGeometry(QtCore.QRect(145, 210, 90, 30))
        self.evaluateButton.setObjectName("evaluateButton")
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(0, 0, 50, 25))
        self.backButton.setObjectName("backButton")

        self.UserInputWindow.setCentralWidget(self.centralwidget)
        self.backButton.clicked.connect(self.backButtonClicked)

        QtCore.QMetaObject.connectSlotsByName(self.UserInputWindow)
        self.evaluateButton.clicked.connect(self.evaluateButtonClicked)

        if self.method == "Gaussian-Seidel":
            self.xGuessLabel = QtWidgets.QLabel(self.centralwidget)
            self.xGuessLabel.setGeometry(QtCore.QRect(20, 140, 70, 25))
            self.xGuessLabel.setObjectName("xGuessLabel")

            self.xInput = QtWidgets.QDoubleSpinBox(self.centralwidget)
            self.xInput.setGeometry(QtCore.QRect(40, 140, 60, 25))
            self.xInput.setDecimals(2)
            self.xInput.setMinimum(-100000000.0)
            self.xInput.setMaximum(100000000.0)

            self.yGuessLabel = QtWidgets.QLabel(self.centralwidget)
            self.yGuessLabel.setGeometry(QtCore.QRect(130, 140, 70, 25))
            self.yGuessLabel.setObjectName("yGuessLabel")

            self.yInput = QtWidgets.QDoubleSpinBox(self.centralwidget)
            self.yInput.setGeometry(QtCore.QRect(150, 140, 60, 25))
            self.yInput.setDecimals(2)
            self.yInput.setMinimum(-100000000.0)
            self.yInput.setMaximum(100000000.0)

            self.zGuessLabel = QtWidgets.QLabel(self.centralwidget)
            self.zGuessLabel.setGeometry(QtCore.QRect(240, 140, 70, 25))
            self.zGuessLabel.setObjectName("zGuessLabel")

            self.zInput = QtWidgets.QDoubleSpinBox(self.centralwidget)
            self.zInput.setGeometry(QtCore.QRect(260, 140, 60, 25))
            self.zInput.setDecimals(2)
            self.zInput.setMinimum(-100000000.0)
            self.zInput.setMaximum(100000000.0)

            self.errorLabel = QtWidgets.QLabel(self.centralwidget)
            self.errorLabel.setGeometry(QtCore.QRect(200, 180, 41, 25))
            self.errorLabel.setObjectName("errorLabel")

            self.errorInput = QtWidgets.QDoubleSpinBox(self.centralwidget)
            self.errorInput.setGeometry(QtCore.QRect(250, 180, 70, 25))
            self.errorInput.setDecimals(5)
            self.errorInput.setMinimum(-1.0)
            self.errorInput.setMaximum(1.0)
            self.errorInput.setObjectName("doubleSpinBox_3")

            self.maxIterLabel = QtWidgets.QLabel(self.centralwidget)
            self.maxIterLabel.setGeometry(QtCore.QRect(10, 180, 141, 25))
            self.maxIterLabel.setObjectName("maxIterLabel")
            self.maxIterInput = QtWidgets.QSpinBox(self.centralwidget)
            self.maxIterInput.setGeometry(QtCore.QRect(140, 180, 50, 25))
            self.maxIterInput.setObjectName("spinBox")

            # self.maxIterationsLabel = QtWidgets.QLabel(self.centralwidget)
            # self.maxIterationsLabel.setGeometry(QtCore.QRect(250, 140, 90, 25))
            # self.maxIterationsLabel.setObjectName("maxIterationsLabel")
            #
            # self.maxIterInput = QtWidgets.QSpinBox(self.centralwidget)
            # self.maxIterInput.setGeometry(QtCore.QRect(340, 140, 50, 25))
            # self.maxIterInput.setObjectName("spinBox")
        self.retranslateUi()

    def backButtonClicked(self):
        self.backUi.setupUi()
        self.UserInputWindow.show()

    def evaluateButtonClicked(self):
        wrongInput = False
        func1 = self.function1Input.text().split('=')
        func2 = self.function2Input.text().split('=')
        func3 = self.function3Input.text().split('=')

        if len(func1) + len(func2) + len(func3) != 6:
            wrongInput = True

        wrongInput = not validateFunction(func1[0])
        wrongInput = not validateFunction(func2[0])
        wrongInput = not validateFunction(func3[0])

        if wrongInput:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Wrong Input")
            msg.setInformativeText('Input Proper Values')
            msg.setWindowTitle("Error")
            msg.exec_()
            return

        if self.method != "Gaussian-Seidel":
            self.outputUi.setValues(func1, func2, func3,
                                    0, 0, 0, self.method)

        else:
            self.outputUi.setValues(func1, func2, func3, [float(self.xInput.value()), float(self.yInput.value()),
                                                          float(self.zInput.value())],
                                    self.maxIterInput.value(), self.errorInput.value(), self.method)

        self.outputUi.setupUi()
        self.UserInputWindow.show()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.UserInputWindow.setWindowTitle(_translate("UserInput", "MainWindow"))
        self.function1Label.setText(_translate("UserInput", "Function 1 :"))
        self.function2Label.setText(_translate("UserInput", "Function 2 :"))
        self.function3Label.setText(_translate("UserInput", "Function 3 :"))

        if self.method == "Gaussian-Seidel":
            self.xGuessLabel.setText(_translate("UserInput", "X :"))
            self.yGuessLabel.setText(_translate("UserInput", "Y :"))
            self.zGuessLabel.setText(_translate("UserInput", "Z :"))
            self.errorLabel.setText(_translate("UserInput", "Error :"))
            self.maxIterLabel.setText(_translate("UserInput", "Maximum Iterations :"))

        self.evaluateButton.setText(_translate("UserInput", "Evaluate"))
        self.backButton.setText(_translate("UserInput", "Back"))


def validateFunction(func: str):
    try:
        function = parse_expr(func)

        if len(function.atoms(Symbol)) > 3 or len(function.atoms(Symbol)) == 0:
            return False
        if 'x' not in str(function):
            return False
        if 'y' not in str(function):
            return False
        if 'z' not in str(function):
            return False

        return True
    except:
        return False
