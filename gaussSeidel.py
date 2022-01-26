from PyQt5 import QtWidgets


def seidel(a, x, b, m, err, outputWidget: QtWidgets.QPlainTextEdit):
    n = len(a)
    flag = 1
    # '/'
    while flag > 0 and m > 0:
        flag = 0
        e = [0, 0, 0]
        for j in range(0, n):
            d = b[j]
            old = x[j]
            # to calculate xi, yi, zi
            for i in range(0, n):
                if j != i:
                    d -= a[j][i] * x[i]
            # updating the value of our solution
            x[j] = d / a[j][j]

            ea = abs((x[j] - old) / x[j])

            if ea > err:
                flag = 1
            ea = ea * 100
            e[j] = ea
        m -= 1
        # print the updated solution
    outputWidget.appendPlainText(f'x = {x[0]:.5f} y = {x[1]:.5f} z = {x[2]:.5f}')
    outputWidget.appendPlainText(f'error  = {ea:.5f}  iterations = {m:.5f}')



if __name__ == "__main__":
    # int(input())input as number of variable to be solved
    m = 50
    err = 0.00001
    a = []
    b = []
    # initial guess
    x = [0, 0, 0]
    a = [[3, -0.1, 0.2], [0.1, 7, -0.3], [0.3, -0.2, 10]]
    b = [7.85, -19.3, 71.4]
    print(x)

    # loop run for m times
    # x = seidel(a, x, b, m, err)
