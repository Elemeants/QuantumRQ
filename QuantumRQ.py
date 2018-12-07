from Modules.ConsoleLoger import ConsoleLoger
from Modules.FileManager import FileManager

# Testing modules...
ConsoleLoger.Info("Testing")
FileManager.create("text.txt")
ConsoleLoger.Ok("Archivo creado")
