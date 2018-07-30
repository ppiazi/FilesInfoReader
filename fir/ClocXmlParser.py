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
import subprocess
from bs4 import BeautifulSoup

class ClocXmlParser:
    def __init__(self, cloc_path):
        self.cloc_path = cloc_path

    def openXml(self, xml_file):
        """
        open xml_file and make beautifulsoup object with it

        :return:
        """
        try:
            f = open(xml_file, "r")
        except FileNotFoundError as e:
            print(str(e))
            return None

        self.soup = BeautifulSoup(f, "lxml")

        f.close()

        return self.soup

    def executeCloc(self, target_path, output_file=r".\temp_cloc.xml"):
        ret = subprocess.call([self.cloc_path, target_path, "--by-file", "--xml", "--out", output_file, "-q"])
        if ret != 0:
            print("Error at calling cloc\n")
        return ret

    def parseXml(self, xml_file):
        """
        cloc xml 파일을 읽어 dict 형태로 반환한다.

        :return:
        """
        soup = self.openXml(xml_file)
        file_line_info = None

        if soup == None:
            return file_line_info

        file_objects = soup.findAll("file")
        file_line_info = {}

        try:
            for file_object in file_objects:
                fli = {}
                fli["blank"] = int(file_object["blank"])
                fli["comment"] = int(file_object["comment"])
                fli["code"] = int(file_object["code"])
                fli["lang"] = file_object["language"]

                file_line_info[file_object["name"]] = fli
        except Exception as e:
            print(str(e))
            file_line_info = None

        return file_line_info
