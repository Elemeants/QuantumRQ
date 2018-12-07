import ctypes

from Modules.Models.Colors import ConsoleColors

kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)


class ConsoleLoger:
    Color = ConsoleColors

    DEFAULT = "[" + Color.CBOLD + "{2}{0}" + Color.CEND + "] {3}{1}" + Color.CEND
    ERROR = Color.CRED2
    OK = Color.CGREEN2
    WARNING = Color.CVIOLET2
    NORMAL = Color.CYELLOW2
    INFO = Color.CBLUE2

    @staticmethod
    def Error(Message: str):
        print(ConsoleLoger.DEFAULT.format(" FAIL ", Message, ConsoleLoger.ERROR, ConsoleLoger.NORMAL))

    @staticmethod
    def Ok(Message: str):
        print(ConsoleLoger.DEFAULT.format("  OK  ", Message, ConsoleLoger.OK, ConsoleLoger.NORMAL))

    @staticmethod
    def Warning(Message: str):
        print(ConsoleLoger.DEFAULT.format(" WARN ", Message, ConsoleLoger.WARNING, ConsoleLoger.NORMAL))

    @staticmethod
    def Info(Message: str):
        print(ConsoleLoger.DEFAULT.format(" INFO ", Message, ConsoleLoger.INFO, ConsoleLoger.NORMAL))

    @staticmethod
    def Help(Message: str):
        print("{1}{0}{2}".format(Message, ConsoleLoger.NORMAL, ConsoleLoger.CEND))
