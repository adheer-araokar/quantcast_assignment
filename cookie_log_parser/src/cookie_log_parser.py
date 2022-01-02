import datetime
from typing import List

from cookie_log_parser.src.datasource.source import Source
from cookie_log_parser.src.datasource.source_parser import get_datasource
from cookie_log_parser.src.date_utils import DateUtils
from cookie_log_parser.src.exceptions import IllegalArgumentException, NoDataException


class CookieLogParser:

    date: datetime
    file_path: str
    source: Source

    def __init__(self, date: str, file_path: str):
        if not DateUtils.validate_date(date):
            raise IllegalArgumentException("Supplied date is not valid.")

        source = get_datasource(file_path)

        if not source.file_exists(file_path):
            raise IllegalArgumentException("Supplied file path does not exist.")

        self.date = DateUtils.get_date(date)
        self.file_path = file_path
        self.source = source

    def parse_log_and_get_latest(self) -> List[str]:
        file_contents = self.source.read_file(file_path=self.file_path)
        if len(file_contents) <= 1:
            raise NoDataException("File has no data or only the header row.")

        latest_timestamp = None
        latest_cookies = []
        for row in file_contents[1:]:
            row_contents = row.split(",")
            if len(row_contents) == 1:
                continue
            cookie = row_contents[0]
            timestamp = row_contents[1]
            if not DateUtils.validate_date(timestamp):
                continue
            timestamp = DateUtils.get_date(timestamp)
            if self.date.date() == timestamp.date():
                if latest_timestamp is None:
                    latest_timestamp = timestamp
                    if cookie not in latest_cookies:
                        latest_cookies.append(cookie)
                elif latest_timestamp == timestamp:
                    if cookie not in latest_cookies:
                        latest_cookies.append(cookie)
            elif self.date.date() > timestamp.date():
                break

        return list(latest_cookies)
