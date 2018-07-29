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

from fir.ClocXmlParser import ClocXmlParser

TEST_TARGET_NOFILE = r"test\nofile.xml"
TEST_TARGET1 = r"test\test1.xml"
TEST_TARGET2 = r"test\test2.xml"

class ClocXmlParserTest(unittest.TestCase):
    testTarget = None

    def setUp(self):
        cloc_path = r"..\util\cloc.exe"
        self.testTarget = ClocXmlParser(cloc_path)

    def tearDown(self):
        pass

    def test_parseXml_with_data1(self):
        soup = self.testTarget.openXml(TEST_TARGET1)
        assert( soup != None )

    def test_parseXml_with_nofile(self):
        soup = self.testTarget.openXml(TEST_TARGET_NOFILE)
        assert ( soup == None )

    def test_parseXml_normal_data(self):
        file_line_info = self.testTarget.parseXml(TEST_TARGET1)
        assert(len(file_line_info) == 236)
        assert (file_line_info["cloc-1.72\\Unix\\cloc"]["code"] == 8424)
        assert (file_line_info[r"cloc-1.72\tests\inputs\issues\114\bar\bee\inner_most.js"]["blank"] == 0)
        assert (file_line_info[r"cloc-1.72\tests\inputs\issues\132\C-Ansi.c"]["code"] == 7)

    def test_parseXml_normal_data_with_korean_path(self):
        file_line_info = self.testTarget.parseXml(TEST_TARGET2)
        assert (len(file_line_info) == 73)
        assert (file_line_info[r".\새 폴더 (2)\result2.xml"]["code"] == 17)
        assert (file_line_info[r".\새 폴더\호호\한글2.c"]["blank"] == 2)

if __name__ == "__main__":
    unittest.main()