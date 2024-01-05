from PyQt5.QtWidgets import *
import sys
import random


class Generate_password(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(0, 0, 400, 310)
        self.setFixedSize(400, 310)
        self.setWindowTitle('Generate Your Password')
        self.digits = '1234567890'
        self.capitals = 'QWERTYUIOPASDFGHJKLZXCVBNM'
        self.special_symbols = '!@#$%&*()_?{}[]'
        self.combo = []
        self.pool = 'qwertyuiopasdfghjklzxcvbnm'
        self.password = ''
        self.pswrd = ''
        self.tt = ''
        self.flag = 0
        self.last = 0
        #

        self.LineEdit = QLineEdit(self)
        self.LineEdit.setGeometry(10, 40, 171, 22)
        self.LineEdit.setText('8')
        #

        self.LineEdit_2 = QLineEdit(self)
        self.LineEdit_2.setGeometry(10, 160, 371, 121)
        #

        self.LineEdit_3 = QLineEdit(self)
        self.LineEdit_3.setGeometry(210, 40, 171, 22)
        self.LineEdit_3.setText('1')
        #

        self.label = QLabel(self)
        self.label.setGeometry(10, 20, 121, 21)
        self.label.setText('Password Length')
        #

        self.label_2 = QLabel(self)
        self.label_2.setGeometry(210, 20, 121, 21)
        self.label_2.setText('Quantity')
        #

        self.checkBox = QCheckBox(self)
        self.checkBox.setGeometry(10, 80, 111, 21)
        self.checkBox.setText('Digits')
        self.checkBox.stateChanged.connect(self.combo_add_digits)
        #

        self.checkBox_2 = QCheckBox(self)
        self.checkBox_2.setGeometry(140, 80, 111, 21)
        self.checkBox_2.setText('Capitals')
        self.checkBox_2.stateChanged.connect(self.combo_add_capitals)
        #

        self.checkBox_3 = QCheckBox(self)
        self.checkBox_3.setGeometry(270, 80, 111, 21)
        self.checkBox_3.setText('Special symbols')
        self.checkBox_3.stateChanged.connect(self.combo_add_special_symbols)
        #

        self.pushButton = QPushButton(self)
        self.pushButton.setGeometry(130, 120, 131, 31)
        self.pushButton.setText('Generate')
        self.pushButton.clicked.connect(self.gnrt)
        #

        self.pushButton_2 = QPushButton(self)
        self.pushButton_2.setGeometry(10, 120, 111, 24)
        self.pushButton_2.setText('Show')
        self.pushButton_2.clicked.connect(self.show_password)
        #

        self.pushButton_3 = QPushButton(self)
        self.pushButton_3.setGeometry(270, 120, 111, 24)
        self.pushButton_3.setText('Hide')
        self.pushButton_3.clicked.connect(self.hide_password)
        #

        self.textEdit = QTextEdit(self)
        self.textEdit.setGeometry(10, 160, 371, 121)
        self.textEdit.setReadOnly(True)
        self.textEdit.setText('')
        self.textEdit.hide()
        #

    def gnrt(self):

        with open('data.txt', 'r', encoding='utf-8') as file:
            data = file.read()
            if len(data) <= 4:
                self.last = 1
                with open('data.txt', 'w', encoding='utf-8') as dt:
                    dt.write('')
            else:
                self.last = len(data.split('\n'))


        count = 1
        pool = []
        if '1' in self.combo:
            count += 1
            pool.append(self.digits)

        if '2' in self.combo:
            count += 1
            pool.append(self.capitals)

        if '3' in self.combo:
            count += 1
            pool.append(self.special_symbols)

        number = int(self.LineEdit.text())
        if number < 4:
            self.Plan_B = self.pool + ''.join(pool)
            self.toText = ''
            self.toDate = ''

            for i in range(1, int(self.LineEdit_3.text()) + 1):
                self.pswrd += ''.join(random.choices(self.Plan_B, k=number))

                self.password = ''
                for j in self.pswrd:
                    self.password += j

                self.toText += str(i) + ' - ' + self.password + '\n'
                self.toDate += str(self.last) + ' - ' + self.password + '\n'
                self.pswrd = ''
                self.last += 1
            self.textEdit.show()
            with open('data.txt', 'a', encoding='utf-8') as file:
                file.write(self.toDate)
            self.textEdit.setText('Click "Show" to see.')
        else:
            self.toText = ''
            self.toDate = ''

            for i in range(1, int(self.LineEdit_3.text()) + 1):
                for j in pool:
                    self.pswrd += ''.join(random.choices(j, k=(random.randint(1, number // count))))

                number3 = number - len(self.pswrd)

                if len(self.pswrd) < number:
                    self.pswrd += ''.join(random.choices(self.pool, k=number3))

                random.shuffle([i for i in self.pswrd])
                self.password = ''
                for j in self.pswrd:
                    self.password += j
                self.toText += str(i) + ' - ' +  self.password + '\n'
                self.toDate += str(self.last) + ' - ' + self.password + '\n'
                self.pswrd = ''
                self.last += 1
            self.textEdit.show()
            with open('data.txt', 'a', encoding='utf-8') as file:
                file.write(self.toDate)
            self.textEdit.setText('Click "Show" to see.')

    def combo_add_digits(self):
        self.combo.append('1')

    def combo_add_capitals(self):
        self.combo.append('2')

    def combo_add_special_symbols(self):
        self.combo.append('3')

    def show_password(self):
        self.textEdit.setText(self.toText)

    def hide_password(self):
        self.textEdit.setText('Click "Show" to see.')


class password_manager(QWidget):

    def __init__(self):

        with open('data.txt', 'r') as file:
            data = file.read().split('\n')
            data = data[1:]

        super().__init__()

        self.setGeometry(8, 372, 400, 310)
        self.setFixedSize(400, 310)
        self.setWindowTitle('Password manager')

        self.LineEdit = QLineEdit(self)
        self.LineEdit.setGeometry(130, 10, 261, 22)
        #

        self.LineEdit_2 = QLineEdit(self)
        self.LineEdit_2.setGeometry(130, 40, 261, 22)
        #

        self.label = QLabel(self)
        self.label.setGeometry(10, 10, 101, 21)
        self.label.setText('password name')
        #

        self.label_2 = QLabel(self)
        self.label_2.setGeometry(10, 40, 101, 21)
        self.label_2.setText('password')
        #

        self.add_button = QPushButton(self)
        self.add_button.setGeometry(310, 80, 81, 41)
        self.add_button.setText('Add')
        self.add_button.clicked.connect(self.add_password)
        #

        self.del_button = QPushButton(self)
        self.del_button.setGeometry(310, 130, 81, 41)
        self.del_button.setText('Delete')
        self.del_button.clicked.connect(self.delete_password)
        #

        self.clear_button = QPushButton(self)
        self.clear_button.setGeometry(310, 180, 81, 41)
        self.clear_button.setText('Clear')
        self.clear_button.clicked.connect(self.clear_passwords)
        #

        self.refresh_button = QPushButton(self)
        self.refresh_button.setGeometry(310, 230, 81, 41)
        self.refresh_button.setText('Refresh')
        self.refresh_button.clicked.connect(self.refresh)

        self.List_widget = QListWidget(self)
        self.List_widget.setGeometry(10, 80, 291, 191)
        self.List_widget.addItems(data)
        #

    def refresh(self):
        with open('data.txt', 'r', encoding='utf-8') as filee:
            data = filee.read().split('\n')[:-1]
            self.List_widget.clear()
            self.List_widget.addItems(data)

    def add_password(self):

        with open('data.txt', 'a', encoding='utf-8') as ff:
            list_item = QListWidgetItem()
            name = ''.join(i for i in self.LineEdit.text())
            password = ''.join(i for i in self.LineEdit_2.text())
            list_item.setText(f'{name} - {password}')
            self.List_widget.addItem(list_item)
            ff.write(f'{name} - {password}\n')

    def delete_password(self):

        listik = []
        with open('data.txt', 'r', encoding='utf-8') as fff:
            data = fff.read().split('\n')[1:]
            for i in data:
                listik.append(i)
            pos = self.List_widget.currentRow()
            warn = QMessageBox.question(self, 'warning', f"Are you sure to delete this password?",
                                        QMessageBox.Yes | QMessageBox.No)
            if warn == QMessageBox.Yes:
                if pos >= 0:
                    pswrd = self.List_widget.takeItem(pos)
                    listik.pop(self.List_widget.currentRow())
                    del pswrd

        with open('data.txt', 'w', encoding='utf-8') as new:
            for i in listik[:-1]:
                new.write(i + '\n')

    def clear_passwords(self):

        warn = QMessageBox.question(self, 'warning', "Are you sure to reset all the values?",
                                    QMessageBox.Yes | QMessageBox.No)
        if warn == QMessageBox.Yes:
            self.List_widget.clear()
            with open('data.txt', 'w', encoding='utf-8') as dell:
                dell.write('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app2 = QApplication(sys.argv)
    ex = Generate_password()
    ex2 = password_manager()
    ex.show()
    ex2.show()
    sys.exit(app.exec())
    sys.exit(app2.exec())
