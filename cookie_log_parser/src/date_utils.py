import datetime

import arrow


class DateUtils:
    @classmethod
    def validate_date(cls, date_str: str) -> bool:
        try:
            arrow.get(date_str)
            return True
        except Exception:
            return False

    @classmethod
    def get_date(cls, date_str: str) -> datetime:
        return arrow.get(date_str).datetime
