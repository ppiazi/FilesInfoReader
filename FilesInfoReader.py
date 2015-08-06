import os
import time
import hashlib
import pandas as pd

__author__ = 'ppiazi'

class FilesInfoReader:
    def __init__(self):
        self.file_info_list = pd.DataFrame(columns=["CheckSum", "MTime", "Size"])
        self.FlagModifiedDate = True
        self.FlagCheckSum = True

    def setRootPath(self, rootPath):
        self.rootPath = rootPath

    def iterate(self):
        for (root, dirs, files) in os.walk(self.rootPath):
            print("Entering %s " % (root))

            for afile in files:
                print("\tReading file info : %s ... " % afile, end=" ")
                full_file_name = os.path.join(root, afile)
                check_sum = self.getFileCheckSum(full_file_name)
                modified_time_str = self.getFileMTime(full_file_name)
                file_size = self.getFileSize(full_file_name)
                print("done")

                self.file_info_list.loc[full_file_name] = [check_sum, modified_time_str, file_size]

    def getFileCheckSum(self, file_name):
        f = open(file_name, "rb")
        check_sum = hashfile(f, hashlib.sha256())
        f.close()
        return check_sum

    def getFileMTime(self, file_name):
        mtime = os.path.getmtime(file_name)
        t = time.gmtime(mtime)
        mtime_str = time.strftime("%Y-%m-%d %H:%M:%S", t)
        return mtime_str

    def getFileSize(self, file_name):
        statinfo = os.stat(file_name)
        return statinfo.st_size

    def printAll(self):
        for index, afile_info in self.file_info_list.iterrows():
            print("%s %s %s %d" % (index, afile_info["CheckSum"], afile_info["MTime"], afile_info["Size"]))

    def saveAsCsv(self, file_name):
        self.file_info_list.to_csv(file_name)

def hashfile(afile, hasher, blocksize=65535):
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    return hasher.hexdigest()
