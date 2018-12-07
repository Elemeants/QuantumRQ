from Modules.ConsoleLoger import *
from Modules.PathManager import *
from Modules.FileManager import FileManager
from Modules.FolderManager import FolderManager
import json


def getConfiguration():
    fileJson = FileManager.readFile("config.json").file_data
    return json.loads(fileJson)


def generateNewProject(_projectname: str):
    logInfo(f" Generando nuevo proyecto {_projectname}")
    if not FolderManager.existFolder(_projectname.capitalize()):
        config = getConfiguration()
        FolderManager.createFolder(_projectname.capitalize())
        enterFolder(_projectname)
        FileManager.createFile(config['properties']['mainFile']['name'])
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


generateNewProject("TestProject")
