import random
import typing


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    players = ["alice", "bob", "charlie", "dylan"]
    actions = ["run", "eat", "sleep", "grab", "move", "climb", "swim", "use"]

    while True:
        player = random.choice(players)
        action = random.choice(actions)
        yield (player, action)


def consume_event(
    events: list[tuple[str, str]],
) -> typing.Generator[tuple[str, str], None, None]:
    while len(events) > 0:
        index = random.randrange(len(events))
        event = events.pop(index)
        yield event


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")

    generator = gen_event()
    for index in range(1000):
        event = next(generator)
        print("Event", str(index) + ": Player", end=" ")
        print(event[0], "did action", event[1])

    events = []
    generator = gen_event()
    for index in range(10):
        events.append(next(generator))

    print("Built list of 10 events:", events)

    for event in consume_event(events):
        print("Got event from list:", event)
        print("Remains in list:", events)
