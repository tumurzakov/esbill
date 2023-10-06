from esbill.common import event, Aggregate, DTO, UUID

class TaskStatusDTO(DTO):
    pass

class TaskStatus(Aggregate):
    @event("Created")
    def __init__(self, dto: TaskStatusDTO) -> None:
        self.__dict__.update(dto.__dict__)

    @event("Updated")
    def update(self, dto: TaskStatusDTO) -> None:
        self.__dict__.update(dto.__dict__)
