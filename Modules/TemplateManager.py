import datetime
import getpass
from string import Template

from Modules.FileManager import FileManager, File
from Modules.JsonManager import getJson, saveJson


def generateConfig(config, _pathFile: str, _projectname: str) -> bool:
    _fileConfig = config["properties"]["configFile"]
    _path = "{0}/Modules\\Templates\\{1}".format(config["path"], _fileConfig["name"])
    _pathFile = _pathFile + "\\" + _fileConfig["name"]
    if FileManager.createFile(_fileConfig["name"]):
        _jsonFile = getJson(_path)
        if _jsonFile:
            _jsonFile["project_name"] = _projectname
            _jsonFile["mainFile"] = "main"
            return saveJson(_pathFile, _jsonFile)
    return False


def generateMain(config, _pathFile: str, _projectname: str) -> bool:
    _paths = config["path"]
    _fileConfig = config["properties"]["mainFile"]
    pathTemplate = "{0}\\Modules\\Templates\\".format(_paths)
    FileManager.createFile(_fileConfig["name"] + ".cpp")
    if FileManager.existFile(_fileConfig["name"] + ".cpp"):
        _file = File(_fileConfig["templateName"], pathTemplate)
        _mainFile = File(_fileConfig["name"] + ".cpp", _pathFile)
        _mainFile.file_data = \
            Template(_file.file_data).substitute(
                __FILENAME__=_fileConfig["name"], __USER__=getpass.getuser(),
                __DATE__=datetime.datetime.now().strftime("%Y/%m/%d"),
                __FILE__=_fileConfig["name"] + ".h", __PROJECT__=_projectname
            )
        FileManager.write(_mainFile, _mainFile.file_data)
        return True
    return False
