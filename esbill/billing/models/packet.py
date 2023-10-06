from typing import Dict
from esbill.common import DTO, Aggregate, event, UUID

class PacketDTO(DTO):
    name: str
    services: Dict[UUID, Dict]

class Packet(Aggregate):
    services: Dict[UUID, Dict]

    @event("Created")
    def __init__(self, packet_dto: PacketDTO) -> None:
        self.__dict__.update(packet_dto.__dict__)

    @event("Updated")
    def update(self, packet_dto: PacketDTO) -> None:
        self.__dict__.update(packet_dto.__dict__)

    @event("ServiceAdded")
    def add_service(self, service_id: UUID) -> None:
        self.services[service_id] = {}

    @event("ServiceDeleted")
    def delete_service(self, service_id: UUID) -> None:
        del(self.services[service_id])

