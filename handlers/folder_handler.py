from pathlib import Path, PosixPath, WindowsPath


class FolderHandler:
    path: Path
    list_files: list[WindowsPath | PosixPath] = []

    def __init__(self, path: Path) -> None:
        self.path = Path(path)

    def read_folder(self) -> list[WindowsPath | PosixPath]:
        try:
            self.__read_folder()
            return self.list_files
        except (Exception) as error:
            raise error
    
    def __read_folder(self) -> None:
        for element in self.path.iterdir():
            self.list_files.append(element)

    
    def save_in_folder(self, folders_name: dict[str, str], files: dict[str, str]) -> None:
        for key in folders_name:
            self.__save_in_folder(folders_name[key], files[key])

    def __save_in_folder(self, dirname: str, files: list[str]) -> None:
        new_path: Path = Path(f"{self.path}/{dirname}")
        new_path.mkdir(exist_ok=True)

        for file in files:
            old_path: Path = Path(f"{self.path}/{file}")
            Path(old_path).rename(f"{new_path}/{file}")
