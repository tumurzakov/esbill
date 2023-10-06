from esbill.common import event, Aggregate, DTO, UUID

class CompanyDTO(DTO):
    name: str

class Company(Aggregate):
    @event("Created")
    def __init__(self, dto: CompanyDTO) -> None:
        self.__dict__.update(dto.__dict__)

    @event("Updated")
    def update(self, dto: CompanyDTO) -> None:
        self.__dict__.update(dto.__dict__)
