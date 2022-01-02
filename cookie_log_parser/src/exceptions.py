class IllegalArgumentException(Exception):
    def __init__(self, msg):
        self.msg = msg


class NoDataException(Exception):
    def __init__(self, msg):
        self.msg = msg
