import sys

from pathlib import Path

from constants import FILE_EXTENSIONS, FOLDERS_NAME
from handlers import FileHandler, FolderHandler


def read_directory(path: Path):
    pass

if __name__ == '__main__':
    try:
        path: Path = sys.argv[2]

        folder_handler: FolderHandler = FolderHandler(path)
        filespath = folder_handler.read_folder()

        file_handler: FileHandler = FileHandler(filespath, FILE_EXTENSIONS)

        files = file_handler.read_files()

        folder_handler.save_in_folder(FOLDERS_NAME, files)

        print("Todos los archivos han sido organizados")
        
    except IndexError as error:
        print("El comando de ejecución es python main.py --path <ruta absoluta>")
    except AttributeError as error:
        print(error)