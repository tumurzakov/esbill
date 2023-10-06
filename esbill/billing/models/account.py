from typing import Dict
from esbill.common import event, Aggregate, DTO, UUID

class PacketNotSubscribedError(Exception):
    pass

class AccountDTO(DTO):
    customer_id: UUID
    packets: Dict[UUID, Dict]

class Account(Aggregate):
    customer_id: UUID
    packets: Dict[UUID, Dict]

    @event("Created")
    def __init__(self, customer_id: UUID) -> None:
        self.customer_id = customer_id
        self.packets = {}

    @event("PacketSubscribed")
    def subscribe(self, account_packet_id: UUID) -> None:
        self.packets[account_packet_id] = {}

    @event("PacketUnsubscribed")
    def unsubscribe(self, account_packet_id: UUID) -> None:
        if account_packet_id not in self.packets:
            raise PacketNotSubscribedError()
        del(self.packets[account_packet_id])

    @event("Terminated")
    def terminate(self) -> None:
        pass
