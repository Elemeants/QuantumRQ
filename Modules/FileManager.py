import os
from Modules.Models.FileModel import File


class FileManager:
    @staticmethod
    def createFile(_file: str) -> bool:
        try:
            open(_file, "x").close()
            return True
        except FileExistsError:
            return False

    @staticmethod
    def existFile(_file: str) -> bool:
        from os import path
        return path.exists(_file)

    @staticmethod
    def removeFile(_file: str) -> int:
        if FileManager.existFile(_file):
            try:
                os.remove(_file)
                return 0
            except (OSError, IOError, FileNotFoundError):
                return -1
        return 1

    @staticmethod
    def readFile(_file: str) -> File:
        return File(_file, os.getcwd())

    @staticmethod
    def write(_file: File, data: str) -> bool:
        raise NotImplementedError

