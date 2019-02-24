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

from tkinter import filedialog
from tkinter import *

import fir
from fir.FilesInfoReader import FilesInfoReader
from fir.FilesInfoReader import OUTPUT_TYPE_EXCEL
from fir.FilesInfoReader import OUTPUT_TYPE_WORD
from fir.FileInfo import FileInfo
from fir.tk.TkMainDlg import TkUi_Frame


class FilesInfoReaderMainTkGUI(TkUi_Frame):
    def __init__(self, master):
        TkUi_Frame.__init__(self, master)
        self.initUI(master)

    def handle_btn_target_folder_brw(self):
        print("Open child")
        target_folder = filedialog.askdirectory()
        self.target_folder = target_folder
        self.set_entry_text(self.entry_target_folder, self.target_folder)

    def handle_cmb_output_file(self):
        pass

    def handle_btn_exit(self):
        self.master.destroy()

    def handle_btn_start(self):
        pass

    def handle_chk_ignroe_ptrn(self):
        ret = self.state_ignore_ptrn.get()

        if ret == False:
            self.entry_ignore_ptrn.config(state=DISABLED)
        else:
            self.entry_ignore_ptrn.config(state=NORMAL)

    def handle_chk_extension_only(self):
        ret = self.state_extension_only.get()

        if ret == False:
            self.entry_extension_only.config(state=DISABLED)
        else:
            self.entry_extension_only.config(state=NORMAL)

    def handle_chk_cloc(self):
        ret = self.state_cloc.get()

        if ret == False:
            self.entry_cloc.config(state=DISABLED)
            self.btn_cloc.config(state=DISABLED)
        else:
            self.entry_cloc.config(state=NORMAL)
            self.btn_cloc.config(state=NORMAL)

if __name__ == "__main__":
    root = Tk()
    app = FilesInfoReaderMainTkGUI(root)
    root.mainloop()
