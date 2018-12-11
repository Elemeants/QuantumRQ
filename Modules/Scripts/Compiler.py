import os

from Modules.ConsoleLoger import *
from Modules.FolderManager import FolderManager


def compileFile(_file: str, _buildOptions: str, _debug: bool):
    if _debug:
        outputFolder = "Debug/"
    else:
        outputFolder = "Release/"
    FolderManager.createFolder(outputFolder)
    result = os.system(f"g++ {_file}.cpp -o {outputFolder}{_file}.exe {_buildOptions}")
    if result == 0:
        logOk("Compilacion correcta")
    else:
        logError("Error de compilacion")


def executeFile(_file: str, _arguments, _debug: bool):
    if _debug:
        outputFolder = "Debug/"
    else:
        outputFolder = "Release/"
    if FolderManager.existFolder(outputFolder):
        logInfo(f"Ejecutando {_file}.exe")
        os.chdir(outputFolder)
        os.system(f"{_file}.exe {_arguments}")
        os.chdir("./..")
    else:
        logWarning("No esta compilado el proyecto")
