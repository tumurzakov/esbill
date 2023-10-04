from eventsourcing.domain import (
    Aggregate,
    event,
)

class Point(Aggregate):
    @event("Created")
    def __init__(self) -> None:
        pass
