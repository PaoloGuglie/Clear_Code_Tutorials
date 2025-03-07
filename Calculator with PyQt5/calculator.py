import PyQt5.QtWidgets as qtw


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        # Set window title
        self.setWindowTitle('Calculator')

        # Set the result field
        self.result_field = None

        # Create vertical layout
        self.setLayout(qtw.QVBoxLayout())

        # Add the keypad to the main window
        self.keypad()

        # Display the object and its elements (widgets)
        self.show()

    def keypad(self):
        # create container
        container = qtw.QWidget()
        # set grid layout
        container.setLayout(qtw.QGridLayout())
        # Create buttons
        self.result_field = qtw.QLineEdit()  # add 'self' to make it accessible from outside the method
        btn_result = qtw.QPushButton('Enter')
        btn_clear = qtw.QPushButton('Clear')
        btn_9 = qtw.QPushButton('9')
        btn_8 = qtw.QPushButton('8')
        btn_7 = qtw.QPushButton('7')
        btn_6 = qtw.QPushButton('6')
        btn_5 = qtw.QPushButton('5')
        btn_4 = qtw.QPushButton('4')
        btn_3 = qtw.QPushButton('3')
        btn_2 = qtw.QPushButton('2')
        btn_1 = qtw.QPushButton('1')
        btn_0 = qtw.QPushButton('0')
        btn_plus = qtw.QPushButton('+')
        btn_minus = qtw.QPushButton('-')
        btn_multiply = qtw.QPushButton('*')
        btn_divide = qtw.QPushButton('/')
        # Add the buttons to the layout
        container.layout().addWidget(self.result_field, 0, 0, 1, 4)
        container.layout().addWidget(btn_result, 1, 0, 1, 2)
        container.layout().addWidget(btn_clear, 1, 2, 1, 2)
        container.layout().addWidget(btn_9, 2, 0)
        container.layout().addWidget(btn_8, 2, 1)
        container.layout().addWidget(btn_7, 2, 2)
        container.layout().addWidget(btn_plus, 2, 3)
        container.layout().addWidget(btn_6, 3, 0)
        container.layout().addWidget(btn_5, 3, 1)
        container.layout().addWidget(btn_4, 3, 2)
        container.layout().addWidget(btn_minus, 3, 3)
        container.layout().addWidget(btn_3, 4, 0)
        container.layout().addWidget(btn_2, 4, 1)
        container.layout().addWidget(btn_1, 4, 2)
        container.layout().addWidget(btn_multiply, 4, 3)
        container.layout().addWidget(btn_0, 5, 0, 1, 3)
        container.layout().addWidget(btn_divide, 5, 3)
        # add the keypad (widget containing widgets) to the main window
        self.layout().addWidget(container)


# Create application and main window
app = qtw.QApplication([])
main_window = MainWindow()

# Style the application
app.setStyle(qtw.QStyleFactory.create('Fusion'))

# Run the application
app.exec_()



