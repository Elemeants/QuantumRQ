import sys

from Modules.PathManager import *
from Modules.Scripts.Compiler import *
from Modules.TemplateManager import *

config = []
paths = []
QuantumPath = sys.argv[1]
ProjectPath = sys.argv[2]


def initQuantumRQ():
    global config
    try:
        gotoDir(QuantumPath)
        config = getJson("config.json")
        if config:
            config["path"] = QuantumPath
            saveJson("config.json", config)
    except():
        logError("No se pudo iniciar QuantumRQ")


def generateNewProject(_projectname: str) -> bool:
    gotoDir(ProjectPath)
    logInfo(f"Generando nuevo proyecto {_projectname}")
    if not FolderManager.existFolder(_projectname.capitalize()):
        FolderManager.createFolder(_projectname.capitalize())
        enterFolder(_projectname)

        def fail(projName: str):
            exitFolder()
            FolderManager.removeFolder(os.getcwd() + projName, True)
            return False

        if not generateConfig(config, os.getcwd(), _projectname):
            return fail(_projectname)
        if not generateMain(config, os.getcwd(), _projectname):
            return fail(_projectname)
        return True
    else:
        logError(f"La carpeta {_projectname.capitalize()} debe estar vacia")
        return False


def cleanProject():
    logError("Limpiando proyecto")
    if FolderManager.existFolder("Debug"):
        FolderManager.removeFolder("Debug", True)
    if FolderManager.existFolder("Release"):
        FolderManager.removeFolder("Release", True)


def deleteProject(_projectname: str, Log: bool) -> bool:
    (logInfo(f"{_projectname} va a ser eliminado") if Log else print())
    if FolderManager.existFolder(_projectname):
        if FileManager.existFile(_projectname + "\\config.json"):
            (logWarning("Eliminando proyecto...") if Log else print())
            FolderManager.removeFolder(_projectname, True)
            return True
        else:
            (logError("No es un proyecto valido") if Log else print())
    else:
        (logError("No existe el proyecto") if Log else print())
    return False


def setBuildOptions(_buildOptions: str):
    projectConfig = getJson("config.json")
    projectConfig["buildOptions"] = _buildOptions
    if not saveJson("config.json", projectConfig):
        logError("No se guardaron las configuraciones")
    else:
        logOk("Configuraciones guardadas")


def buildProject(_execute: bool):
    logInfo("Compilando el proyecto")
    projectConfig = getJson("config.json")
    if projectConfig:
        raise NotImplementedError
    else:
        logError("No se encontro archivo de proyecto")


class addComponent:
    @staticmethod
    def library(_name: str):
        print(" Agregando libreria")

    @staticmethod
    def component(_name: str):
        print(" Agregando componente")


# Working in AUTO HELP
def ShowHelp(namespace):
    gotoDir(QuantumPath)
    helpPath = config["path"] + config["helpPath"]
    jsonHelp = getJson(helpPath)
    if namespace[0] != '':
        for x in range(0, namespace.__len__()):
            if jsonHelp.get(namespace[x]):
                jsonHelp = jsonHelp[namespace[x]]
            else:
                print()
                logHelp(getJson(helpPath)["errorhelp"])
                return
    try:
        print()
        if jsonHelp.get("help"):
            logHelp(jsonHelp["help"])
            print()
        for var in jsonHelp:
            logHelp('{:>12}   -->   {:>12}'.format(var, "test"))

        print()
    except (TypeError, KeyError):
        pass


initQuantumRQ()
ShowHelp(["commands", "add"])
# if generateNewProject("Test"):
#    gotoDir(ProjectPath)
#    deleteProject("Test", True)
