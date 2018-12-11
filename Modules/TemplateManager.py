import datetime
import getpass
import json
from string import Template

from Modules.FileManager import FileManager, File


def generateConfig(config, _pathFile: str, _projectname: str):
    _path = "{0}\\Modules\\Templates\\".format(config["path"])
    _fileConfig = config["properties"]["configFile"]
    _pathFile = _pathFile + "\\" + _fileConfig["name"]
    # logInfo(_pathFile)
    # logInfo(_path)
    # logInfo(_fileConfig)
    FileManager.createFile(_fileConfig["name"])
    _jsonFile = json.loads(File(_fileConfig["templateName"], _path).file_data)
    _jsonFile["project_name"] = _projectname
    with open(_pathFile, "w") as f:
        json.dump(_jsonFile, f, indent=4, sort_keys=True)


def generateMain(config, _pathFile: str, _projectname: str):
    _paths = config["path"]
    _fileConfig = config["properties"]["mainFile"]
    FileManager.createFile(_fileConfig["name"] + ".cpp")
    # logInfo("{0}\\Modules\\{1}".format(_paths, _configMain['templatePath']))
    pathTemplate = "{0}\\Modules\\Templates\\".format(config["path"])
    _file = File(_fileConfig["templateName"], pathTemplate)
    # logInfo(_file.file_data)
    # logInfo(_pathFile)
    _mainFile = File(_fileConfig["name"] + ".cpp", _pathFile)
    _mainFile.file_data = \
        Template(_file.file_data).substitute(
            __FILENAME__=_fileConfig["name"], __USER__=getpass.getuser(),
            __DATE__=datetime.datetime.now().strftime("%Y/%m/%d"),
            __FILE__=_fileConfig["name"] + ".h", __PROJECT__=_projectname
        )
    # logInfo(_mainFile.file_data)
    FileManager.write(_mainFile, _mainFile.file_data)
