import os
from typing import List

from cookie_log_parser.src.datasource.source import Source


class FileSystemSource(Source):
    def get_files_in_path_with_extension(self, dir_path: str, extension: str) -> List[str]:
        files_with_extn = []
        for root, dirs, files in os.walk(dir_path):
            for filename in files:
                if filename.endswith(extension):
                    files_with_extn.append(os.path.join(root, filename))
        return files_with_extn

    def read_file(self, file_path: str) -> List[str]:
        with open(file_path, "r") as content_file:
            content = content_file.readlines()
        return content

    def file_exists(self, file_path: str) -> bool:
        return os.path.exists(file_path)

    def is_dir(self, path: str) -> bool:
        return os.path.isdir(path)
