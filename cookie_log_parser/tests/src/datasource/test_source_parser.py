from cookie_log_parser.src.datasource.file_system_source import FileSystemSource
from cookie_log_parser.src.datasource.source_parser import get_datasource


class TestSourceParser:
    def test_get_datasource(self):
        path = "/local/path"
        source = get_datasource(path)
        assert type(source) == FileSystemSource
