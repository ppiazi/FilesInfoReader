import os
import time
import hashlib

__author__ = 'ppiazi'

class FilesInfoReader:
    def __init__(self):
        self.file_info_list = []
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
                modified_time = self.getFileMTime(full_file_name)
                file_size = self.getFileSize(full_file_name)
                print("done")

                afile_info = {}
                afile_info["Name"] = full_file_name
                afile_info["CheckSum"] = check_sum
                afile_info["MTime"] = modified_time
                afile_info["Size"] = file_size

                self.file_info_list.append(afile_info)

    def getFileCheckSum(self, file_name):
        f = open(file_name, "rb")
        check_sum = hashfile(f, hashlib.sha256())
        f.close()
        return check_sum

    def getFileMTime(self, file_name):
        mtime = os.path.getmtime(file_name)
        return mtime

    def getFileSize(self, file_name):
        statinfo = os.stat(file_name)
        return statinfo.st_size

    def printAll(self):
        for afile_info in self.file_info_list:
            print("%s %s %s %d" % (afile_info["Name"], afile_info["CheckSum"], time.ctime(afile_info["MTime"]), afile_info["Size"]))

def hashfile(afile, hasher, blocksize=65535):
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    return hasher.hexdigest()

if __name__ == "__main__":
    fig = FilesInfoReader()

    fig.setRootPath("D:\\temp")

    fig.iterate()

    fig.printAll()