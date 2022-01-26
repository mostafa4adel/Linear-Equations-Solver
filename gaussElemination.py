from sympy import *
from PyQt5 import QtWidgets
import time
from sympy import *
import sys
import numpy as np


def gaussElemination(func1: Float, eql1, func2: Float, eql2, func3: Float, eql3,
                     outputWidget: QtWidgets.QPlainTextEdit):
    x = np.zeros(3)
    a = np.zeros((3, 3 + 1))

    sx = Symbol('x')
    sy = Symbol('y')
    sz = Symbol('z')

    a[0][0], a[0][1], a[0][2], a[0][3] = func1.coeff(sx), func1.coeff(sy), func1.coeff(sz), eql1

    a[1][0], a[1][1], a[1][2], a[1][3] = func2.coeff(sx), func2.coeff(sy), func2.coeff(sz), eql2

    a[2][0], a[2][1], a[2][2], a[2][3] = func3.coeff(sx), func3.coeff(sy), func3.coeff(sz), eql3

    # Applying Gauss Elimination
    for i in range(3):
        if a[i][i] == 0.0:
            outputWidget.appendPlainText('Divide by zero detected!')
            return
        for j in range(i + 1, 3):
            ratio = a[j][i] / a[i][i]

            for k in range(3 + 1):
                a[j][k] = a[j][k] - ratio * a[i][k]

    # Back Substitution

    x[3 - 1] = a[3 - 1][3] / a[3 - 1][3 - 1]

    for i in range(3 - 2, -1, -1):
        x[i] = a[i][3]

        for j in range(i + 1, 3):
            x[i] = x[i] - a[i][j] * x[j]

        x[i] = x[i] / a[i][i]

    outputWidget.appendPlainText('\nRequired solution is: ')
    outputWidget.appendPlainText(f'x = {x[0]:.5f} y = {x[1]:.5f} z = {x[2]:.5f}')


if __name__ == "__main__":
    x = Symbol('x')
    y = Symbol('y')
    z = Symbol('z')
    func1 = x * 25 + y * 5 + 1 * z
    func2 = x * 64 + 8 * y + 1 * z
    func3 = x * 144 + y * 12 + z
    eql1 = 106.8
    eql2 = 177.2
    eql3 = 279.26666
    gaussElemination(func1, eql1, func2, eql2, func3, eql3)
