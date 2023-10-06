from esbill.common import event, Aggregate, DTO, UUID

class ChannelDTO(DTO):
    name: str
    alias: str

class Channel(Aggregate):
    @event("Created")
    def __init__(self, dto: ChannelDTO) -> None:
        self.__dict__.update(dto.__dict__)

    @event("Updated")
    def update(self, dto: ChannelDTO) -> None:
        self.__dict__.update(dto.__dict__)
