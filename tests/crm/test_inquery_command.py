from unittest import TestCase
from esbill.common import UUID, uuid4
from esbill.crm  import InqueryCommand
from esbill.crm.models import InqueryDTO

class TestInqueryCommand(TestCase):
    def test_create(self) -> None:
        dto = InqueryDTO(channel_id=uuid4())
        cmd = InqueryCommand()
        id = cmd.create(dto)
        assert id is not None
        assert isinstance(id, UUID)

    def test_update(self) -> None:
        dto = InqueryDTO(channel_id=uuid4())
        cmd = InqueryCommand()
        id = cmd.create(dto)
        assert id is not None
        assert isinstance(id, UUID)

        dto = InqueryDTO(id=id, title='Hello')
        cmd.update(dto)

        dto = cmd.get(id)
        assert dto is not None
        assert dto.title == 'Hello'
