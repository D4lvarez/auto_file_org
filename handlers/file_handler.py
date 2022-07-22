from pathlib import Path, PosixPath, WindowsPath


class FileHandler:
    filespath: list[WindowsPath | PosixPath]

    # Type Files
    executable_files: list[WindowsPath | PosixPath] = []
    audios_files: list[WindowsPath | PosixPath] = []
    images_files: list[WindowsPath | PosixPath] = []
    compressed_files: list[WindowsPath | PosixPath] = []
    document_files: list[WindowsPath | PosixPath] = []

    def __init__(self, filespath, constants: dict[str, list[str]]) -> None:
        self.filespath = filespath
        self.__constants = constants
    
    def __file_extension(self, filepath: WindowsPath | PosixPath) -> str:
        return Path(filepath).suffix

    def __get_file(self, file: WindowsPath | PosixPath):
        return str(file).split('\\').pop()
    
    def read_files(self) -> dict[str, list[WindowsPath | PosixPath]]:
        for filepath in self.filespath:
            if self.__file_extension(filepath) in self.__constants['apps']:
                self.executable_files.append(self.__get_file(filepath))
            
            if self.__file_extension(filepath) in self.__constants['audio']:
                self.audios_files.append(self.__get_file(filepath))
            
            if self.__file_extension(filepath) in self.__constants['imgs']:
                self.images_files.append(self.__get_file(filepath))

            if self.__file_extension(filepath) in self.__constants['compressed']:
                self.compressed_files.append(self.__get_file(filepath))

            if self.__file_extension(filepath) in self.__constants['docs']:
                self.document_files.append(self.__get_file(filepath))

        return {
            'apps': self.executable_files,
            'audio': self.audios_files,
            'compressed': self.compressed_files,
            'docs': self.document_files,
            'imgs': self.images_files
        }