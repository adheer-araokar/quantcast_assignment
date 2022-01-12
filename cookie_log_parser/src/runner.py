from cookie_log_parser.src.cookie_log_parser import CookieLogParser


def get_latest_cookies(date: str, file_path: str):

    parser = CookieLogParser(date=date, path=file_path)
    return parser.parse_log_and_get_most_active_cookie()
