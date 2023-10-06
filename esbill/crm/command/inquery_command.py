from uuid import UUID

from esbill.common import Command

from esbill.crm.models import (
    Inquery,
    InqueryDTO,
)

class InqueryCommand(Command):
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
