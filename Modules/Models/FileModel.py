from os import path


class File:
    def __init__(self, _file_name: str, _file_path: str):
        self.file_name = _file_name
        self.file_path = _file_path
        self.file_data = ""
        filePath = _file_path + "\\" + _file_name
        self.file_available = path.exists(filePath)
        if self.file_available:
            try:
                access = open(filePath, "r")
                self.file_data = access.read()
                access.close()
            except FileNotFoundError:
                self.file_data = ""

    def __str__(self) -> str:
        data = "filename: " + self.file_name + "\n\r" + \
               "path    : " + self.file_path + "\n\r" + \
               "exist   : " + self.file_available.__str__() + "\n\r"
        if self.file_data != "":
            data += "data    : " + self.file_data + "\n\r"
        return data