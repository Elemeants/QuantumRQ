import json
import sys

from Modules.ConsoleLoger import *
from Modules.FileManager import FileManager
from Modules.FolderManager import FolderManager
from Modules.PathManager import *
from Modules.TemplateManager import *

paths = [sys.argv[1], sys.argv[0]]


def getConfiguration():
    fileJson = FileManager.readFile("config.json").file_data
    return json.loads(fileJson)


def setConfigPaths():
    config = getConfiguration()
    config["path"] = os.getcwd()
    with open("config.json", "w") as f:
        json.dump(config, f)
    os.chdir(sys.argv[1])


def generateNewProject(_projectname: str, _path: str):
    logInfo(f" Generando nuevo proyecto {_projectname}")
    if not FolderManager.existFolder(_projectname.capitalize()):
        config = getConfiguration()
        FolderManager.createFolder(_projectname.capitalize())
        enterFolder(_projectname)
        templateMain(config["properties"]["mainFile"], config["path"], os.getcwd())
    else:
        logError(f" La carpeta {_projectname.capitalize()} debe estar vacia")


def cleanProject():
    print(" Limpiando proyecto")


def buildProject():
    print(" Compilando...")


class addComponent:
    @staticmethod
    def library(_name: str):
        print(" Agregando libreria")

    @staticmethod
    def component(_name: str):
        print(" Agregando componente")


def initQuantumRQ():
    print(sys.argv)
    print(paths)
    os.chdir(paths[0])
    setConfigPaths()


initQuantumRQ()
# generateNewProject("TestProject", sys.argv[0])
