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

    def remaining(self) -> int:
        return len(self.data)


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

    def ingest(self, data: typing.Any) -> None:
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

    def ingest(self, data: typing.Any) -> None:
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
        return "log_level" in data and "log_message" in data

    def validate(self, data: typing.Any) -> bool:
        if self.is_log(data):
            return True
        if isinstance(data, list):
            for item in data:
                if not self.is_log(item):
                    return False
            return True
        return False

    def ingest(self, data: typing.Any) -> None:
        if not self.validate(data):
            raise Exception("Improper log data")
        if isinstance(data, list):
            for item in data:
                self.add_item(item["log_level"] + ": " + item["log_message"])
        else:
            self.add_item(data["log_level"] + ": " + data["log_message"])


class DataStream:
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for element in stream:
            processed = False
            for processor in self.processors:
                if processor.validate(element):
                    processor.ingest(element)
                    processed = True
                    break
            if not processed:
                print("DataStream error - Can't process element:", element)

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if len(self.processors) == 0:
            print("No processor found, no data")
        for processor in self.processors:
            print(processor.name + ":", end=" ")
            print("total", processor.total_processed, "items,", end=" ")
            print("remaining", processor.remaining(), "on processor")


if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===")
    print("Initialize Data Stream...")
    stream = DataStream()
    stream.print_processors_stats()

    batch = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {"log_level": "WARNING", "log_message": "Telnet access"},
            {"log_level": "INFO", "log_message": "User is connected"},
        ],
        42,
        ["Hi", "five"],
    ]

    print("Registering Numeric Processor")
    stream.register_processor(NumericProcessor())
    print("Send first batch of data on stream:", batch)
    stream.process_stream(batch)
    stream.print_processors_stats()

    print("Registering other data processors")
    stream.register_processor(TextProcessor())
    stream.register_processor(LogProcessor())
    print("Send the same batch again")
    stream.process_stream(batch)
    stream.print_processors_stats()

    print("Consume some elements from the data processors")
    stream.processors[0].output()
    stream.processors[0].output()
    stream.processors[0].output()
    stream.processors[1].output()
    stream.processors[1].output()
    stream.processors[2].output()
    stream.print_processors_stats()
