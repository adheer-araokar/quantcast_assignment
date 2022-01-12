import pytest

from cookie_log_parser.src.cookie_log_parser import CookieLogParser
from cookie_log_parser.src.exceptions import IllegalArgumentException


class TestCookieLogParser:
    def test_init_invalid_date(self, get_file_path):
        path = get_file_path("cookie_log.csv")
        date = "2018-12-09asas"
        with pytest.raises(IllegalArgumentException):
            CookieLogParser(date=date, file_path=path)

    def test_init_invalid_path(self, get_file_path):
        path = get_file_path("cookie_logasas.csv")
        date = "2018-12-09"
        with pytest.raises(IllegalArgumentException):
            CookieLogParser(date=date, file_path=path)

    def test_parse_log_and_get_most_active(self, get_file_path):
        path = get_file_path("cookie_log.csv")
        date = "2018-12-09"
        parser = CookieLogParser(date=date, file_path=path)
        cookies = parser.parse_log_and_get_latest()
        assert cookies == ["AtY0laUfhglK3lC7"]

    def test_parse_log_and_get_most_active_second_source(self, get_file_path):
        path = get_file_path("cookie_log_multiple.csv")
        date = "2018-12-09"
        parser = CookieLogParser(date=date, file_path=path)
        cookies = parser.parse_log_and_get_latest()
        assert cookies == ["AtY0laUfhglK3lC7"]
