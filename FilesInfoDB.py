import xlwt
from collections import OrderedDict

class FilesInfoDB:
    def __init__(self, columns=[]):
        self.cols = columns
        self.db = {}

    def insert(self, file_name, cols):
        self.db[file_name] = [file_name, cols]

    def to_csv(self, file_name):
        # sort db and save into sorted_db
        sorted_db_list = sorted(sorted(self.db.items(), key=lambda x : x[0]))
        sorted_db = OrderedDict(sorted_db_list)

        wbk = xlwt.Workbook()
        sheet = wbk.add_sheet("Result", cell_overwrite_ok=True)

        # make heading
        sheet.write(0, 0, "File Full Name")
        i = 1
        for col in self.cols:
            sheet.write(0, i, col)
            i = i + 1

        # write data
        r = 1
        for (a_file,a_file_data) in sorted_db.items():
            sheet.write(r, 0, a_file)

            i = 1
            for col in a_file_data[1]:
                sheet.write(r, i, col)
                i = i + 1

            r = r + 1

        wbk.save(file_name)