import os

from Modules.ConsoleLoger import *
from Modules.Models.FileModel import File


class FileManager:
    @staticmethod
    def createFile(_file: str) -> bool:
        try:
            open(_file, "x").close()
            logOk(f"Archivo {_file} creado")
            return True
        except FileExistsError:
            logError(f"Error al crear el archivo {_file}")
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
                logOk(f"Archivo {_file} eliminado")
                return 0
            except (OSError, IOError, FileNotFoundError):
                logWarning(f"No se puede elimiar \"{_file}\"")
                return -1
        return 1

    @staticmethod
    def readFile(_file: str) -> File:
        return File(_file, os.getcwd())

    @staticmethod
    def write(_file: File, data: str) -> bool:
        try:
            file = open(_file.file_name, "w+")
            _file.file_data = data
            file.write(_file.file_data)
            file.close()
            logOk(f"Escritura correcta Archivo -> {_file.file_name}")
            return True
        except (OSError, IOError, FileNotFoundError):
            logWarning(f"Error en la escritura del archivo -> {_file.file_name}")
            return False
