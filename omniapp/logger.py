import enum
import datetime


class LogLevel(enum.Enum):
    FATAL = 1
    ERROR = 2
    WARN = 3
    INFO = 4
    DEBUG = 5
    TRACE = 6
    EVERYTHING = 7
    OFF = 8


class Logger:
    def log(self, message='', log_method=print):
        log_message = 'I [' + datetime.datetime.now().isoformat() + \
            ']: ' + message
        log_method(log_message)
