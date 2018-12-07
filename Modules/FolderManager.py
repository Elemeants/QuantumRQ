import errno
import os
import shutil
from os import path
from Modules.ConsoleLoger import *


class FolderManager:

    @staticmethod
    def createFolder(_path: str) -> bool:
        try:
            os.mkdir(_path)
            logOk(f"Carpeta {_path} creada")
            return True
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                logError(f"Error de escritura al crear la carpeta {_path}")
                raise
            logWarning(f"Ya existe la carpeta{_path}")
            raise

    # noinspection PyBroadException
    @staticmethod
    def existFolder(_path: str) -> bool:
        try:
            return path.exists(_path)
        except OSError:
            return False

    @staticmethod
    def removeFolder(_path: str, treeMode: bool) -> bool:
        if treeMode:
            shutil.rmtree(path, ignore_errors=True)
        else:
            try:
                os.rmdir(_path)
            except OSError:
                pass
        return FolderManager.existFolder(_path)
