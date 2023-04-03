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
    @staticmethod
    def log(message, log_method=print):
        """
        Logs a message with a log method. Log method defaults to print()

        Args:
            message (str) the message to log.
            log_method (Function, optional): the log method. Defaults to print.
        """
        log_message = 'I [' + datetime.datetime.now().isoformat() + \
            ']: ' + message
        log_method(log_message)
