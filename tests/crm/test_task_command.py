from unittest import TestCase
from esbill.common import UUID, uuid4
from esbill.crm  import TaskCommand
from esbill.crm.models import TaskDTO

class TestTaskCommand(TestCase):
    def test_create(self) -> None:
        dto = TaskDTO.construct(['TaskList'])
        cmd = TaskCommand()
        id = cmd.create(dto)
        assert id is not None
        assert isinstance(id, UUID)

    def test_update(self) -> None:
        dto = TaskDTO.construct(['TaskList'])
        cmd = TaskCommand()
        id = cmd.create(dto)
        assert id is not None
        assert isinstance(id, UUID)

        dto = TaskDTO.construct(['TaskList'], id=id, title='Hello')
        cmd.update(dto)

        dto = cmd.get(id)
        assert dto is not None
        assert dto.title == 'Hello'
