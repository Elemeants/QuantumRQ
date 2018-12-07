import os

from Modules.ConsoleLoger import ConsoleLoger
from Modules.FileManager import FileManager
from Modules.Models.FileModel import File

# Testing modules...
ConsoleLoger.Info("Testing")
FileManager.create("text.txt")
ConsoleLoger.Ok("Archivo creado")
test = File("text.txt", os.getcwd())
print(test.__str__())
