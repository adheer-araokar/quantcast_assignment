from cookie_log_parser.src.datasource.file_system_source import FileSystemSource
from cookie_log_parser.src.datasource.source import Source


# Currently, since only 1 source. i.e. local is supported, we'll simply return the same
# As and when more sources are required to be added, we will use the path and any other arg to get the data source
def get_datasource(path: str) -> Source:
    return FileSystemSource()
