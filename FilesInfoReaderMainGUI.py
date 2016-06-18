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
import os
import qt4.MainDlg
from PySide import QtCore, QtGui
import FileInfo
import FilesInfoReader
import FilesInfoReaderMain

class FilesInfoReaderMainGUI(QtGui.QDialog, qt4.MainDlg.Ui_Dialog):
    def __init__(self, parent=None):
        super(FilesInfoReaderMainGUI, self).__init__(parent)
        self.setupUi(self)
        self.BtnBrowse.clicked.connect(self.showTargetFolderDlg)
        self.BtnOutputBrowse.clicked.connect(self.showOutputFileDlg)
        self.BtnStart.clicked.connect(self.readInfo)
        self.BtnExit.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.ChkBoxExtOnly.stateChanged.connect(self.changeExtOnly)
        self.EditSourceExtList.setText(",".join(FileInfo.SOURCE_CODE_EXT))
        self.EditExtList.setText(",".join(FilesInfoReader.SEARCH_TARGET_EXT))
        self.EditOutput.setText("output.xlsx")
        self.RadBtnHashGroup = QtGui.QButtonGroup()
        self.RadBtnHashGroup.addButton(self.RadBtnCrc32)
        self.RadBtnHashGroup.addButton(self.RadBtnMD5)
        self.RadBtnHashGroup.addButton(self.RadBtnSHA1)
        self.setWindowTitle("FilesInfoReader - %s" % (FilesInfoReaderMain.__version__))
        self._extonly_flag = False

    def changeExtOnly(self, state):
        if state == QtCore.Qt.Checked:
            self.EditExtList.setEnabled(True)
            self._extonly_flag = True
        else:
            self.EditExtList.setEnabled(False)
            self._extonly_flag = False

    def showTargetFolderDlg(self):
        folder = QtGui.QFileDialog.getExistingDirectory(self, "Select Folder")
        self.EditTargetFolder.setText(folder)

    def showOutputFileDlg(self):
        output_file, tmp = QtGui.QFileDialog.getSaveFileName(self, "Output File")
        self.EditOutput.setText(output_file)

    def readInfo(self):
        # check target folder validation
        target_folder = self.EditTargetFolder.text()
        if os.path.exists(target_folder) == False:
            self._warning("Invalid target folder")
            return
        # check ext only option
        ext_only = False
        if self._extonly_flag == True:
            ext_only = True
            try:
                ext_list = self.EditExtList.text().split(",")
            except:
                self._warning("Invalid ext list")
                return
            FilesInfoReader.SEARCH_TARGET_EXT = ext_list

        # check source code ext option
        try:
            src_ext_list = self.EditSourceExtList.text().split(",")
        except:
            self._warning("Invalid source ext list")
            return
        FileInfo.SOURCE_CODE_EXT = src_ext_list

        # check hash method
        if self.RadBtnCrc32.isChecked() == True:
            hash_method = "crc32"
        elif self.RadBtnMD5.isChecked() == True:
            hash_method = "md5"
        elif self.RadBtnSHA1.isChecked() == True:
            hash_method = "sha1"
        else:
            hash_method = "crc32"

        fir = FilesInfoReader.FilesInfoReader(hash_method)
        fir.setRootPath(target_folder)
        fir.iterate(ext_only)
        fir.saveAsCsv(self.EditOutput.text())
        self._info("Done")

    def _warning(self, msg):
        QtGui.QMessageBox.question(self, "Warning", msg, QtGui.QMessageBox.Yes)

    def _info(self, msg):
        QtGui.QMessageBox.question(self, "Info", msg, QtGui.QMessageBox.Yes)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    diag = FilesInfoReaderMainGUI()
    diag.show()
    sys.exit(app.exec_())