import os
import hashlib

__author__ = 'ppiazi'

class FilesInfoReader:
    def __init__(self):
        self.file_info_dict = {}
        self.FlagModifiedDate = True
        self.FlagCheckSum = True

    def setRootPath(self, rootPath):
        self.rootPath = rootPath

    def iterate(self):
        for (root, dirs, files) in os.walk(self.rootPath):
            print("Entering %s " % (root))

            for file in files:
                print("\tReading file info : %s ... " % file, end=" ")
                full_file_name = os.path.join(root, file)
                f = open(full_file_name, "rb")
                check_sum = hashfile(f, hashlib.sha256())
                print("done")

                self.file_info_dict[full_file_name] = {}
                self.file_info_dict[full_file_name]["CheckSum"] = check_sum

def hashfile(afile, hasher, blocksize=65535):
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    return hasher.digest()

if __name__ == "__main__":
    fig = FilesInfoReader()

    fig.setRootPath("D:\\temp")

    fig.iterate()