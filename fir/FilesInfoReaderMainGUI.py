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

import configparser
import os
import sys

try:
    from PySide2 import QtCore, QtGui, QtWidgets
except:
    from PyQt2 import QtCore, QtGui, QtWidgets

import FileInfo
import FilesInfoReaderMain
import FilesInfoReader
import qt4.MainDlg

CONFIG_FILE = "config.ini"

class FirWorksDoneSignal(QtCore.QObject):
    sig = QtCore.Signal(str)

class FirWorker(QtCore.QThread):
    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.running = False
        self.signal = FirWorksDoneSignal()

    def set_data(self, fir_ins, ext_only, igr_enabled, line_info = None):
        self.fir_ins = fir_ins
        self.ext_only = ext_only
        self.igr_enabled = igr_enabled
        self.line_info = line_info

    def run(self):
        try:
            self.fir_ins.iterate(self.ext_only, self.igr_enabled, self.line_info)
            self.signal.sig.emit("DONE")
        except Exception as e:
            self.signal.sig.emit(str(e))

class FilesInfoReaderMainGUI(QtWidgets.QDialog, qt4.MainDlg.Ui_Dialog):
    """
    GUI 버전 FilesInfoReader
    """
    def __init__(self, parent=None):
        super(FilesInfoReaderMainGUI, self).__init__(parent)
        self.setupUi(self)

        # Set application icon
        self.setWindowIcon(QtGui.QIcon(r"..\icon.ico"))

        # 설정 파일을 읽는다.
        self._load_config()

        # UI 전체 enable / disable을 위한 container를 생성한다.
        self._ui_handles = {}

        self.BtnBrowse.clicked.connect(self.show_target_folder_dlg)
        self.BtnOutputBrowse.clicked.connect(self.show_output_file_dlg)
        self.BtnClocPathBrowse.clicked.connect(self.show_cloc_path_dlg)
        self.BtnStart.clicked.connect(self.read_info)
        self.BtnExit.clicked.connect(self.close_app)
        self.ChkBoxExtOnly.stateChanged.connect(self.change_ext_only)

        self._ui_handles["BtnBrowse"] = self.BtnBrowse
        self._ui_handles["BtnOutputBrowse"] = self.BtnOutputBrowse
        self._ui_handles["BtnClocPathBrowse"] = self.BtnClocPathBrowse
        self._ui_handles["BtnStart"] = self.BtnStart
        self._ui_handles["BtnExit"] = self.BtnExit
        self._ui_handles["ChkBoxExtOnly"] = self.ChkBoxExtOnly

        self.EditSourceExtList.setText(self._config.get("SETTING", "source_ext_list", fallback=",".join(
            FileInfo.SOURCE_CODE_EXT)))
        self.EditExtList.setText(self._config.get("SETTING", "search_ext_list", fallback=",".join(
            FilesInfoReader.SEARCH_TARGET_EXT)))
        self.EditOutput.setText(self._config.get("SETTING", "output_file",fallback="output.xlsx"))
        self.EditIgnorePattern.setText(self._config.get("SETTING", "ignore_pattern", fallback=FilesInfoReader.IGNORE_SEARCH_PATTERN))
        self.EditTargetFolder.setText(self._config.get("SETTING", "target_folder", fallback=""))
        self.EditClocPath.setText(self._config.get("SETTING", "cloc_path", fallback=""))

        self._ui_handles["EditSourceExtList"]  = self.EditSourceExtList
        #self._ui_handles["EditExtList"]  = self.EditExtList
        self._ui_handles["EditOutput"]  = self.EditOutput
        #self._ui_handles["EditIgnorePattern"]  = self.EditIgnorePattern
        self._ui_handles["EditTargetFolder"]  = self.EditTargetFolder
        #self._ui_handles["EditClocPath"]  = self.EditClocPath

        self.ChkBoxIgnore.stateChanged.connect(self.change_ignore)
        self.ChkBoxClocUse.stateChanged.connect(self.change_cloc_use)
        self.RadBtnHashGroup = QtWidgets.QButtonGroup()
        self.RadBtnHashGroup.addButton(self.RadBtnCrc32)
        self.RadBtnHashGroup.addButton(self.RadBtnMD5)
        self.RadBtnHashGroup.addButton(self.RadBtnSHA1)
        self.setWindowTitle("FilesInfoReader - %s by ppiazi" % (FilesInfoReaderMain.__version__))

        self._ui_handles["ChkBoxIgnore"] = self.ChkBoxIgnore
        self._ui_handles["ChkBoxClocUse"] = self.ChkBoxClocUse
        self._ui_handles["RadBtnCrc32"] = self.RadBtnCrc32
        self._ui_handles["RadBtnMD5"] = self.RadBtnMD5
        self._ui_handles["RadBtnSHA1"] = self.RadBtnSHA1

        self._extonly_flag = False
        self._igr_enabled_flag = False
        self._cloc_use_flag = False

        self._worker = FirWorker()
        self._worker.signal.sig.connect(self._check_worker)
        
        self.setFixedSize(self.size())

    def close_app(self):
        # before close, try to save current status into config.ini
        f = open(CONFIG_FILE, "w")
        try:
            self._config.add_section("SETTING")
        except Exception as e:
            print(str(e))
        self._config.set("SETTING", "source_ext_list", self.EditSourceExtList.text())
        self._config.set("SETTING", "search_ext_list", self.EditExtList.text())
        self._config.set("SETTING", "output_file", self.EditOutput.text())
        self._config.set("SETTING", "ignore_pattern", self.EditIgnorePattern.text())
        self._config.set("SETTING", "target_folder", self.EditTargetFolder.text())
        self._config.set("SETTING", "cloc_path", self.EditClocPath.text())
        self._config.write(f)

        print("CONFIG saved\n")
        f.close()

        QtCore.QCoreApplication.instance().quit()

    def _load_config(self):
        self._config = configparser.ConfigParser()
        self._config.read(CONFIG_FILE)


    def change_ignore(self, state):
        """
        Ignore 체크 버튼 이벤트를 처리한다.
        :param state:
        :return:
        """
        if state == QtCore.Qt.Checked:
            self._ui_handles["EditIgnorePattern"] = self.EditIgnorePattern
            self.EditIgnorePattern.setEnabled(True)
            self._igr_enabled_flag = True
        else:
            self._ui_handles["EditIgnorePattern"] = None
            self.EditIgnorePattern.setEnabled(False)
            self._igr_enabled_flag = False

    def change_cloc_use(self, state):
        """
        CLOC 사용여부 체크 버튼 이벤트를 처리한다.
        :param state:
        :return:
        """
        if state == QtCore.Qt.Checked:
            self._ui_handles["BtnClocPathBrowse"] = self.BtnClocPathBrowse
            self.BtnClocPathBrowse.setEnabled(True)
            #self.EditClocPath.setEnabled(True)
            self._cloc_use_flag = True
        else:
            self._ui_handles["BtnClocPathBrowse"] = None
            self.BtnClocPathBrowse.setEnabled(False)
            #self.EditClocPath.setEnabled(False)
            self._cloc_use_flag = False

    def change_ext_only(self, state):
        """
        ExtOnly 체크 버튼 이벤트를 처리한다.
        :param state:
        :return:
        """
        if state == QtCore.Qt.Checked:
            self._ui_handles["EditExtList"] = self.EditExtList
            self.EditExtList.setEnabled(True)
            self._extonly_flag = True
        else:
            self._ui_handles["EditExtList"] = None
            self.EditExtList.setEnabled(False)
            self._extonly_flag = False

    def show_target_folder_dlg(self):
        """
        타켓 폴더 지정 버튼 이벤트 처리한다.
        :return:
        """
        folder = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Folder")
        self.EditTargetFolder.setText(folder)

    def show_output_file_dlg(self):
        """
        아웃풋 폴더 지정 버튼 이벤트를 처리한다.
        :return:
        """
        output_file, tmp = QtWidgets.QFileDialog.getSaveFileName(self, "Output File", "output.xlsx", filter="*.xlsx")
        if output_file == "":
            output_file = "output.xlsx"
        self.EditOutput.setText(output_file)

    def show_cloc_path_dlg(self):
        """
        CLOC 파일 지정 버튼 이벤트를 처리한다.
        :return:
        """
        output_file, tmp = QtWidgets.QFileDialog.getOpenFileName(self, "CLOC File")
        self.EditClocPath.setText(output_file)

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

        self.fir = FilesInfoReader.FilesInfoReader(hash_method, self._cloc_use_flag)

        self.fir.set_root_path(target_folder)
        if igr_enabled == True:
            self.fir.set_ignore_pattern(self.EditIgnorePattern.text())

        if self._cloc_use_flag == False:
            line_info = None
        else:
            p_use_cloc_path = self.EditClocPath.text()
            line_info = self.fir.start_cloc(p_use_cloc_path)

        #start fir.iterate
        self._worker.set_data(self.fir, ext_only, igr_enabled, line_info)
        self._all_disable()
        self._worker.start()   

    def _all_disable(self):
        for v in self._ui_handles.values():
            if v != None:
                v.setEnabled(False)

    def _all_enable(self):
        for v in self._ui_handles.values():
            if v != None:
                v.setEnabled(True)

    def _check_worker(self, end_status):
        if end_status == "DONE":
            try:
                self.fir.save(self.EditOutput.text())
            except Exception as e:
                self._warning("Error to save output : " + str(e))
            else:
                self._info("Done")
        else:
            self._warning("Error to iterate files : " + end_status)
        self._all_enable()

    def _warning(self, msg):
        """
        Warning 정보 표시
        :param msg:
        :return:
        """
        QtWidgets.QMessageBox.question(self, "Warning", msg, QtWidgets.QMessageBox.Yes)

    def _info(self, msg):
        """
        Info 정보 표시
        :param msg:
        :return:
        """
        QtWidgets.QMessageBox.question(self, "Info", msg, QtWidgets.QMessageBox.Yes)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    diag = FilesInfoReaderMainGUI()
    diag.show()
    sys.exit(app.exec_())
