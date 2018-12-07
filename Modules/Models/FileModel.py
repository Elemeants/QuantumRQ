import os


class File:
    def __init__(self, _file_name: str, _file_path: str):
        self.file_name = _file_name
        self.file_path = _file_path
        self.file_available = False
        try:
            controller = os
            controller.chdir(self.file_path)
            self.file_data = open(_file_name, "r").read()
            self.file_available = True

        except FileNotFoundError:
            self.file_data = ""
