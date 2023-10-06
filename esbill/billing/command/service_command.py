from uuid import UUID

from esbill.common import Command

from esbill.billing.models import (
    Service,
    ServiceDTO,
)

class ServiceCommand(Command):
    def create(self, dto: ServiceDTO) -> UUID:
        aggregate = Service(dto)
        self.save(aggregate)
        return aggregate.id

    def update(self, dto: ServiceDTO) -> None:
        assert dto.id is not None
        aggregate: Service = self.repository.get(dto.id)
        aggregate.update(dto)
        self.save(aggregate)

    def get(self, id: UUID) -> ServiceDTO:
        aggregate: Service = self.repository.get(id)
        return ServiceDTO.from_aggregate(aggregate)
