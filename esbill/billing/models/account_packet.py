from esbill.common import UUID, Aggregate, event

class AccountPacket(Aggregate):

    @event("Created")
    def __init__(self, packet_id: UUID) -> None:
        self.packet_id = packet_id
