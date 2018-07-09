import tempfile
from pprint import pprint

from ds_config import DSConfig


class DSHelper:
    def __init__(self):
        pass

    @classmethod
    def readContent(cls):
        pass

    @classmethod
    def printPrettyJSON(cls, obj):
        pass

    @classmethod
    def ensureDirExistance(cls, param):
        pass

    @classmethod
    def writeByteArrayToFile(cls, filePath, docBytes):
        pass

    @classmethod
    def create_private_key_temp_file(cls, file_suffix):
        tmp_file = tempfile.NamedTemporaryFile(mode='w+b', suffix=file_suffix)
        f = open(tmp_file.name, "w+")
        f.write(DSConfig.private_key())
        f.close()
        return tmp_file
