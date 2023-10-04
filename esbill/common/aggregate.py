from datetime import datetime
from typing import Any, Dict, List
from uuid import UUID

from eventsourcing.domain import (
    Aggregate as BaseAggregate,
    CanInitAggregate,
    CanMutateAggregate,
    event,
)

from pydantic import BaseModel

class DomainEvent(BaseModel):
    originator_id: UUID
    originator_version: int
    timestamp: datetime

    class Config:
        allow_mutation = False
        arbitrary_types_allowed = True


class Aggregate(BaseAggregate):
    class Event(DomainEvent, CanMutateAggregate):
        pass

    class Created(Event, CanInitAggregate):
        originator_topic: str

