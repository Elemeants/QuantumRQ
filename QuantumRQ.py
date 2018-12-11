import sys

from Modules.PathManager import *
from Modules.Scripts.Compiler import *
from Modules.TemplateManager import *

config = []
paths = []


def initQuantumRQ():
    global config
    try:
        os.chdir(sys.argv[1])
        fileJson = FileManager.readFile("config.json").file_data
        config = json.loads(fileJson)
    except(json.decoder.JSONDecodeError, OSError, FileNotFoundError):
        logError("Error de inicializacion")
    config["path"] = os.getcwd()
    with open("config.json", "w") as f:
        json.dump(config, f, indent=4, sort_keys=True)
    os.chdir(sys.argv[2])


def generateNewProject(_projectname: str):
    os.chdir(sys.argv[2])
    logInfo(f" Generando nuevo proyecto {_projectname}")
    if not FolderManager.existFolder(_projectname.capitalize()):
        FolderManager.createFolder(_projectname.capitalize())
        enterFolder(_projectname)
        generateConfig(config, os.getcwd(), _projectname)
        generateMain(config, os.getcwd(), _projectname)
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


initQuantumRQ()
generateNewProject("TestProject")
compileFile(config["properties"]["mainFile"]["name"], "", True)
executeFile(config["properties"]["mainFile"]["name"], "", True)
