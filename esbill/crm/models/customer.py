from esbill.common import event, Aggregate, DTO, UUID

class CustomerDTO(DTO):
    pass

class Customer(Aggregate):
    @event("Created")
    def __init__(self) -> None:
        pass
