import sys
from PyQt4 import QtCore, QtGui
import solving

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(737, 773)
        MainWindow.setBaseSize(QtCore.QSize(737, 768))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.case0_0 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case0_0.setFont(font)
        self.case0_0.setObjectName(_fromUtf8("case0_0"))
        self.gridLayout_2.addWidget(self.case0_0, 0, 0, 1, 1)
        self.case0_3 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case0_3.setFont(font)
        self.case0_3.setObjectName(_fromUtf8("case0_3"))
        self.gridLayout_2.addWidget(self.case0_3, 0, 4, 1, 1)
        self.case0_2 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case0_2.setFont(font)
        self.case0_2.setObjectName(_fromUtf8("case0_2"))
        self.gridLayout_2.addWidget(self.case0_2, 0, 2, 1, 1)
        self.case0_6 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case0_6.setFont(font)
        self.case0_6.setObjectName(_fromUtf8("case0_6"))
        self.gridLayout_2.addWidget(self.case0_6, 0, 8, 1, 1)
        self.case0_5 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case0_5.setFont(font)
        self.case0_5.setObjectName(_fromUtf8("case0_5"))
        self.gridLayout_2.addWidget(self.case0_5, 0, 6, 1, 1)
        self.case0_7 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case0_7.setFont(font)
        self.case0_7.setObjectName(_fromUtf8("case0_7"))
        self.gridLayout_2.addWidget(self.case0_7, 0, 9, 1, 1)
        self.case0_4 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case0_4.setFont(font)
        self.case0_4.setObjectName(_fromUtf8("case0_4"))
        self.gridLayout_2.addWidget(self.case0_4, 0, 5, 1, 1)
        self.case0_8 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case0_8.setFont(font)
        self.case0_8.setObjectName(_fromUtf8("case0_8"))
        self.gridLayout_2.addWidget(self.case0_8, 0, 10, 1, 1)
        self.case0_1 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case0_1.setFont(font)
        self.case0_1.setObjectName(_fromUtf8("case0_1"))
        self.gridLayout_2.addWidget(self.case0_1, 0, 1, 1, 1)
        self.case1_0 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case1_0.setFont(font)
        self.case1_0.setObjectName(_fromUtf8("case1_0"))
        self.gridLayout_2.addWidget(self.case1_0, 1, 0, 1, 1)
        self.case1_2 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case1_2.setFont(font)
        self.case1_2.setObjectName(_fromUtf8("case1_2"))
        self.gridLayout_2.addWidget(self.case1_2, 1, 2, 1, 1)
        self.case1_5 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case1_5.setFont(font)
        self.case1_5.setObjectName(_fromUtf8("case1_5"))
        self.gridLayout_2.addWidget(self.case1_5, 1, 6, 1, 1)
        self.case1_8 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case1_8.setFont(font)
        self.case1_8.setObjectName(_fromUtf8("case1_8"))
        self.gridLayout_2.addWidget(self.case1_8, 1, 10, 1, 1)
        self.case1_6 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case1_6.setFont(font)
        self.case1_6.setObjectName(_fromUtf8("case1_6"))
        self.gridLayout_2.addWidget(self.case1_6, 1, 8, 1, 1)
        self.case1_7 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case1_7.setFont(font)
        self.case1_7.setObjectName(_fromUtf8("case1_7"))
        self.gridLayout_2.addWidget(self.case1_7, 1, 9, 1, 1)
        self.case2_0 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case2_0.setFont(font)
        self.case2_0.setObjectName(_fromUtf8("case2_0"))
        self.gridLayout_2.addWidget(self.case2_0, 2, 0, 1, 1)
        self.case1_4 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case1_4.setFont(font)
        self.case1_4.setObjectName(_fromUtf8("case1_4"))
        self.gridLayout_2.addWidget(self.case1_4, 1, 5, 1, 1)
        self.case1_3 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case1_3.setFont(font)
        self.case1_3.setObjectName(_fromUtf8("case1_3"))
        self.gridLayout_2.addWidget(self.case1_3, 1, 4, 1, 1)
        self.case1_1 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case1_1.setFont(font)
        self.case1_1.setObjectName(_fromUtf8("case1_1"))
        self.gridLayout_2.addWidget(self.case1_1, 1, 1, 1, 1)
        self.case2_5 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case2_5.setFont(font)
        self.case2_5.setObjectName(_fromUtf8("case2_5"))
        self.gridLayout_2.addWidget(self.case2_5, 2, 6, 1, 1)
        self.case2_6 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case2_6.setFont(font)
        self.case2_6.setObjectName(_fromUtf8("case2_6"))
        self.gridLayout_2.addWidget(self.case2_6, 2, 8, 1, 1)
        self.case2_7 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case2_7.setFont(font)
        self.case2_7.setObjectName(_fromUtf8("case2_7"))
        self.gridLayout_2.addWidget(self.case2_7, 2, 9, 1, 1)
        self.case2_1 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case2_1.setFont(font)
        self.case2_1.setObjectName(_fromUtf8("case2_1"))
        self.gridLayout_2.addWidget(self.case2_1, 2, 1, 1, 1)
        self.case2_8 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case2_8.setFont(font)
        self.case2_8.setObjectName(_fromUtf8("case2_8"))
        self.gridLayout_2.addWidget(self.case2_8, 2, 10, 1, 1)
        self.case3_1 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case3_1.setFont(font)
        self.case3_1.setObjectName(_fromUtf8("case3_1"))
        self.gridLayout_2.addWidget(self.case3_1, 4, 1, 1, 1)
        self.case3_0 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case3_0.setFont(font)
        self.case3_0.setObjectName(_fromUtf8("case3_0"))
        self.gridLayout_2.addWidget(self.case3_0, 4, 0, 1, 1)
        self.case3_2 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case3_2.setFont(font)
        self.case3_2.setObjectName(_fromUtf8("case3_2"))
        self.gridLayout_2.addWidget(self.case3_2, 4, 2, 1, 1)
        self.case3_3 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case3_3.setFont(font)
        self.case3_3.setObjectName(_fromUtf8("case3_3"))
        self.gridLayout_2.addWidget(self.case3_3, 4, 4, 1, 1)
        self.case2_2 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case2_2.setFont(font)
        self.case2_2.setObjectName(_fromUtf8("case2_2"))
        self.gridLayout_2.addWidget(self.case2_2, 2, 2, 1, 1)
        self.case2_4 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case2_4.setFont(font)
        self.case2_4.setObjectName(_fromUtf8("case2_4"))
        self.gridLayout_2.addWidget(self.case2_4, 2, 5, 1, 1)
        self.case2_3 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case2_3.setFont(font)
        self.case2_3.setObjectName(_fromUtf8("case2_3"))
        self.gridLayout_2.addWidget(self.case2_3, 2, 4, 1, 1)
        self.case3_4 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case3_4.setFont(font)
        self.case3_4.setObjectName(_fromUtf8("case3_4"))
        self.gridLayout_2.addWidget(self.case3_4, 4, 5, 1, 1)
        self.case5_8 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case5_8.setFont(font)
        self.case5_8.setObjectName(_fromUtf8("case5_8"))
        self.gridLayout_2.addWidget(self.case5_8, 6, 10, 1, 1)
        self.case6_5 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case6_5.setFont(font)
        self.case6_5.setObjectName(_fromUtf8("case6_5"))
        self.gridLayout_2.addWidget(self.case6_5, 8, 6, 1, 1)
        self.case4_2 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case4_2.setFont(font)
        self.case4_2.setObjectName(_fromUtf8("case4_2"))
        self.gridLayout_2.addWidget(self.case4_2, 5, 2, 1, 1)
        self.case5_3 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case5_3.setFont(font)
        self.case5_3.setObjectName(_fromUtf8("case5_3"))
        self.gridLayout_2.addWidget(self.case5_3, 6, 4, 1, 1)
        self.case6_7 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case6_7.setFont(font)
        self.case6_7.setObjectName(_fromUtf8("case6_7"))
        self.gridLayout_2.addWidget(self.case6_7, 8, 9, 1, 1)
        self.case5_6 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case5_6.setFont(font)
        self.case5_6.setObjectName(_fromUtf8("case5_6"))
        self.gridLayout_2.addWidget(self.case5_6, 6, 8, 1, 1)
        self.case6_8 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case6_8.setFont(font)
        self.case6_8.setObjectName(_fromUtf8("case6_8"))
        self.gridLayout_2.addWidget(self.case6_8, 8, 10, 1, 1)
        self.case4_4 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case4_4.setFont(font)
        self.case4_4.setObjectName(_fromUtf8("case4_4"))
        self.gridLayout_2.addWidget(self.case4_4, 5, 5, 1, 1)
        self.case4_8 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case4_8.setFont(font)
        self.case4_8.setObjectName(_fromUtf8("case4_8"))
        self.gridLayout_2.addWidget(self.case4_8, 5, 10, 1, 1)
        self.case5_4 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case5_4.setFont(font)
        self.case5_4.setObjectName(_fromUtf8("case5_4"))
        self.gridLayout_2.addWidget(self.case5_4, 6, 5, 1, 1)
        self.case6_0 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case6_0.setFont(font)
        self.case6_0.setObjectName(_fromUtf8("case6_0"))
        self.gridLayout_2.addWidget(self.case6_0, 8, 0, 1, 1)
        self.case4_1 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case4_1.setFont(font)
        self.case4_1.setObjectName(_fromUtf8("case4_1"))
        self.gridLayout_2.addWidget(self.case4_1, 5, 1, 1, 1)
        self.case5_0 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case5_0.setFont(font)
        self.case5_0.setObjectName(_fromUtf8("case5_0"))
        self.gridLayout_2.addWidget(self.case5_0, 6, 0, 1, 1)
        self.case6_1 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case6_1.setFont(font)
        self.case6_1.setObjectName(_fromUtf8("case6_1"))
        self.gridLayout_2.addWidget(self.case6_1, 8, 1, 1, 1)
        self.case6_2 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case6_2.setFont(font)
        self.case6_2.setObjectName(_fromUtf8("case6_2"))
        self.gridLayout_2.addWidget(self.case6_2, 8, 2, 1, 1)
        self.case5_2 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case5_2.setFont(font)
        self.case5_2.setObjectName(_fromUtf8("case5_2"))
        self.gridLayout_2.addWidget(self.case5_2, 6, 2, 1, 1)
        self.case5_1 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case5_1.setFont(font)
        self.case5_1.setObjectName(_fromUtf8("case5_1"))
        self.gridLayout_2.addWidget(self.case5_1, 6, 1, 1, 1)
        self.case6_3 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case6_3.setFont(font)
        self.case6_3.setObjectName(_fromUtf8("case6_3"))
        self.gridLayout_2.addWidget(self.case6_3, 8, 4, 1, 1)
        self.case3_7 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case3_7.setFont(font)
        self.case3_7.setObjectName(_fromUtf8("case3_7"))
        self.gridLayout_2.addWidget(self.case3_7, 4, 9, 1, 1)
        self.case6_6 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case6_6.setFont(font)
        self.case6_6.setObjectName(_fromUtf8("case6_6"))
        self.gridLayout_2.addWidget(self.case6_6, 8, 8, 1, 1)
        self.case3_6 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case3_6.setFont(font)
        self.case3_6.setObjectName(_fromUtf8("case3_6"))
        self.gridLayout_2.addWidget(self.case3_6, 4, 8, 1, 1)
        self.case3_8 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case3_8.setFont(font)
        self.case3_8.setObjectName(_fromUtf8("case3_8"))
        self.gridLayout_2.addWidget(self.case3_8, 4, 10, 1, 1)
        self.case4_3 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case4_3.setFont(font)
        self.case4_3.setObjectName(_fromUtf8("case4_3"))
        self.gridLayout_2.addWidget(self.case4_3, 5, 4, 1, 1)
        self.case4_6 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case4_6.setFont(font)
        self.case4_6.setObjectName(_fromUtf8("case4_6"))
        self.gridLayout_2.addWidget(self.case4_6, 5, 8, 1, 1)
        self.case5_5 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case5_5.setFont(font)
        self.case5_5.setObjectName(_fromUtf8("case5_5"))
        self.gridLayout_2.addWidget(self.case5_5, 6, 6, 1, 1)
        self.case6_4 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case6_4.setFont(font)
        self.case6_4.setObjectName(_fromUtf8("case6_4"))
        self.gridLayout_2.addWidget(self.case6_4, 8, 5, 1, 1)
        self.case3_5 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case3_5.setFont(font)
        self.case3_5.setObjectName(_fromUtf8("case3_5"))
        self.gridLayout_2.addWidget(self.case3_5, 4, 6, 1, 1)
        self.case4_5 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case4_5.setFont(font)
        self.case4_5.setObjectName(_fromUtf8("case4_5"))
        self.gridLayout_2.addWidget(self.case4_5, 5, 6, 1, 1)
        self.case4_0 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case4_0.setFont(font)
        self.case4_0.setObjectName(_fromUtf8("case4_0"))
        self.gridLayout_2.addWidget(self.case4_0, 5, 0, 1, 1)
        self.case5_7 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case5_7.setFont(font)
        self.case5_7.setObjectName(_fromUtf8("case5_7"))
        self.gridLayout_2.addWidget(self.case5_7, 6, 9, 1, 1)
        self.case4_7 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case4_7.setFont(font)
        self.case4_7.setObjectName(_fromUtf8("case4_7"))
        self.gridLayout_2.addWidget(self.case4_7, 5, 9, 1, 1)
        self.case8_3 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case8_3.setFont(font)
        self.case8_3.setObjectName(_fromUtf8("case8_3"))
        self.gridLayout_2.addWidget(self.case8_3, 10, 4, 1, 1)
        self.case8_6 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case8_6.setFont(font)
        self.case8_6.setObjectName(_fromUtf8("case8_6"))
        self.gridLayout_2.addWidget(self.case8_6, 10, 8, 1, 1)
        self.case8_0 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case8_0.setFont(font)
        self.case8_0.setObjectName(_fromUtf8("case8_0"))
        self.gridLayout_2.addWidget(self.case8_0, 10, 0, 1, 1)
        self.case8_1 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case8_1.setFont(font)
        self.case8_1.setObjectName(_fromUtf8("case8_1"))
        self.gridLayout_2.addWidget(self.case8_1, 10, 1, 1, 1)
        self.case7_3 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case7_3.setFont(font)
        self.case7_3.setObjectName(_fromUtf8("case7_3"))
        self.gridLayout_2.addWidget(self.case7_3, 9, 4, 1, 1)
        self.case8_7 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case8_7.setFont(font)
        self.case8_7.setObjectName(_fromUtf8("case8_7"))
        self.gridLayout_2.addWidget(self.case8_7, 10, 9, 1, 1)
        self.case7_4 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case7_4.setFont(font)
        self.case7_4.setObjectName(_fromUtf8("case7_4"))
        self.gridLayout_2.addWidget(self.case7_4, 9, 5, 1, 1)
        self.case7_2 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case7_2.setFont(font)
        self.case7_2.setObjectName(_fromUtf8("case7_2"))
        self.gridLayout_2.addWidget(self.case7_2, 9, 2, 1, 1)
        self.case7_8 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case7_8.setFont(font)
        self.case7_8.setObjectName(_fromUtf8("case7_8"))
        self.gridLayout_2.addWidget(self.case7_8, 9, 10, 1, 1)
        self.case7_1 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case7_1.setFont(font)
        self.case7_1.setObjectName(_fromUtf8("case7_1"))
        self.gridLayout_2.addWidget(self.case7_1, 9, 1, 1, 1)
        self.case7_0 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case7_0.setFont(font)
        self.case7_0.setObjectName(_fromUtf8("case7_0"))
        self.gridLayout_2.addWidget(self.case7_0, 9, 0, 1, 1)
        self.case7_5 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case7_5.setFont(font)
        self.case7_5.setObjectName(_fromUtf8("case7_5"))
        self.gridLayout_2.addWidget(self.case7_5, 9, 6, 1, 1)
        self.case8_2 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case8_2.setFont(font)
        self.case8_2.setObjectName(_fromUtf8("case8_2"))
        self.gridLayout_2.addWidget(self.case8_2, 10, 2, 1, 1)
        self.case7_7 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case7_7.setFont(font)
        self.case7_7.setObjectName(_fromUtf8("case7_7"))
        self.gridLayout_2.addWidget(self.case7_7, 9, 9, 1, 1)
        self.case8_5 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case8_5.setFont(font)
        self.case8_5.setObjectName(_fromUtf8("case8_5"))
        self.gridLayout_2.addWidget(self.case8_5, 10, 6, 1, 1)
        self.case8_4 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case8_4.setFont(font)
        self.case8_4.setObjectName(_fromUtf8("case8_4"))
        self.gridLayout_2.addWidget(self.case8_4, 10, 5, 1, 1)
        self.case8_8 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case8_8.setFont(font)
        self.case8_8.setObjectName(_fromUtf8("case8_8"))
        self.gridLayout_2.addWidget(self.case8_8, 10, 10, 1, 1)
        self.case7_6 = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(32)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.case7_6.setFont(font)
        self.case7_6.setObjectName(_fromUtf8("case7_6"))
        self.gridLayout_2.addWidget(self.case7_6, 9, 8, 1, 1)
        spacerItem = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 0, 3, 6, 1)
        spacerItem1 = QtGui.QSpacerItem(5, 5, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 3, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(10, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 4, 7, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(5, 10, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 7, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 737, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuNouveau = QtGui.QMenu(self.menubar)
        self.menuNouveau.setObjectName(_fromUtf8("menuNouveau"))
        self.menuSolve = QtGui.QMenu(self.menubar)
        self.menuSolve.setObjectName(_fromUtf8("menuSolve"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionNouveau = QtGui.QAction(MainWindow)
        self.actionNouveau.setObjectName(_fromUtf8("actionNouveau"))
        self.actionQuitter = QtGui.QAction(MainWindow)
        self.actionQuitter.setObjectName(_fromUtf8("actionQuitter"))
        self.actionR_gles_EUP = QtGui.QAction(MainWindow)
        self.actionR_gles_EUP.setObjectName(_fromUtf8("actionR_gles_EUP"))
        self.actionBacktracking_only = QtGui.QAction(MainWindow)
        self.actionBacktracking_only.setObjectName(_fromUtf8("actionBacktracking_only"))
        self.actionSolve = QtGui.QAction(MainWindow)
        self.actionSolve.setObjectName(_fromUtf8("actionSolve"))
        self.actionNouveau_2 = QtGui.QAction(MainWindow)
        self.actionNouveau_2.setObjectName(_fromUtf8("actionNouveau_2"))
        self.menuNouveau.addAction(self.actionNouveau_2)
        self.menuNouveau.addAction(self.actionQuitter)
        self.menuSolve.addAction(self.actionR_gles_EUP)
        self.menuSolve.addAction(self.actionBacktracking_only)
        self.menuSolve.addSeparator()
        self.menuSolve.addAction(self.actionSolve)
        self.menubar.addAction(self.menuNouveau.menuAction())
        self.menubar.addAction(self.menuSolve.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def textedits():
            for child in self.centralwidget.children():
                yield child    
        
        for child in textedits():
            child.setAlignment(QtCore.Qt.AlignCenter)
            
        self.actionNouveau_2.triggered.connect(self.reset)
        self.actionQuitter.triggered.connect(self.quitter)
        self.actionSolve.triggered.connect(self.solve)

        self.actionNouveau_2.triggered.connect(self.reset)
        self.actionQuitter.triggered.connect(self.quitter)
        self.actionSolve.triggered.connect(self.solve)

        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def reset(self):
        for child in self.centralwidget.children():
            try:
                child.clear()
                child.setAlignment(QtCore.Qt.AlignCenter)
            except:
                pass
            
    def quitter(self):
        sys.exit(app.exec_())
        
    def solve(self):
        cases = [f"case{i}_{j}" for i in range(0, 9) for j in range(0, 9)]
        sudoku = [[None for i in range(9)] for k in range(9)]
        for case in cases:
            textedit = self.centralwidget.findChild(QtGui.QTextEdit, case)
            number = textedit.toPlainText()
            
            if number == '': 
                number = 0
                
            index = (int(case[6]) ,int(case[4]))
            
            try:
                number = int(number)
            except:
                raise ValueError("Not numeric value entered")
                                 
            if int(number) not in range(0, 10):
                raise ValueError("Out of range value entered.")
            else:
                sudoku[index[1]][index[0]] = int(number)

        # solving.sudo_print(sudoku)
          
        sudoku = solving.solve(sudoku)
        for case in cases:
            textedit = self.centralwidget.findChild(QtGui.QTextEdit, case)
            if textedit.toPlainText() == '':
                textedit.setTextColor(QtGui.QColor(0,0,200))
                textedit.setText(str(sudoku[int(case[6])][int(case[4])]))
                textedit.setAlignment(QtCore.Qt.AlignCenter)
        


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Solver", None))
        self.menuNouveau.setTitle(_translate("MainWindow", "Sudoku", None))
        self.menuSolve.setTitle(_translate("MainWindow", "Solve", None))
        self.actionNouveau.setText(_translate("MainWindow", "Nouveau", None))
        self.actionQuitter.setText(_translate("MainWindow", "Quit", None))
        self.actionR_gles_EUP.setText(_translate("MainWindow", "EUP Rules Only", None))
        self.actionBacktracking_only.setText(_translate("MainWindow", "Backtracking Only", None))
        self.actionSolve.setText(_translate("MainWindow", "Solve", None))
        self.actionNouveau_2.setText(_translate("MainWindow", "Reset", None))

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
