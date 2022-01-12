from cookie_log_parser.src.datasource.file_system_source import FileSystemSource


class TestFileSystemSource:
    def test_read_file(self, get_file_path):
        source = FileSystemSource()
        path = get_file_path("cookie_log.csv")
        lines = source.read_file(path)
        assert len(lines) == 13

    def test_file_exists(self, get_file_path):
        source = FileSystemSource()
        path = get_file_path("cookie_log.csv")
        assert source.file_exists(path) is True

    def test_file_not_exists(self, get_file_path):
        source = FileSystemSource()
        path = "/dummy/path"
        assert source.file_exists(path) is False
