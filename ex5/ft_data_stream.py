import random
from typing import Generator

PLAYERS: list[str] = ["alice", "bob", "charlie", "dylan"]
ACTIONS: list[str] = ["run", "jump", "eat", "sleep",
                      "move", "climb", "swim", "grab", "use", "release"]

def gen_event() -> Generator[tuple[str, str], None, None]:
    while True:
        name = random.choice(PLAYERS)
        action = random.choice(ACTIONS)
        yield (name, action)


def consume_event(
        events: list[tuple[str, str]]
        ) -> Generator[tuple[str, str], None, None]:
    index: int = random.randint(0, len(events) - 1)
    event_remove: tuple[str, str] = events[index]
    events.pop(index)
    yield event_remove


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")

    stream: Generator[tuple[str, str], None, None] = gen_event()
    for i in range(1000):
        gen: tuple[str, str] = next(stream)
        print(f"Event {i}: Player {gen[0]} did action {gen[1]}")

    event_list: list[tuple[str, str]] = []
    for i in range(10):
        event_list.append(next(stream))
    print(f"Built list of 10 events: {event_list}")

    for i in range(10):
        list_remove: tuple[str, str] = next(consume_event(event_list))
        print(f"Got event from list: {list_remove}")
        print(f"Remains in list: {event_list}")
