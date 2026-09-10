import abc
import typing


class DataProcessor(abc.ABC):
    def __init__(self, name: str) -> None:
        self.name = name
        self.data: list[tuple[int, str]] = []
        self.total_processed = 0

    @abc.abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abc.abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    def add_item(self, value: str) -> None:
        rank = self.total_processed
        self.data.append((rank, value))
        self.total_processed = self.total_processed + 1

    def output(self) -> tuple[int, str]:
        if len(self.data) == 0:
            raise Exception("No data available")
        return self.data.pop(0)


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__("Numeric Processor")

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, int) or isinstance(data, float):
            return True
        if isinstance(data, list):
            for item in data:
                if not isinstance(item, int) and not isinstance(item, float):
                    return False
            return True
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise Exception("Improper numeric data")
        if isinstance(data, list):
            for item in data:
                self.add_item(str(item))
        else:
            self.add_item(str(data))


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__("Text Processor")

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            for item in data:
                if not isinstance(item, str):
                    return False
            return True
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise Exception("Improper text data")
        if isinstance(data, list):
            for item in data:
                self.add_item(item)
        else:
            self.add_item(data)


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__("Log Processor")

    def is_log(self, data: typing.Any) -> bool:
        if not isinstance(data, dict):
            return False
        if "log_level" not in data or "log_message" not in data:
            return False
        if not isinstance(data["log_level"], str):
            return False
        if not isinstance(data["log_message"], str):
            return False
        return True

    def validate(self, data: typing.Any) -> bool:
        if self.is_log(data):
            return True
        if isinstance(data, list):
            for item in data:
                if not self.is_log(item):
                    return False
            return True
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise Exception("Improper log data")
        if isinstance(data, list):
            for item in data:
                self.add_item(item["log_level"] + ": " + item["log_message"])
        else:
            self.add_item(data["log_level"] + ": " + data["log_message"])


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")

    numeric = NumericProcessor()
    print("Testing Numeric Processor...")
    print("Trying to validate input '42':", numeric.validate(42))
    print("Trying to validate input 'Hello':", numeric.validate("Hello"))
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        numeric.ingest("foo")  # type: ignore[arg-type]
    except Exception as error:
        print("Got exception:", error)
    print("Processing data:", [1, 2, 3, 4, 5])
    numeric.ingest([1, 2, 3, 4, 5])
    print("Extracting 3 values...")
    for index in range(3):
        value = numeric.output()
        print("Numeric value", str(index) + ":", value[1])

    text = TextProcessor()
    print("Testing Text Processor...")
    print("Trying to validate input '42':", text.validate(42))
    print("Processing data:", ["Hello", "Nexus", "World"])
    text.ingest(["Hello", "Nexus", "World"])
    print("Extracting 1 value...")
    value = text.output()
    print("Text value 0:", value[1])

    log = LogProcessor()
    logs = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"},
    ]
    print("Testing Log Processor...")
    print("Trying to validate input 'Hello':", log.validate("Hello"))
    print("Processing data:", logs)
    log.ingest(logs)
    print("Extracting 2 values...")
    for index in range(2):
        value = log.output()
        print("Log entry", str(index) + ":", value[1])
