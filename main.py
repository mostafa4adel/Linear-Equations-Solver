import sys
from PyQt5 import QtWidgets
import ChooseFunction
import UserInput
import Output

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    userInputUi = UserInput.Ui_UserInput(mainWindow)
    chooseFunctionUi = ChooseFunction.Ui_ChooseMethod(mainWindow, userInputUi)
    chooseFunctionUi.setupUi()

    outputUi = Output.Ui_Output(mainWindow)
    outputUi.setFunctionUi(chooseFunctionUi)

    userInputUi.setBackUi(chooseFunctionUi,outputUi)
    userInputUi = UserInput.Ui_UserInput(mainWindow)


    mainWindow.show()
    sys.exit(app.exec_())
