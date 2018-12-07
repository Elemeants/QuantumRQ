class FolderManager:

    @staticmethod
    def createFolder(_file: str) -> bool:
        raise NotImplementedError

    @staticmethod
    def existFolder(_path: str) -> bool:
        raise NotImplementedError

    @staticmethod
    def removeFolder(_path: str, treeMode: bool) -> bool:
        raise NotImplementedError
