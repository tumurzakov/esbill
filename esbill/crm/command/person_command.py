from uuid import UUID

from esbill.common import Command

from esbill.crm.models import (
    Person,
    PersonDTO,
)

class PersonCommand(Command):
    def create(self, dto: PersonDTO) -> UUID:
        aggregate = Person(dto)
        self.save(aggregate)
        return aggregate.id

    def update(self, dto: PersonDTO) -> None:
        assert dto.id is not None
        aggregate: Person = self.repository.get(dto.id)
        aggregate.update(dto)
        self.save(aggregate)

    def get(self, id: UUID) -> PersonDTO:
        aggregate: Person = self.repository.get(id)
        return PersonDTO.from_aggregate(aggregate)
