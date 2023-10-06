from uuid import UUID

from esbill.common import Command

from esbill.crm.models import (
    Company,
    CompanyDTO,
)

class CompanyCommand(Command):
    def create(self, dto: CompanyDTO) -> UUID:
        aggregate = Company(dto)
        self.save(aggregate)
        return aggregate.id

    def update(self, dto: CompanyDTO) -> None:
        assert dto.id is not None
        aggregate: Company = self.repository.get(dto.id)
        aggregate.update(dto)
        self.save(aggregate)

    def get(self, id: UUID) -> CompanyDTO:
        aggregate: Company = self.repository.get(id)
        return CompanyDTO.from_aggregate(aggregate)
