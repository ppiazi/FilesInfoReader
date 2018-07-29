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
import unittest

from fir.FileInfo import *

TEST_TARGET1 = r".\test\test1.xml"
TEST_TARGET2 = r".\test\test_FileInfo.py"
TEST_TARGET3 = r".\test\nofile.cPp"

class test_FileInfo(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_init(self):
        sut = FileInfo(TEST_TARGET1)
        assert(sut.__file_info["FilePath"] == TEST_TARGET1)
        assert(sut.__file_info["FileSize"] == 0)
        assert(sut.file_type == FILE_TYPE_NORMAL)

    def test_check_file_type_source_code(self):
        sut = FileInfo(TEST_TARGET3)
        sut.check_file_type()
        assert(sut.file_type == FILE_TYPE_SOURCECODE)

    def test_check_file_type_no_source_code(self):
        sut = FileInfo(TEST_TARGET1)
        sut.check_file_type()
        assert(sut.file_type == FILE_TYPE_NORMAL)

    def test_get_file_ext_1(self):
        sut = FileInfo(TEST_TARGET1)
        _ext = sut.get_file_ext()
        assert(_ext == ".xml")

    def test_get_file_ext_2(self):
        sut = FileInfo(TEST_TARGET3)
        _ext = sut.get_file_ext()
        assert(_ext == ".cPp")
 
    def test_read_info_1(self):
        sut = FileInfo(TEST_TARGET1)
        sut.read_info()
        assert(sut.get_size() != 0)
        assert(sut.get_mtime() != 0)
        assert(sut.get_line_count() == 0)

    def test_read_info_2(self):
        sut = FileInfo(TEST_TARGET2)
        sut.read_info()
        assert(sut.get_size() != 0)
        assert(sut.get_mtime() != 0)
        assert(sut.get_line_count() != 0)

if __name__ == "__main__":
    unittest.main()