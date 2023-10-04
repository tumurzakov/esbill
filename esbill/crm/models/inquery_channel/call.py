from eventsourcing.domain import (
    event,
)

from .inquery import Inquery, InqueryDTO

from typing_extensions import Self

class Call(Inquery):
    @event("Created")
    def __init__(self, callerid: str) -> None:
        self.callerid = callerid

class CallDTO(InqueryDTO):
    callerid: str
