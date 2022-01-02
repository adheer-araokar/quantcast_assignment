import os
from typing import List

from cookie_log_parser.src.datasource.source import Source


class FileSystemSource(Source):
    def read_file(self, file_path: str) -> List[str]:
        with open(file_path, "r") as content_file:
            content = content_file.readlines()
        return content

    def file_exists(self, file_path: str) -> bool:
        return os.path.exists(file_path)
