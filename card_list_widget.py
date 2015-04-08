from PyQt4.QtGui import QApplication, QWidget, QVBoxLayout, QListWidget, QLineEdit


if __name__ == '__main__':
    # The app doesn't receive sys.argv, because we're using
    # sys.argv[1] to receive the image directory
    app = QApplication([])

    # Create a window, set its size, and give it a layout
    win = QWidget()
    win.setWindowTitle('Image List')
    win.setMinimumSize(600, 400)
    layout = QVBoxLayout()
    win.setLayout(layout)

    # Create one of our ImageFileList objects using the image
    # directory passed in from the command line
    lst = QListWidget(win)
    lst.addItems(["haha", "hoho", "hihi"])

    layout.addWidget(lst)

    entry = QLineEdit(win)

    layout.addWidget(entry)

    def on_item_changed(curr, prev):
        entry.setText(curr.text())

    lst.currentItemChanged.connect(on_item_changed)

    win.show()
    app.exec_()