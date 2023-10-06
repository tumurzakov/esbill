from uuid import UUID

from esbill.common import Command

from esbill.crm.models import (
    InqueryChannel,
    InqueryChannelDTO,
)

class InqueryChannelCommand(Command):
    def create(self, dto: InqueryChannelDTO) -> UUID:
        aggregate = InqueryChannel(dto)
        self.save(aggregate)
        return aggregate.id

    def update(self, dto: InqueryChannelDTO) -> None:
        assert dto.id is not None
        aggregate: InqueryChannel = self.repository.get(dto.id)
        aggregate.update(dto)
        self.save(aggregate)

    def get(self, id: UUID) -> InqueryChannelDTO:
        aggregate: InqueryChannel = self.repository.get(id)
        return InqueryChannelDTO.from_aggregate(aggregate)
