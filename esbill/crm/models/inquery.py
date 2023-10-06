from esbill.common import event, Aggregate, DTO, UUID
from typing import Optional

class InqueryDTO(DTO):
    channel_id: Optional[UUID] = None
    person_id: Optional[UUID] = None
    company_id: Optional[UUID] = None
    title: Optional[str] = None
    details: Optional[str] = None

class Inquery(Aggregate):
    @event("Created")
    def __init__(self, dto: InqueryDTO) -> None:
        self.__dict__.update(dto.__dict__)

    @event("Updated")
    def update(self, dto: InqueryDTO) -> None:
        self.__dict__.update(dto.__dict__)
