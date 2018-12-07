import os


def enterFolder(_folder: str):
    expected_path = os.getcwd() + "\\" + _folder
    try:
        os.chdir(expected_path)
    except:
        raise FileNotFoundError


def exitFolder():
    os.chdir("./..")
