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
from collections import OrderedDict
import xlsxwriter
from mailmerge import MailMerge

STDOUT_SEPARATOR_CHAR='|'

class FilesInfoDB:
    """
    File 정보를 임시적으로 내부 {}에 저장한다.
    csv, excel 등의 포맷으로 저장하는 역할을 한다.
    """
    def __init__(self, columns):
        self.__cols = columns
        self.__db = {}

    def get_db(self):
        return self.__db

    def insert(self, file_name, cols):
        """
        file_name을 key로, cols를 value로 내부 {} 에 저장한다.

        :param file_name:
        :param cols:
        :return:
        """
        self.__db[file_name] = [file_name, cols]

    def to_csv(self, file_name):
        """
        내부 저장하고 있는 정보들을 csv(또는 excel)로 저장한다.

        :param file_name:
        :return:
        """
        # sort db and save into sorted_db
        sorted_db_list = sorted(sorted(self.__db.items(), key=lambda x: x[0]))
        sorted_db = OrderedDict(sorted_db_list)

        wbk = xlsxwriter.Workbook(file_name)
        sheet = wbk.add_worksheet("Result")

        # make heading
        sheet.write(0, 0, "File Full Name")
        index = 1
        for col in self.__cols:
            sheet.write(0, index, col)
            index = index + 1

        # write data
        row = 1
        for (a_file, a_file_data) in sorted_db.items():
            sheet.write(row, 0, a_file)

            index = 1
            for col in a_file_data[1]:
                sheet.write(row, index, col)
                index = index + 1

            row = row + 1

        wbk.close()

    def to_word(self, file_name):
        """
        Word 파일로 저장한다.
        """
        template = "output_word_template.docx"

        document = MailMerge(template)

        # sort db and save into sorted_db
        sorted_db_list = sorted(sorted(self.__db.items(), key=lambda x: x[0]))
        sorted_db = OrderedDict(sorted_db_list)

        merge_folder_item = {}
        for (a_file, a_file_data) in sorted_db.items():
            merge_item = {}
            merge_item["SPS_File_Name"] = a_file_data[1][0]
            merge_item["SPS_File_MTime"] = a_file_data[1][2]
            merge_item["SPS_File_Hash"] = a_file_data[1][3]
            merge_item["SPS_File_Size"] = str(a_file_data[1][4])
            merge_item["SPS_File_LOC"] = str(a_file_data[1][5])

            try:
                merge_folder_item[a_file_data[1][1]].append(merge_item)
            except:
                merge_folder_item[a_file_data[1][1]] = []
                merge_folder_item[a_file_data[1][1]].append(merge_item)

        all_merge = []
        for (a_folder, a_merge_data) in merge_folder_item.items():
            d = {}
            d["SPS_Folder_Name"] = a_folder
            d["SPS_File_Name"] = a_merge_data
            all_merge.append(d)

        document.merge_pages(all_merge)

        document.write(file_name)

    def to_stdout(self, file_name):
        """
        내부 저장하고 있는 정보들을 stdout 으로 출력한다.

        :param file_name:
        :return:
        """
        # sort db and save into sorted_db
        sorted_db_list = sorted(sorted(self.__db.items(), key=lambda x: x[0]))
        sorted_db = OrderedDict(sorted_db_list)

        print("File Full Name", end=STDOUT_SEPARATOR_CHAR)
        for col in self.__cols:
            print("%s"%(col), end=STDOUT_SEPARATOR_CHAR)
        print("")

        for (a_file, a_file_data) in sorted_db.items():
            print("%s"%(a_file), end=STDOUT_SEPARATOR_CHAR)

            for col in a_file_data[1]:
                print("%s"%(col), end=STDOUT_SEPARATOR_CHAR)
            print("")