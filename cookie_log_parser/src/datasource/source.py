from abc import ABCMeta, abstractmethod
from typing import List


class Source(metaclass=ABCMeta):
    """
    Interface for Data Source actions
    """

    @abstractmethod
    def get_files_in_path_with_extension(self, dir_path: str, extension: str) -> List[str]:
        pass

    @abstractmethod
    def read_file(self, file_path: str) -> List[str]:
        pass

    @abstractmethod
    def file_exists(self, file_path: str) -> bool:
        pass

    @abstractmethod
    def is_dir(self, path: str) -> bool:
        pass
