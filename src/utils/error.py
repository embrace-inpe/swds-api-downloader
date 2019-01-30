import sys


class NoTraceBackWithLineNumber(Exception):
    def __init__(self, msg):
        self.args = "{0.__name__}: {1}".format(type(self), msg),
        self.msg = msg
        sys.exit(self)


class SwdsError(NoTraceBackWithLineNumber):
    pass
