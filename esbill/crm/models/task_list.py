from esbill.common import event, Aggregate, DTO, UUID

class TaskListDTO(DTO):
    pass

class TaskList(Aggregate):
    @event("Created")
    def __init__(self, dto: TaskListDTO) -> None:
        self.__dict__.update(dto.__dict__)

    @event("Updated")
    def update(self, dto: TaskListDTO) -> None:
        self.__dict__.update(dto.__dict__)
