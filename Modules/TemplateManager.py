from Modules.FileManager import FileManager, File


def templateMain(_configMain, _paths: str, _pathFile: str):
    FileManager.createFile(_configMain["name"])
    pathTemplate = "{0}\\Modules\\{1}".format(_paths, _configMain['TemplateFile'])
    _file = File(_configMain["templateName"], pathTemplate)
    _mainFile = File(_configMain["name"], _pathFile)
    FileManager.write(_mainFile, _file.file_data)
