from esbill.common import event, Aggregate, DTO, UUID, uuid4
from typing import Optional, List
from .task import TaskDTO

class InqueryDTO(DTO):
    channel_id: Optional[UUID] = None
    person_id: Optional[UUID] = None
    company_id: Optional[UUID] = None
    title: Optional[str] = None
    details: Optional[str] = None

class Inquery(Aggregate):
    tasks: Optional[List[UUID]]

    @event("Created")
    def __init__(self, dto: InqueryDTO) -> None:
        self.__dict__.update(dto.__dict__)
        self.tasks = []

    @event("Updated")
    def update(self, dto: InqueryDTO) -> None:
        self.__dict__.update(dto.__dict__)

    @event("TaskAdded")
    def add_task(self, task_id: UUID) -> None:
        self.tasks.append(task_id)

    def get_tasks(self) -> List[UUID]:
        return self.tasks
