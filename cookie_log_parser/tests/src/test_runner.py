from cookie_log_parser.src.runner import get_latest_cookies


class TestCookieLogParserRunner:
    def test_run_job(self, get_file_path):
        path = get_file_path("cookie_log.csv")
        date = "2018-12-09"
        cookies = get_latest_cookies(date, path)
        assert cookies == ["AtY0laUfhglK3lC7"]

    def test_run_job_multiple(self, get_file_path):
        path = get_file_path("cookie_log_multiple.csv")
        date = "2018-12-09"
        cookies = get_latest_cookies(date, path)
        assert cookies == ["AtY0laUfhglK3lC7", "SAZuXPGUrfbcn5UA"]
