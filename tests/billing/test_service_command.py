from unittest import TestCase
from esbill.common import UUID, uuid4
from esbill.billing  import ServiceCommand
from esbill.billing.models import ServiceDTO

class TestServiceCommand(TestCase):
    def test_create(self) -> None:
        dto = ServiceDTO(name='Test')
        cmd = ServiceCommand()
        id = cmd.create(dto)
        assert id is not None
        assert isinstance(id, UUID)

    def test_update(self) -> None:
        dto = ServiceDTO(name='Test')
        cmd = ServiceCommand()
        id = cmd.create(dto)
        assert id is not None
        assert isinstance(id, UUID)

        dto = ServiceDTO(id=id, name='Hello')
        cmd.update(dto)

        dto = cmd.get(id)
        assert dto is not None
        assert dto.name == 'Hello'
