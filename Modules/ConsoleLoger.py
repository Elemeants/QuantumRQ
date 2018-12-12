import ctypes

from Modules.Models.Colors import ConsoleColors

kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

Color = ConsoleColors
DEFAULT = "[" + Color.CBOLD + "{2}{0}" + Color.CEND + "] {3}{1}" + Color.CEND
ERROR = Color.CRED2
OK = Color.CGREEN2
WARNING = Color.CVIOLET2
NORMAL = Color.CYELLOW2
DEBUG = Color.CBEIGE2
INFO = Color.CBLUE2


def logDebug(msg):
    print(DEFAULT.format(" DBUG ", msg, ERROR, DEBUG))


def logError(msg):
    print(DEFAULT.format(" FAIL ", msg, ERROR, NORMAL))


def logOk(msg):
    print(DEFAULT.format("  OK  ", msg, OK, NORMAL))


def logWarning(msg):
    print(DEFAULT.format(" WARN ", msg, WARNING, NORMAL))


def logInfo(msg):
    print(DEFAULT.format(" INFO ", msg, INFO, NORMAL))


def logHelp(msg):
    print("  {1}{0}{2}".format(msg, NORMAL, ConsoleColors.CEND))
