from Modules.Models.FileModel import File


class FileManager:
    @staticmethod
    def create(_file: str) -> bool:
        try:
            open(_file, "x").close()
            return True
        except ():
            return False

    @staticmethod
    def exist(_file: str) -> bool:
        from os import path
        return path.exists(_file)

    @staticmethod
    def remove(_file: str):
        raise NotImplementedError

    @staticmethod
    def read(_file: str) -> File:
        raise NotImplementedError
