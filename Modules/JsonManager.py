import json

from Modules.FileManager import FileManager


def getJson(_file: str) -> json:
    try:
        if FileManager.existFile(_file):
            fileJson = FileManager.readPath(_file)
            return json.loads(fileJson)
        return False
    except(json.decoder.JSONDecodeError, OSError, FileNotFoundError):
        return False


def saveJson(_file: str, _data) -> bool:
    try:
        with open(_file, "w") as f:
            json.dump(_data, f, indent=4, sort_keys=True)
        return True
    except(json.decoder.JSONDecodeError, OSError, FileNotFoundError):
        return False
