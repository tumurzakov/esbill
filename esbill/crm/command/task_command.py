from uuid import UUID

from esbill.common import Command

from esbill.crm.models import (
    Task,
    TaskDTO,
)

class TaskCommand(Command):
    def create(self, dto: TaskDTO) -> UUID:
        aggregate = Task(dto)
        self.save(aggregate)
        return aggregate.id

    def update(self, dto: TaskDTO) -> None:
        assert dto.id is not None
        aggregate: Task = self.repository.get(dto.id)
        aggregate.update(dto)
        self.save(aggregate)

    def get(self, id: UUID) -> TaskDTO:
        aggregate: Task = self.repository.get(id)
        return TaskDTO.from_aggregate(aggregate)
