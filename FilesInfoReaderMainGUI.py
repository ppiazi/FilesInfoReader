# -*- coding: utf-8 -*-
"""
Copyright 2015 Joohyun Lee(ppiazi@gmail.com)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import sys
import time
import qt4.MainDlg
from PyQt4 import QtCore, QtGui
import FileInfo

class FilesInfoReaderMainGUI(QtGui.QDialog, qt4.MainDlg.Ui_Dialog):
    def __init__(self, parent=None):
        super(FilesInfoReaderMainGUI, self).__init__(parent)
        self.setupUi(self)
        self.BtnBrowse.clicked.connect(self.showFileBrowserDlg)
        self.BtnStart.clicked.connect(self.readInfo)
        self.BtnExit.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.ChkBoxExtOnly.stateChanged.connect(self.changeExtOnly)
        self.EditExtList.setText(",".join(FileInfo.SOURCE_CODE_EXT))

    def changeExtOnly(self, state):
        if state == QtCore.Qt.Checked:
            self.EditExtList.setEnabled(True)
        else:
            self.EditExtList.setEnabled(False)

    def showFileBrowserDlg(self):
        folder = QtGui.QFileDialog.getExistingDirectory(self, "Select Folder")
        self.TargetFolder = folder
        self.EditTargetFolder.setText(folder)

    def readInfo(self):
        # check target folder validation

        # 

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    diag = FilesInfoReaderMainGUI()
    diag.show()
    sys.exit(app.exec_())