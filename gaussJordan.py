import sys
from PyQt5 import QtWidgets


def jordan(a, b, n, outputWidget: QtWidgets.QPlainTextEdit):
    x = [0, 0, 0]
    for i in range(n):
        if a[i][i] == 0.0:
            outputWidget.appendPlainText('Divide by zero detected!')
            return
        for j in range(n):
            if i != j:
                ratio = a[j][i] / a[i][i]

                for k in range(n):
                    a[j][k] = a[j][k] - ratio * a[i][k]
                b[j] = b[j] - ratio * b[i]
    for i in range(n):
        x[i] = b[i] / a[i][i]

    outputWidget.appendPlainText(f'x = {x[0]:.5f} y = {x[1]:.5f} z = {x[2]:.5f}')


if __name__ == '__main__':
    n = 3
    a = [[1, 1, -1], [1, -1, 2], [2, 1, 1]]
    b = [7, 3, 9]
    x = jordan(a, b, n)
    # Displaying solution
    print('\nRequired solution is: ', x)
