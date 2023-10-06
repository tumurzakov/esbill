from esbill.common import event, Aggregate, DTO, UUID

class PersonDTO(DTO):
    name: str

class Person(Aggregate):
    @event("Created")
    def __init__(self, dto: PersonDTO) -> None:
        self.__dict__.update(dto.__dict__)

    @event("Updated")
    def update(self, dto: PersonDTO) -> None:
        self.__dict__.update(dto.__dict__)
