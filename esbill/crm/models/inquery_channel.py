from esbill.common import event, Aggregate, DTO, UUID

class InqueryChannelDTO(DTO):
    pass

class InqueryChannel(Aggregate):
    @event("Created")
    def __init__(self, dto: InqueryChannelDTO) -> None:
        self.__dict__.update(dto.__dict__)

    @event("Updated")
    def update(self, dto: InqueryChannelDTO) -> None:
        self.__dict__.update(dto.__dict__)
