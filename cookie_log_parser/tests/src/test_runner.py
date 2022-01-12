from cookie_log_parser.src.runner import get_latest_cookies


class TestCookieLogParserRunner:
    def test_run_job(self, get_file_path):
        path = get_file_path("cookie_log.csv")
        date = "2018-12-09"
        cookies = get_latest_cookies(date, path)
        assert cookies == ["AtY0laUfhglK3lC7"]

    def test_run_job_multiple_different_date(self, get_file_path):
        path = get_file_path("cookie_log.csv")
        date = "2018-12-08"
        cookies = get_latest_cookies(date, path)
        assert cookies == ["SAZuXPGUrfbcn5UA", "4sMM2LxV07bPJzwf", "fbcn5UAVanZf6UtG"]

    def test_run_job_second_source_file(self, get_file_path):
        path = get_file_path("cookie_log_multiple.csv")
        date = "2018-12-09"
        cookies = get_latest_cookies(date, path)
        assert cookies == ["AtY0laUfhglK3lC7"]
