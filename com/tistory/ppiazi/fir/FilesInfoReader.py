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
import logging
import logging.handlers
import os
import os.path
import re

from com.tistory.ppiazi.fir.FilesInfoDB import FilesInfoDB
from com.tistory.ppiazi.fir.ClocXmlParser import ClocXmlParser

from com.tistory.ppiazi.fir import FileInfo

__author__ = 'ppiazi'

SEARCH_TARGET_EXT = FileInfo.SOURCE_CODE_EXT
IGNORE_SEARCH_PATTERN = "\.git"

FIELDS_COMULMNS_NORMAL = ["FileName", "Folder", "MTime", "CheckSum", "Size", "LineCount"]
FIELDS_COMULMNS_CLOC = ["FileName", "Folder", "MTime", "CheckSum", "Size", "LineCount", "Blank", "Comment"]

class FilesInfoReader:
    """
    root_path로 지정된 곳의 파일들을 읽어 저장하고, 원하는 포맷으로 파일을 생성하기 위한 클래스.
    """
    def __init__(self, hash_code="crc32", loc_normal_type=True):
        self.loc_normal_type = loc_normal_type
        if self.loc_normal_type == True:
            selected_columns = FIELDS_COMULMNS_NORMAL
        else:
            selected_columns = FIELDS_COMULMNS_CLOC

        self.file_info_list = FilesInfoDB(columns=selected_columns)
        self.flag_modified_date = True
        self.flag_check_sum = True
        self.root_path = None

        if hash_code == "md5":
            self.hash_code = FileInfo.HASH_CODE_MD5
        elif hash_code == "sha1":
            self.hash_code = FileInfo.HASH_CODE_SHA1
        else:
            self.hash_code = FileInfo.HASH_CODE_CRC32

        # Setting up logging module
        logging.basicConfig(level=logging.DEBUG)
        self.logger = logging.getLogger("FilesInfoReader")
        self.igr_pattern = IGNORE_SEARCH_PATTERN

    def set_ignore_pattern(self, igr_pattern):
        self.igr_pattern = igr_pattern

    def get_path_ignore_pattern(self):
        return self.igr_pattern

    def set_root_path(self, root_path):
        """
        Set the root path to be iterated

        :param root_path:
        :return:
        """
        self.root_path = root_path

    def start_cloc(self):
        """
        cloc target folder

        :return:
        """
        cloc_parser = ClocXmlParser()
        ret = cloc_parser.executeCloc(self.root_path)
        self.line_info = cloc_parser.parseXml(r".\temp_cloc.xml")


    def iterate(self, ext_only=False, igr_enabled=False):
        """
        Start to iterate folders and gather file information.

        :param ext_only:
        :return:
        """
        re_igr_pattern = re.compile(self.igr_pattern)

        if self.loc_normal_type == False:
            self.logger.info("Starting CLOC")
            self.start_cloc()
            self.logger.info("Done")

        for (root, _, files) in os.walk(self.root_path):
            log_str = "Entering %s " % (root)
            self.logger.info(log_str)

            for afile in files:
                log_str = "\tReading file info : %s" % afile
                self.logger.info(log_str)
                full_file_name = os.path.join(root, afile)

                file_info = FileInfo.FileInfo(full_file_name)

                if igr_enabled == True:
                    m = re_igr_pattern.search(full_file_name)
                    if m != None:
                        self.logger.info("\tPath Pattern Ignored : %s" % root)
                        continue

                if ext_only and file_info.get_file_ext().lower() not in SEARCH_TARGET_EXT:
                    self.logger.info("\tExtension Ignored : %s" % afile)
                    continue

                folder_name, file_name = os.path.split(full_file_name)

                try:
                    file_info.read_info(self.hash_code)

                    check_sum = file_info.get_checksum()
                    modified_time_str = file_info.get_mtime()
                    file_size = file_info.get_size()
                    if file_info.get_line_count() == 0 or self.loc_normal_type == True:
                        source_code_line_count = file_info.get_line_count()
                        source_code_comment_count = 0
                        source_code_blank_count = 0
                    else:
                        try:
                            source_code_line_count = self.line_info[full_file_name]["code"]
                            source_code_comment_count = self.line_info[full_file_name]["comment"]
                            source_code_blank_count = self.line_info[full_file_name]["blank"]
                        except Exception as e:
                            self.logger.warning("\tNot Found in cloc : " + str(e))
                            source_code_line_count = file_info.get_line_count()
                            source_code_comment_count = 0
                            source_code_blank_count = 0
                except Exception as e:
                    self.logger.error("\tException : " + str(e))
                    check_sum = str(e)
                    modified_time_str = str(e)
                    file_size = 0
                    source_code_line_count = 0
                    source_code_comment_count = 0
                    source_code_blank_count = 0

                # columns=["FileName", "Folder", "MTime", "CheckSum", "Size", "LineCount"]
                if self.loc_normal_type == True:
                    self.file_info_list.insert(full_file_name,
                                               [file_name, folder_name, modified_time_str, check_sum,
                                                file_size, source_code_line_count])
                else:
                    self.file_info_list.insert(full_file_name,
                                               [file_name, folder_name, modified_time_str, check_sum,
                                                file_size, source_code_line_count, source_code_comment_count, source_code_blank_count])

    def save(self, file_name):
        """
        Save data as a csv fie

        :param file_name:
        :return:
        """

        if file_name == "stdout":
            self.file_info_list.to_stdout(file_name)

        extension = os.path.splitext(file_name)[1]
        if extension != ".xlsx" :
            file_name = file_name + ".xlsx"

        self.file_info_list.to_csv(file_name)
