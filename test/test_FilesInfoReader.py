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

from fir.FilesInfoReader import *

class test_FilesInfoReader(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_iterate(self):
        p_cloc = False
        p_sourcecode_only = True
        p_igr_enabled = True
        fir = FilesInfoReader("crc32", p_cloc)
        fir.set_root_path(r"./test")
        fir.iterate(p_sourcecode_only, p_igr_enabled)
        file_info_db = fir.get_file_info_db()
        assert(len(file_info_db.get_db()) != 0)

if __name__ == "__main__":
    unittest.main()