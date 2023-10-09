from uuid import UUID

from typing import List

from esbill.common import Command

from esbill.crm.models import (
    Inquery,
    InqueryDTO,
    Task,
    TaskDTO,
)

from .task_command import TaskCommand

class InqueryCommand(Command):
    task_cmd: TaskCommand = None

    def create(self, dto: InqueryDTO) -> UUID:
        aggregate = Inquery(dto)
        self.save(aggregate)
        return aggregate.id

    def update(self, dto: InqueryDTO) -> None:
        assert dto.id is not None
        aggregate: Inquery = self.repository.get(dto.id)
        aggregate.update(dto)
        self.save(aggregate)

    def get(self, id: UUID) -> InqueryDTO:
        aggregate: Inquery = self.repository.get(id)
        return InqueryDTO.from_aggregate(aggregate)

    def create_task(self, id: UUID, task_dto: TaskDTO) -> None:
        aggregate: Inquery = self.repository.get(id)
        task_id = self.task_cmd.create(task_dto)
        aggregate.add_task(task_id)
        self.save(aggregate)
        return task_id

    def get_tasks(self, id: UUID) -> List[UUID]:
        aggregate: Inquery = self.repository.get(id)
        return aggregate.get_tasks()


