from eventsourcing.domain import (
    event,
)

from typing import Optional, Any
from typing_extensions import Self
from pydantic import BaseModel
from uuid import UUID

from esbill.common.aggregate import Aggregate
from esbill.common.dto import DTO

class InqueryDTO(DTO):
    id: Optional[UUID] = None
    name: Optional[str] = None
    reason: Optional[str] = None
    customer_id: Optional[UUID] = None

class Inquery(Aggregate):
    @event("Created")
    def __init__(self) -> None:
        pass

    @event("Updated")
    def update(self, inquery: InqueryDTO) -> None:
        self.name = inquery.name
        self.reason = inquery.reason
        self.customer_id = inquery.customer_id
