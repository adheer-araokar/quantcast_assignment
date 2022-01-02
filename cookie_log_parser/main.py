import argparse
from typing import List, Dict, Any

from cookie_log_parser.src.runner import get_latest_cookies


def get_args() -> Dict[str, Any]:
    ap = argparse.ArgumentParser()
    ap.add_argument("-f", "--filename", type=str, help="File Name to Parse")
    ap.add_argument("-d", "--date", type=str, help="Date to get the latest cookie")
    return ap.parse_args().__dict__


def main(argv: List[str] = None):
    args = get_args()
    filename = args.get("filename", None)
    date = args.get("date", None)

    # Start the main job here!
    latest_cookies = get_latest_cookies(date, filename)
    for cookie in latest_cookies:
        print(cookie)
