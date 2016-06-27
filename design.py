# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kieranjol/Downloads/615def9e197d5db04bef-c52e123ba3de78a5ae11bbaa4cd826207044f29c/design.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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
        MainWindow.resize(702, 424)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.dirname_text = QtGui.QLineEdit(self.centralwidget)
        self.dirname_text.setObjectName(_fromUtf8("dirname_text"))
        self.gridLayout.addWidget(self.dirname_text, 1, 1, 1, 1)
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox, 2, 1, 1, 1)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 6, 1, 1, 1)
        self.checkBox_2 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.gridLayout.addWidget(self.checkBox_2, 5, 0, 1, 1)
        self.btnBrowse = QtGui.QPushButton(self.centralwidget)
        self.btnBrowse.setObjectName(_fromUtf8("btnBrowse"))
        self.gridLayout.addWidget(self.btnBrowse, 0, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 2, 0, 1, 1)
        self.checkBox = QtGui.QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.gridLayout.addWidget(self.checkBox, 4, 0, 1, 2)
        self.filename_text = QtGui.QLineEdit(self.centralwidget)
        self.filename_text.setMinimumSize(QtCore.QSize(450, 0))
        self.filename_text.setObjectName(_fromUtf8("filename_text"))
        self.gridLayout.addWidget(self.filename_text, 0, 1, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 702, 25))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menuBar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menuBar)
        self.actionOpen_single_file = QtGui.QAction(MainWindow)
        self.actionOpen_single_file.setObjectName(_fromUtf8("actionOpen_single_file"))
        self.actionOpen_Directory_Batch = QtGui.QAction(MainWindow)
        self.actionOpen_Directory_Batch.setObjectName(_fromUtf8("actionOpen_Directory_Batch"))
        self.actionSettings = QtGui.QAction(MainWindow)
        self.actionSettings.setObjectName(_fromUtf8("actionSettings"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.menuFile.addAction(self.actionOpen_single_file)
        self.menuFile.addAction(self.actionOpen_Directory_Batch)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSettings)
        self.menuHelp.addAction(self.actionAbout)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "FFV1 Transcoder v0.1 - 2016", None))
        self.comboBox.setItemText(0, _translate("MainWindow", ".mkv", None))
        self.comboBox.setItemText(1, _translate("MainWindow", ".mov", None))
        self.comboBox.setItemText(2, _translate("MainWindow", ".avi", None))
        self.pushButton.setText(_translate("MainWindow", "Encode", None))
        self.checkBox_2.setText(_translate("MainWindow", "Generate md5 manifest", None))
        self.btnBrowse.setText(_translate("MainWindow", "Select file (single input)", None))
        self.lineEdit.setText(_translate("MainWindow", "Select Container:", None))
        self.checkBox.setText(_translate("MainWindow", "Disable Lossless Verification (NOT RECOMMENDED)", None))
        self.pushButton_2.setText(_translate("MainWindow", "Select Directory (batch encode)", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionOpen_single_file.setText(_translate("MainWindow", "Open Single File", None))
        self.actionOpen_Directory_Batch.setText(_translate("MainWindow", "Open Directory (Batch)", None))
        self.actionSettings.setText(_translate("MainWindow", "Settings", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
