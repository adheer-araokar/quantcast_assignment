import datetime
from typing import List, Dict

from cookie_log_parser.src.datasource.source import Source
from cookie_log_parser.src.datasource.source_parser import get_datasource
from cookie_log_parser.src.date_utils import DateUtils
from cookie_log_parser.src.exceptions import IllegalArgumentException, NoDataException
from cookie_log_parser.src.enums import EXTENSION


class CookieLogParser:

    date: datetime
    path: str
    source: Source
    valid_extension: str = EXTENSION.CSV.value

    def __init__(self, date: str, path: str):
        if not DateUtils.validate_date(date):
            raise IllegalArgumentException("Supplied date is not valid.")

        source = get_datasource(path)

        if not source.file_exists(path):
            raise IllegalArgumentException("Supplied file path does not exist.")

        self.date = DateUtils.get_date(date)
        self.path = path
        self.source = source

    def parse_log_and_get_most_active_cookie(self) -> List[str]:
        paths = []
        if not self.source.is_dir(self.path):
            paths.append(self.path)
        else:
            paths = self.source.get_files_in_path_with_extension(self.path, self.valid_extension)
        parent_cookie_frequency_map = {}
        for path in paths:
            cookie_frequency_map = self.parse_log_and_get_cookie_frequency_map(path)
            for cookie in cookie_frequency_map.keys():
                frequency = parent_cookie_frequency_map.get(cookie)
                if frequency is None:
                    parent_cookie_frequency_map[cookie] = cookie_frequency_map[cookie]
                else:
                    parent_cookie_frequency_map[cookie] = frequency + cookie_frequency_map[cookie]

        return self.get_latest_cookie_from_cookie_freq_map(parent_cookie_frequency_map)

    def parse_log_and_get_cookie_frequency_map(self, file_path: str) -> Dict[str, int]:
        file_contents = self.source.read_file(file_path=file_path)
        if len(file_contents) <= 1:
            raise NoDataException("File has no data or only the header row.")

        cookie_frequency_map = dict()
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
            elif self.date.date() > timestamp.date():
                break

        return cookie_frequency_map

    def get_latest_cookie_from_cookie_freq_map(self, cookie_frequency_map: Dict[str, int]) -> List[str]:
        latest_cookies = []
        max_frequency = 0
        for cookie in cookie_frequency_map.keys():
            frequency = cookie_frequency_map[cookie]
            if frequency > max_frequency:
                max_frequency = frequency

        for cookie in cookie_frequency_map.keys():
            if cookie_frequency_map[cookie] == max_frequency:
                latest_cookies.append(cookie)

        return list(latest_cookies)
