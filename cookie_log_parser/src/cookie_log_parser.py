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

        cookie_frequency_map = dict()
        latest_cookies = []
        max_frequency = 0
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
                frequency = cookie_frequency_map.get(cookie)
                if frequency is None:
                    frequency = 1
                else:
                    frequency += 1
                cookie_frequency_map[cookie] = frequency
                if frequency > max_frequency:
                    max_frequency = frequency
            elif self.date.date() > timestamp.date():
                break

        for cookie in cookie_frequency_map.keys():
            if cookie_frequency_map[cookie] == max_frequency:
                latest_cookies.append(cookie)

        return list(latest_cookies)
