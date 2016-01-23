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
        Dialog.resize(501, 539)
        self.widget = QtGui.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 10, 479, 521))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.LayoutTargetFolder = QtGui.QHBoxLayout()
        self.LayoutTargetFolder.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.LayoutTargetFolder.setObjectName(_fromUtf8("LayoutTargetFolder"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.LayoutTargetFolder.addWidget(self.label)
        self.EditTargetFolder = QtGui.QLineEdit(self.widget)
        self.EditTargetFolder.setObjectName(_fromUtf8("EditTargetFolder"))
        self.LayoutTargetFolder.addWidget(self.EditTargetFolder)
        self.BtnBrowse = QtGui.QPushButton(self.widget)
        self.BtnBrowse.setObjectName(_fromUtf8("BtnBrowse"))
        self.LayoutTargetFolder.addWidget(self.BtnBrowse)
        self.verticalLayout.addLayout(self.LayoutTargetFolder)
        self.LayoutOutput = QtGui.QHBoxLayout()
        self.LayoutOutput.setObjectName(_fromUtf8("LayoutOutput"))
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.LayoutOutput.addWidget(self.label_3)
        self.EditOutput = QtGui.QLineEdit(self.widget)
        self.EditOutput.setObjectName(_fromUtf8("EditOutput"))
        self.LayoutOutput.addWidget(self.EditOutput)
        self.BtnOutputBrowse = QtGui.QPushButton(self.widget)
        self.BtnOutputBrowse.setObjectName(_fromUtf8("BtnOutputBrowse"))
        self.LayoutOutput.addWidget(self.BtnOutputBrowse)
        self.verticalLayout.addLayout(self.LayoutOutput)
        self.LayoutHashMethod = QtGui.QHBoxLayout()
        self.LayoutHashMethod.setObjectName(_fromUtf8("LayoutHashMethod"))
        self.RadBtnCrc32 = QtGui.QRadioButton(self.widget)
        self.RadBtnCrc32.setChecked(True)
        self.RadBtnCrc32.setObjectName(_fromUtf8("RadBtnCrc32"))
        self.LayoutHashMethod.addWidget(self.RadBtnCrc32)
        self.RadBtnMD5 = QtGui.QRadioButton(self.widget)
        self.RadBtnMD5.setObjectName(_fromUtf8("RadBtnMD5"))
        self.LayoutHashMethod.addWidget(self.RadBtnMD5)
        self.RadBtnSHA1 = QtGui.QRadioButton(self.widget)
        self.RadBtnSHA1.setObjectName(_fromUtf8("RadBtnSHA1"))
        self.LayoutHashMethod.addWidget(self.RadBtnSHA1)
        self.verticalLayout.addLayout(self.LayoutHashMethod)
        self.LayoutExtOnly = QtGui.QHBoxLayout()
        self.LayoutExtOnly.setObjectName(_fromUtf8("LayoutExtOnly"))
        self.ChkBoxExtOnly = QtGui.QCheckBox(self.widget)
        self.ChkBoxExtOnly.setObjectName(_fromUtf8("ChkBoxExtOnly"))
        self.LayoutExtOnly.addWidget(self.ChkBoxExtOnly)
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.LayoutExtOnly.addWidget(self.label_2)
        self.EditExtList = QtGui.QLineEdit(self.widget)
        self.EditExtList.setEnabled(False)
        self.EditExtList.setObjectName(_fromUtf8("EditExtList"))
        self.LayoutExtOnly.addWidget(self.EditExtList)
        self.verticalLayout.addLayout(self.LayoutExtOnly)
        self.TextOutput = QtGui.QTextBrowser(self.widget)
        self.TextOutput.setObjectName(_fromUtf8("TextOutput"))
        self.verticalLayout.addWidget(self.TextOutput)
        self.LayoutStartExitButton = QtGui.QHBoxLayout()
        self.LayoutStartExitButton.setObjectName(_fromUtf8("LayoutStartExitButton"))
        self.BtnStart = QtGui.QPushButton(self.widget)
        self.BtnStart.setObjectName(_fromUtf8("BtnStart"))
        self.LayoutStartExitButton.addWidget(self.BtnStart)
        self.BtnExit = QtGui.QPushButton(self.widget)
        self.BtnExit.setObjectName(_fromUtf8("BtnExit"))
        self.LayoutStartExitButton.addWidget(self.BtnExit)
        self.verticalLayout.addLayout(self.LayoutStartExitButton)
        self.TextOutput.raise_()
        self.label_2.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "FilesInfoReader GUI", None))
        self.label.setText(_translate("Dialog", "TargetFolder", None))
        self.BtnBrowse.setText(_translate("Dialog", "Browse", None))
        self.label_3.setText(_translate("Dialog", "Output", None))
        self.EditOutput.setText(_translate("Dialog", ".\\output.xls", None))
        self.BtnOutputBrowse.setText(_translate("Dialog", "Browse", None))
        self.RadBtnCrc32.setText(_translate("Dialog", "CRC32", None))
        self.RadBtnMD5.setText(_translate("Dialog", "MD5", None))
        self.RadBtnSHA1.setText(_translate("Dialog", "SHA1", None))
        self.ChkBoxExtOnly.setText(_translate("Dialog", "Ext Only", None))
        self.label_2.setText(_translate("Dialog", "Extensions", None))
        self.TextOutput.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
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

