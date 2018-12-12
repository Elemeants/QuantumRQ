import os


def gotoDir(_path: str):
    try:
        os.chdir(_path)
        if os.path.normpath(_path) != os.path.normpath(os.getcwd()):
            raise EnvironmentError
        else:
            return True
    except...:
        raise FileNotFoundError

def enterFolder(_folder: str):
    expected_path = os.getcwd() + "\\" + _folder
    try:
        os.chdir(expected_path)
        if os.path.normpath(expected_path) != os.path.normpath(os.getcwd()):
            raise EnvironmentError
        else:
            return True
    except...:
        raise FileNotFoundError


def exitFolder():
    os.chdir("./..")
