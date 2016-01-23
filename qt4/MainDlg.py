# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainDlg.ui'
#
# Created: Sat Jan 23 21:22:01 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(501, 539)
        self.layoutWidget = QtGui.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 479, 521))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.LayoutTargetFolder = QtGui.QHBoxLayout()
        self.LayoutTargetFolder.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.LayoutTargetFolder.setObjectName("LayoutTargetFolder")
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.LayoutTargetFolder.addWidget(self.label)
        self.EditTargetFolder = QtGui.QLineEdit(self.layoutWidget)
        self.EditTargetFolder.setObjectName("EditTargetFolder")
        self.LayoutTargetFolder.addWidget(self.EditTargetFolder)
        self.BtnBrowse = QtGui.QPushButton(self.layoutWidget)
        self.BtnBrowse.setObjectName("BtnBrowse")
        self.LayoutTargetFolder.addWidget(self.BtnBrowse)
        self.verticalLayout.addLayout(self.LayoutTargetFolder)
        self.LayoutOutput = QtGui.QHBoxLayout()
        self.LayoutOutput.setObjectName("LayoutOutput")
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.LayoutOutput.addWidget(self.label_3)
        self.EditOutput = QtGui.QLineEdit(self.layoutWidget)
        self.EditOutput.setText("")
        self.EditOutput.setObjectName("EditOutput")
        self.LayoutOutput.addWidget(self.EditOutput)
        self.BtnOutputBrowse = QtGui.QPushButton(self.layoutWidget)
        self.BtnOutputBrowse.setObjectName("BtnOutputBrowse")
        self.LayoutOutput.addWidget(self.BtnOutputBrowse)
        self.verticalLayout.addLayout(self.LayoutOutput)
        self.LayoutHashMethod = QtGui.QHBoxLayout()
        self.LayoutHashMethod.setObjectName("LayoutHashMethod")
        self.RadBtnCrc32 = QtGui.QRadioButton(self.layoutWidget)
        self.RadBtnCrc32.setChecked(True)
        self.RadBtnCrc32.setObjectName("RadBtnCrc32")
        self.LayoutHashMethod.addWidget(self.RadBtnCrc32)
        self.RadBtnMD5 = QtGui.QRadioButton(self.layoutWidget)
        self.RadBtnMD5.setObjectName("RadBtnMD5")
        self.LayoutHashMethod.addWidget(self.RadBtnMD5)
        self.RadBtnSHA1 = QtGui.QRadioButton(self.layoutWidget)
        self.RadBtnSHA1.setObjectName("RadBtnSHA1")
        self.LayoutHashMethod.addWidget(self.RadBtnSHA1)
        self.verticalLayout.addLayout(self.LayoutHashMethod)
        self.LayoutExtOnly = QtGui.QHBoxLayout()
        self.LayoutExtOnly.setObjectName("LayoutExtOnly")
        self.ChkBoxExtOnly = QtGui.QCheckBox(self.layoutWidget)
        self.ChkBoxExtOnly.setObjectName("ChkBoxExtOnly")
        self.LayoutExtOnly.addWidget(self.ChkBoxExtOnly)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.LayoutExtOnly.addWidget(self.label_2)
        self.EditExtList = QtGui.QLineEdit(self.layoutWidget)
        self.EditExtList.setEnabled(False)
        self.EditExtList.setObjectName("EditExtList")
        self.LayoutExtOnly.addWidget(self.EditExtList)
        self.verticalLayout.addLayout(self.LayoutExtOnly)
        self.TextOutput = QtGui.QTextBrowser(self.layoutWidget)
        self.TextOutput.setObjectName("TextOutput")
        self.verticalLayout.addWidget(self.TextOutput)
        self.LayoutStartExitButton = QtGui.QHBoxLayout()
        self.LayoutStartExitButton.setObjectName("LayoutStartExitButton")
        self.BtnStart = QtGui.QPushButton(self.layoutWidget)
        self.BtnStart.setObjectName("BtnStart")
        self.LayoutStartExitButton.addWidget(self.BtnStart)
        self.BtnExit = QtGui.QPushButton(self.layoutWidget)
        self.BtnExit.setObjectName("BtnExit")
        self.LayoutStartExitButton.addWidget(self.BtnExit)
        self.verticalLayout.addLayout(self.LayoutStartExitButton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "FilesInfoReader GUI", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "TargetFolder", None, QtGui.QApplication.UnicodeUTF8))
        self.BtnBrowse.setText(QtGui.QApplication.translate("Dialog", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.BtnOutputBrowse.setText(QtGui.QApplication.translate("Dialog", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.RadBtnCrc32.setText(QtGui.QApplication.translate("Dialog", "CRC32", None, QtGui.QApplication.UnicodeUTF8))
        self.RadBtnMD5.setText(QtGui.QApplication.translate("Dialog", "MD5", None, QtGui.QApplication.UnicodeUTF8))
        self.RadBtnSHA1.setText(QtGui.QApplication.translate("Dialog", "SHA1", None, QtGui.QApplication.UnicodeUTF8))
        self.ChkBoxExtOnly.setText(QtGui.QApplication.translate("Dialog", "Ext Only", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Extensions", None, QtGui.QApplication.UnicodeUTF8))
        self.TextOutput.setHtml(QtGui.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.BtnStart.setText(QtGui.QApplication.translate("Dialog", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.BtnExit.setText(QtGui.QApplication.translate("Dialog", "Exit", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

