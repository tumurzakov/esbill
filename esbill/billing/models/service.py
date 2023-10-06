from esbill.common import DTO, Aggregate, event

class ServiceDTO(DTO):
    name: str

class Service(Aggregate):
    @event("Created")
    def __init__(self, service_dto: ServiceDTO) -> None:
        self.__dict__.update(service_dto.__dict__)

    @event("Updated")
    def update(self, service_dto: ServiceDTO) -> None:
        self.__dict__.update(service_dto.__dict__)
