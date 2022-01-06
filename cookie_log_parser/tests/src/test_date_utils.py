import datetime

from dateutil.tz import tzutc

from cookie_log_parser.src.date_utils import DateUtils


class TestDateUtils:
    def test_validate_date_valid(self):
        valid_date = "2022-01-01"
        valid = DateUtils.validate_date(valid_date)
        assert valid is True

    def test_validate_date_invalid(self):
        valid_date = "2022-01as-01"
        valid = DateUtils.validate_date(valid_date)
        assert valid is False

    def test_get_date(self):
        valid_date = "2022-01-01"
        date = DateUtils.get_date(valid_date)
        assert type(date) == datetime.datetime
        assert date == datetime.datetime(year=2022, month=1, day=1, tzinfo=tzutc())
