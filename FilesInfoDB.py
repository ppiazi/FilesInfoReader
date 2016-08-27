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

class FilesInfoDB:
    """
    File 정보를 임시적으로 내부 {}에 저장한다.
    csv, excel 등의 포맷으로 저장하는 역할을 한다.
    """
    def __init__(self, columns):
        self.__cols = columns
        self.__db = {}

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
