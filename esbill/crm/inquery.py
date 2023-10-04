from typing import Any

from eventsourcing.application import (
        Application,
)

from eventsourcing.persistence import (
        Mapper,
        Transcoder,
)

from uuid import UUID

from esbill.crm.models.inquery_channel import (
        Inquery, InqueryDTO,
        Call, CallDTO,
)

from esbill.common import PydanticMapper, OrjsonTranscoder

class InqueryApp(Application):
    def register_call(self, callerid: str) -> UUID:
        call = Call(callerid)
        self.save(call)
        return CallDTO.from_aggregate(call)

    def get_call(self, call_id: UUID) -> Call:
        call: Call = self.repository.get(call_id)
        return CallDTO.from_aggregate(call)

    def update(self, update: Inquery) -> None:
        inquery: Inquery = self.repository.get(update.id)
        inquery.update(update)
        self.save(inquery)

    def construct_mapper(self) -> Mapper:
        return self.factory.mapper(
            transcoder=self.construct_transcoder(),
            mapper_class=PydanticMapper,
        )

    def construct_transcoder(self) -> Transcoder:
        return OrjsonTranscoder()
