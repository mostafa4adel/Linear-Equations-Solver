# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Output.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!
import numpy as np

from PyQt5 import QtCore, QtGui, QtWidgets
import ChooseFunction
from sympy import *

import gaussElemination
import gaussJordan
import gaussSeidel


class Ui_Output(object):
    def __init__(self, mainWindow):
        self.OutputWindow = mainWindow

    def setFunctionUi(self, functionUi):
        self.functionUi = functionUi

    def setValues(self, func1, func2, func3, xyzGuess, maxIter, error, method):
        self.maxIter = maxIter
        self.func1 = func1
        self.func2 = func2
        self.func3 = func3
        self.error = error
        self.maxIter = maxIter
        self.method = method
        self.xyzGuess = xyzGuess
        print('set Values')

    def setupUi(self):
        print(123)
        self.OutputWindow.setObjectName("Output")
        self.OutputWindow.resize(400, 250)
        self.OutputWindow.setMinimumSize(QtCore.QSize(400, 250))
        self.OutputWindow.setMaximumSize(QtCore.QSize(400, 250))
        self.centralwidget = QtWidgets.QWidget(self.OutputWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.outputBox = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.outputBox.setGeometry(QtCore.QRect(25, 30, 200, 200))
        self.outputBox.setObjectName("iterationsOutput")
        self.outputBox.setReadOnly(True)

        self.outputLabel = QtWidgets.QLabel(self.centralwidget)
        self.outputLabel.setGeometry(QtCore.QRect(25, 10, 71, 17))
        self.outputLabel.setObjectName("outputLabel")

        self.newFunctioButton = QtWidgets.QPushButton(self.centralwidget)
        self.newFunctioButton.setGeometry(QtCore.QRect(250, 10, 141, 51))
        self.newFunctioButton.setObjectName("newFunctioButton")
        self.OutputWindow.setCentralWidget(self.centralwidget)
        self.newFunctioButton.clicked.connect(self.newFunctionClicked)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.OutputWindow)

    def newFunctionClicked(self):
        self.functionUi.setupUi()
        self.OutputWindow.show()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.OutputWindow.setWindowTitle(_translate("Output", "Output"))
        self.func1[0] = parse_expr(self.func1[0])
        self.func2[0] = parse_expr(self.func2[0])
        self.func3[0] = parse_expr(self.func3[0])

        self.func1[1] = float(self.func1[1])
        self.func2[1] = float(self.func2[1])
        self.func3[1] = float(self.func3[1])

        a = np.zeros((3, 3))
        b = [0, 0, 0]

        sx = Symbol('x')
        sy = Symbol('y')
        sz = Symbol('z')
        a[0][0], a[0][1], a[0][2] = self.func1[0].coeff(sx), self.func1[0].coeff(sy), self.func1[0].coeff(sz)
        a[1][0], a[1][1], a[1][2] = self.func2[0].coeff(sx), self.func2[0].coeff(sy), self.func2[0].coeff(sz)
        a[2][0], a[2][1], a[2][2] = self.func3[0].coeff(sx), self.func3[0].coeff(sy), self.func3[0].coeff(sz)

        b[0], b[1], b[2] = self.func1[1], self.func2[1], self.func3[1]

        if self.method == "Gaussian-Seidel":

            if self.maxIter == 0:
                self.maxIter = 50
            if self.error == 0:
                self.error = 0.00001

            gaussSeidel.seidel(a, self.xyzGuess, b, self.maxIter, self.error, self.outputBox)

        if self.method == 'Gaussian-elimination':
            gaussElemination.gaussElemination(self.func1[0], self.func1[1],
                                              self.func2[0], self.func2[1],
                                              self.func3[0], self.func3[1],
                                              self.outputBox)

        if self.method == 'Gaussian-Jordan':
            gaussJordan.jordan(a, b, 3, self.outputBox)

        self.outputLabel.setText(_translate("Output", "Output"))

        self.newFunctioButton.setText(_translate("Output", "Enter New Function"))
