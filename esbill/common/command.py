from eventsourcing.application import Application
from eventsourcing.persistence import Mapper, Transcoder
from uuid import UUID
from .persistence import PydanticMapper, OrjsonTranscoder

class Command(Application):
    def construct_mapper(self) -> Mapper:
        return self.factory.mapper(
            transcoder=self.construct_transcoder(),
            mapper_class=PydanticMapper,
        )

    def construct_transcoder(self) -> Transcoder:
        return OrjsonTranscoder()
