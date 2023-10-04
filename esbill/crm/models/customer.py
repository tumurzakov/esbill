from eventsourcing.domain import (
    Aggregate,
    event,
)

from esbill.common.dto import DTO
from esbill.crm.models.inquery_channel import Inquery
from esbill.crm.models.service import Service

class CustomerDTO(DTO):
    pass

class Customer(Aggregate):
    @event("Created")
    def __init__(self) -> None:
        pass

    @event("InqueryRequested")
    def request(self, inquery: Inquery) -> None:
        pass

    @event("ServiceSubscribed")
    def subscribe(self, service: Service) -> None:
        pass

    @event("ServiceUnsubscribed")
    def unsubscribe(self, service: Service) -> None:
        pass

    @event("Terminated")
    def terminate(self) -> None:
        pass
