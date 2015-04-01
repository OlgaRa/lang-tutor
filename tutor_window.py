import sys
from PyQt4 import QtGui

class Example(QtGui.QMainWindow):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        word = QtGui.QLabel('Word:', self)
        word.move(20, 60)

        translation = QtGui.QLabel('Transcription:', self)
        translation.move(20, 80)

        example = QtGui.QLabel('Example:', self)
        example.move(20, 100)

        chooser = QtGui.QLabel('The rigth answer is:', self)
        chooser.move(20, 140)

        cb1 = QtGui.QCheckBox('Version 1', self)
        cb1.move(20, 160)

        cb2 = QtGui.QCheckBox('Version 2', self)
        cb2.move(20, 180)

        cb3 = QtGui.QCheckBox('Version 3', self)
        cb3.move(20, 200)

        exitAction = QtGui.QAction(QtGui.QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(QtGui.qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAction)

        self.setToolTip('This is a button to continue')
        btn = QtGui.QPushButton('Ready', self)
        btn.setToolTip('This is a a button to continue')
        btn.resize(btn.sizeHint())
        btn.clicked.connect(self.buttonClicked)
        btn.move(120, 220)

        self.setGeometry(300, 300, 300, 260)
        self.setWindowTitle('Language tutor')
        self.show()

    def closeEvent(self, event):

        reply = QtGui.QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QtGui.QMessageBox.Yes |
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def buttonClicked(self):

        sender = self.sender()
        self.statusBar().showMessage('It is corect/incorret answer')


def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()