from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtGui import QPalette,QBrush,QPixmap
from share import SI                                          #share,TeacherWindow,StudentWindow都是自己的python文件
from TeacherWindow import Tea_Window
from StudentWindow import Stu_Window


class Ui_Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(680, 434)
        self.setWindowTitle("学生信息管理系统V11.2.3")                                        # 设置窗口标题
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(710, 434))
        Form.setMaximumSize(QtCore.QSize(710, 434))
        icon = QtGui.QIcon()                                                                #自定义图标
        icon.addPixmap(QtGui.QPixmap("./icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.splitter_2 = QtWidgets.QSplitter(Form)
        self.splitter_2.setGeometry(QtCore.QRect(180, 200, 265, 39))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.label_password = QtWidgets.QLabel(self.splitter_2)
        self.label_password.setObjectName("label_password")
        self.edt_password = QtWidgets.QLineEdit(self.splitter_2)
        self.edt_password.setObjectName("edt_password")
        self.edt_password.setClearButtonEnabled(True)
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setGeometry(QtCore.QRect(180, 150, 265, 39))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label_accout = QtWidgets.QLabel(self.splitter)
        self.label_accout.setObjectName("label_accout")

        self.edt_password.setClearButtonEnabled(True)

        self.edt_account = QtWidgets.QLineEdit(self.splitter)
        self.edt_account.setObjectName("edt_account")

        self.edt_password.setClearButtonEnabled(True)


        self.splitter_3 = QtWidgets.QSplitter(Form)
        self.splitter_3.setGeometry(QtCore.QRect(200, 250, 250, 31))
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.label_2 = QtWidgets.QLabel(self.splitter_3)
        self.label_2.setObjectName("label_2")
        self.radBtn_tea = QtWidgets.QRadioButton(self.splitter_3)
        self.radBtn_tea.setObjectName("radBtn_tea")
        self.radBtn_stu = QtWidgets.QRadioButton(self.splitter_3)
        self.radBtn_stu.setObjectName("radBtn_stu")
        self.btn_login = QtWidgets.QPushButton(Form)
        self.btn_login.setGeometry(QtCore.QRect(250, 320, 131, 41))
        self.btn_login.setAutoDefault(False)
        self.btn_login.setFlat(False)
        self.btn_login.setObjectName("btn_login")
        self.label_wel_tip = QtWidgets.QLabel(Form)
        self.label_wel_tip.setGeometry(QtCore.QRect(80, 50, 538, 51))
        self.label_wel_tip.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_wel_tip.setTextFormat(QtCore.Qt.AutoText)
        self.label_wel_tip.setScaledContents(False)
        self.label_wel_tip.setObjectName("label_wel_tip")


        self.edt_password.returnPressed.connect(self.jud_login)
        self.btn_login.clicked.connect(self.jud_login)


        QtCore.QMetaObject.connectSlotsByName(Form)


        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("./Form_background.jfif")))
        Form.setPalette(palette)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.label_password.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">密码</span></p></body></html>"))
        self.label_accout.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">账号</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">身份</span></p></body></html>"))
        self.radBtn_tea.setText(_translate("Form", "教师"))
        self.radBtn_stu.setText(_translate("Form", "学生"))
        self.btn_login.setText(_translate("Form", "登录"))
        self.label_wel_tip.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; color:#5555ff;\">欢迎使用学生信息管理系统!</span></p></body></html>"))

      #以上的代码是描述界面的，是自动生成的，可根据自己需要来改
      #下面的代码是自己完成的

      #判断账号密码的函数
    def jud_login(self):
        user_acco = self.edt_account.text().strip()        #去掉空格，增强健壮性
        password = self.edt_password.text().strip()        #去掉空格，增强健壮性
        accFile = open("accout_password.txt","r")          #读取账号密码
        ls=[]
        word = 0
        for line in accFile :
              line=line.replace("\n","")
              ls = line.split(" ")
              if user_acco == ls[0] and password == ls[1] :
                  word = 1
                  accFile.close()
                  break
        if word == 0:
            QMessageBox.warning(self, '警告', '账户或密码错误', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        elif len(ls[0]) == 4 :
                SI.Win_main = Tea_Window()               #账号密码正确且账号是4位数，打开老师界面
                SI.Win_main.show()
                self.close()
        else:
            SI.Win_main = Stu_Window()                  #账号密码正确且账号不是4位数，打开学生界面
            SI.Win_main.show()
            self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_login = Ui_Widget()
    main_login.show()
    sys.exit(app.exec_())