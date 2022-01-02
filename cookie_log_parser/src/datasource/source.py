from abc import ABCMeta, abstractmethod
from typing import List


class Source(metaclass=ABCMeta):
    """
    Interface for Data Source actions
    """

    @abstractmethod
    def read_file(self, file_path: str) -> List[str]:
        pass

    @abstractmethod
    def file_exists(self, file_path: str) -> bool:
        pass
