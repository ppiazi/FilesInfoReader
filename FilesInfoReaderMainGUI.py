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
    """
    GUI 버전 FilesInfoReader
    """
    def __init__(self, parent=None):
        super(FilesInfoReaderMainGUI, self).__init__(parent)
        self.setupUi(self)
        self.BtnBrowse.clicked.connect(self.show_target_folder_dlg)
        self.BtnOutputBrowse.clicked.connect(self.show_output_file_dlg)
        self.BtnStart.clicked.connect(self.read_info)
        self.BtnExit.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.ChkBoxExtOnly.stateChanged.connect(self.change_ext_only)
        self.EditSourceExtList.setText(",".join(FileInfo.SOURCE_CODE_EXT))
        self.EditExtList.setText(",".join(FilesInfoReader.SEARCH_TARGET_EXT))
        self.EditOutput.setText("output.xlsx")
        self.EditIgnorePattern.setText(FilesInfoReader.IGNORE_SEARCH_PATTERN)
        self.ChkBoxIgnore.stateChanged.connect(self.change_ignore)
        self.RadBtnHashGroup = QtGui.QButtonGroup()
        self.RadBtnHashGroup.addButton(self.RadBtnCrc32)
        self.RadBtnHashGroup.addButton(self.RadBtnMD5)
        self.RadBtnHashGroup.addButton(self.RadBtnSHA1)
        self.setWindowTitle("FilesInfoReader - %s by ppiazi" % (FilesInfoReaderMain.__version__))
        self._extonly_flag = False
        self._igr_enabled_flag = False

    def change_ignore(self, state):
        """
        Ignore 체크 버튼 이벤트를 처리한다.
        :param state:
        :return:
        """
        if state == QtCore.Qt.Checked:
            self.EditIgnorePattern.setEnabled(True)
            self._igr_enabled_flag = True
        else:
            self.EditIgnorePattern.setEnabled(False)
            self._igr_enabled_flag = False

    def change_ext_only(self, state):
        """
        ExtOnly 체크 버튼 이벤트를 처리한다.
        :param state:
        :return:
        """
        if state == QtCore.Qt.Checked:
            self.EditExtList.setEnabled(True)
            self._extonly_flag = True
        else:
            self.EditExtList.setEnabled(False)
            self._extonly_flag = False

    def show_target_folder_dlg(self):
        """
        타켓 폴더 지정 버튼 이벤트 처리한다.
        :return:
        """
        folder = QtGui.QFileDialog.getExistingDirectory(self, "Select Folder")
        self.EditTargetFolder.setText(folder)

    def show_output_file_dlg(self):
        """
        아웃풋 폴더 지정 버튼 이벤트를 처리한다.
        :return:
        """
        output_file, tmp = QtGui.QFileDialog.getSaveFileName(self, "Output File")
        self.EditOutput.setText(output_file)

    def read_info(self):
        """
        지정된 타켓 폴더의 파일 정보들을 읽는다.
        :return:
        """
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

        # check ignore pattern option
        igr_enabled = self._igr_enabled_flag

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
        fir.set_root_path(target_folder)
        if igr_enabled == True:
            fir.set_ignore_pattern(self.EditIgnorePattern.text())
        fir.iterate(ext_only, igr_enabled)

        try:
            fir.save(self.EditOutput.text())
        except Exception as e:
            self._warning("Error to save output : " + str(e))
        else:
            self._info("Done")

    def _warning(self, msg):
        """
        Warning 정보 표시
        :param msg:
        :return:
        """
        QtGui.QMessageBox.question(self, "Warning", msg, QtGui.QMessageBox.Yes)

    def _info(self, msg):
        """
        Info 정보 표시
        :param msg:
        :return:
        """
        QtGui.QMessageBox.question(self, "Info", msg, QtGui.QMessageBox.Yes)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    diag = FilesInfoReaderMainGUI()
    diag.show()
    sys.exit(app.exec_())
