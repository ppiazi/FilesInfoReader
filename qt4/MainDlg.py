# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainDlg.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(501, 531)
        self.widget = QtGui.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 10, 479, 521))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.EditTargetFolder = QtGui.QLineEdit(self.widget)
        self.EditTargetFolder.setObjectName(_fromUtf8("EditTargetFolder"))
        self.horizontalLayout.addWidget(self.EditTargetFolder)
        self.BtnBrowse = QtGui.QPushButton(self.widget)
        self.BtnBrowse.setObjectName(_fromUtf8("BtnBrowse"))
        self.horizontalLayout.addWidget(self.BtnBrowse)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.RadBtnCrc32 = QtGui.QRadioButton(self.widget)
        self.RadBtnCrc32.setChecked(True)
        self.RadBtnCrc32.setObjectName(_fromUtf8("RadBtnCrc32"))
        self.horizontalLayout_5.addWidget(self.RadBtnCrc32)
        self.RadBtnMD5 = QtGui.QRadioButton(self.widget)
        self.RadBtnMD5.setObjectName(_fromUtf8("RadBtnMD5"))
        self.horizontalLayout_5.addWidget(self.RadBtnMD5)
        self.RadBtnSHA1 = QtGui.QRadioButton(self.widget)
        self.RadBtnSHA1.setObjectName(_fromUtf8("RadBtnSHA1"))
        self.horizontalLayout_5.addWidget(self.RadBtnSHA1)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.ChkBoxExtOnly = QtGui.QCheckBox(self.widget)
        self.ChkBoxExtOnly.setObjectName(_fromUtf8("ChkBoxExtOnly"))
        self.horizontalLayout_2.addWidget(self.ChkBoxExtOnly)
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.EditExtList = QtGui.QLineEdit(self.widget)
        self.EditExtList.setEnabled(False)
        self.EditExtList.setObjectName(_fromUtf8("EditExtList"))
        self.horizontalLayout_2.addWidget(self.EditExtList)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.TextOutput = QtGui.QTextBrowser(self.widget)
        self.TextOutput.setObjectName(_fromUtf8("TextOutput"))
        self.verticalLayout.addWidget(self.TextOutput)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.BtnStart = QtGui.QPushButton(self.widget)
        self.BtnStart.setObjectName(_fromUtf8("BtnStart"))
        self.horizontalLayout_3.addWidget(self.BtnStart)
        self.BtnExit = QtGui.QPushButton(self.widget)
        self.BtnExit.setObjectName(_fromUtf8("BtnExit"))
        self.horizontalLayout_3.addWidget(self.BtnExit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.TextOutput.raise_()
        self.label_2.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "FilesInfoReader GUI", None))
        self.label.setText(_translate("Dialog", "TargetFolder", None))
        self.BtnBrowse.setText(_translate("Dialog", "Browse", None))
        self.RadBtnCrc32.setText(_translate("Dialog", "CRC32", None))
        self.RadBtnMD5.setText(_translate("Dialog", "MD5", None))
        self.RadBtnSHA1.setText(_translate("Dialog", "SHA1", None))
        self.ChkBoxExtOnly.setText(_translate("Dialog", "Ext Only", None))
        self.label_2.setText(_translate("Dialog", "Extensions", None))
        self.BtnStart.setText(_translate("Dialog", "Start", None))
        self.BtnExit.setText(_translate("Dialog", "Exit", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

