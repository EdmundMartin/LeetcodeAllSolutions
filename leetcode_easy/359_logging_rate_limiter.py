

class Logger:

    def __init__(self):
        self.seen_messages = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.seen_messages:
            self.seen_messages[message] = timestamp
            return True
        last_timestamp = self.seen_messages[message]
        if timestamp - last_timestamp >= 10:
            self.seen_messages[message] = timestamp
            return True
        return False


if __name__ == '__main__':
    logger = Logger()
    result = logger.shouldPrintMessage(1, "foo")
    assert result is True
    result = logger.shouldPrintMessage(2, "bar")
    assert result is True
    result = logger.shouldPrintMessage(3, "foo")
    assert result is False