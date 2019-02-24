from tkinter import filedialog
from tkinter import *
from tkinter.ttk import *

ENTRY_WIDTH_1 = 50
ENTRY_WIDTH_2 = 50
BUTTON_WIDTH = 10

class TkUi_Frame(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

    def handle_btn_target_folder_brw(self):
        pass

    def handle_cmb_output_file(self):
        pass

    def handle_btn_exit(self):
        pass

    def handle_btn_start(self):
        pass

    def handle_chk_ignroe_ptrn(self):
        pass

    def handle_chk_extension_only(self):
        pass

    def handle_chk_cloc(self):
        pass

    def set_entry_text(self, target, text):
        target.delete(0, END)
        target.insert(0, text)

    def disable_all(self):
        for item in self.ui_handle_list:
            item.config(state=DISABLED)

    def enable_all(self):
        for item in self.ui_handle_list:
            item.config(state=NORMAL)

    def initUI(self, master):
        self.master = master
        self.columnconfigure(1, pad=5, weight=1)

        self.ui_handle_list = []

        # Target Folder Frame
        self.frm_main = Frame(self)
        self.frm_main.pack(fill=X)

        self.lbl_target_folder = Label(self.frm_main, text="Target Folder")
        self.lbl_target_folder.grid(row=0, column=0)

        self.entry_target_folder = Entry(self.frm_main, width=ENTRY_WIDTH_1)
        self.entry_target_folder.grid(row=0, column=1, sticky=W + E)

        self.btn_target_folder_brw = Button(self.frm_main, text ="Browse", width=BUTTON_WIDTH, command=self.handle_btn_target_folder_brw)
        self.btn_target_folder_brw.grid(row=0, column=2, sticky=W + E)

        self.ui_handle_list.append(self.entry_target_folder)
        self.ui_handle_list.append(self.btn_target_folder_brw)

        # Output File Frame
        self.frm_output_file = Frame(self)
        self.frm_output_file.pack(fill=X)

        self.lbl_output_file = Label(self.frm_main, text="Output File", )
        self.lbl_output_file.grid(row=1, column=0)

        self.entry_output_file = Entry(self.frm_main, width=ENTRY_WIDTH_1)
        self.entry_output_file.grid(row=1, column=1)
        self.entry_output_file.config(state=DISABLED)

        self.cmb_output_file = Combobox(self.frm_main, width=BUTTON_WIDTH, state="readonly")
        self.cmb_output_file['values'] = ("Excel", "Word")
        self.cmb_output_file.current(0)
        self.cmb_output_file .grid(row=1, column=2, sticky=W + E)

        self.ui_handle_list.append(self.entry_output_file)
        self.ui_handle_list.append(self.cmb_output_file)

        # Hash Type Frame
        self.lbl_hash_type = Label(self.frm_main, text="Hash Type")
        self.lbl_hash_type.grid(row=2, column=0)

        frm_hash = Frame(self.frm_main)
        frm_hash.grid(row=2, column=1)

        self.state_hash_type = IntVar()
        self.rb_hash_type1 = Radiobutton(frm_hash, text ="CRC32", value = 1, variable = self.state_hash_type)
        self.rb_hash_type2 = Radiobutton(frm_hash, text ="MD5", value=2, variable = self.state_hash_type)
        self.rb_hash_type3 = Radiobutton(frm_hash, text ="SHA1", value=3, variable = self.state_hash_type)
        self.rb_hash_type1.grid(row=0, column=0)
        self.rb_hash_type2.grid(row=0, column=1)
        self.rb_hash_type3.grid(row=0, column=2)

        self.ui_handle_list.append(self.rb_hash_type1)
        self.ui_handle_list.append(self.rb_hash_type2)
        self.ui_handle_list.append(self.rb_hash_type3)

        # Source Ext Frame
        self.lbl_source_ext = Label(self.frm_main, text="Source Extension")
        self.lbl_source_ext.grid(row=3, column=0)

        self.entry_source_ext = Entry(self.frm_main, width=ENTRY_WIDTH_2)
        self.entry_source_ext.grid(row=3, column=1, sticky=W + E)

        self.ui_handle_list.append(self.entry_source_ext)

        # Ignore Pattern Frame
        self.frm_ignore_ptrn = Frame(self)
        self.frm_ignore_ptrn .pack(fill=X)

        self.state_ignore_ptrn = BooleanVar()
        self.state_ignore_ptrn.set(False)
        self.chk_ignroe_ptrn = Checkbutton(self.frm_main, text="Ignore Pattern(re)", var=self.state_ignore_ptrn, command=self.handle_chk_ignroe_ptrn)
        self.chk_ignroe_ptrn.grid(row=4, column=0)

        self.entry_ignore_ptrn = Entry(self.frm_main, width=ENTRY_WIDTH_2)
        self.entry_ignore_ptrn.grid(row=4, column=1)

        self.ui_handle_list.append(self.chk_ignroe_ptrn)
        self.ui_handle_list.append(self.entry_ignore_ptrn)

        # Extension Only Frame
        self.state_extension_only = BooleanVar()
        self.state_extension_only.set(False)
        self.chk_extension_only = Checkbutton(self.frm_main, text="Extension Only", var=self.state_extension_only, command=self.handle_chk_extension_only)
        self.chk_extension_only.grid(row=5, column=0)

        self.entry_extension_only = Entry(self.frm_main, width = ENTRY_WIDTH_2)
        self.entry_extension_only.grid(row=5, column=1)

        self.ui_handle_list.append(self.chk_extension_only)
        self.ui_handle_list.append(self.entry_extension_only)

        # CLOC Frame
        self.state_cloc = BooleanVar()
        self.state_cloc.set(False)
        self.chk_cloc = Checkbutton(self.frm_main, text="CLOC", var=self.state_cloc, command=self.handle_chk_cloc)
        self.chk_cloc.grid(row=6, column=0)

        self.entry_cloc = Entry(self.frm_main, width = ENTRY_WIDTH_2)
        self.entry_cloc.grid(row=6, column=1)

        self.btn_cloc = Button(self.frm_main, text="Browse")
        self.btn_cloc.grid(row=6, column=2, sticky=W + E)

        self.ui_handle_list.append(self.chk_cloc)
        self.ui_handle_list.append(self.entry_cloc)
        self.ui_handle_list.append(self.btn_cloc)

        # Control Frame
        tmp_frame = Frame(self.frm_main)
        tmp_frame.grid(row=7, column=0, columnspan=3)

        self.btn_start = Button(tmp_frame, text="Start", command=self.handle_btn_start)
        self.btn_start.pack(side=LEFT, padx=5, pady=5)

        self.btn_exit = Button(tmp_frame, text="Exit", command=self.handle_btn_exit)
        self.btn_exit.pack(side=RIGHT, padx=5, pady=5)

        self.ui_handle_list.append(self.btn_start)
        self.ui_handle_list.append(self.btn_exit)

        # Pack
        self.pack(fill=BOTH, expand=True, padx=5, pady=5)

if __name__ == "__main__":
    root = Tk()
    app = TkUi_Frame(root)
    root.mainloop()
