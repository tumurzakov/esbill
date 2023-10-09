from unittest import TestCase
from esbill.common import UUID, uuid4
from esbill.crm  import TaskCommand
from esbill.crm.models import TaskDTO

class TestTaskCommand(TestCase):
    def test_create(self) -> None:
        dto = TaskDTO()
        cmd = TaskCommand()
        id = cmd.create(dto)
        assert id is not None
        assert isinstance(id, UUID)

    def test_update(self) -> None:
        dto = TaskDTO()
        cmd = TaskCommand()
        id = cmd.create(dto)
        assert id is not None
        assert isinstance(id, UUID)

        task_list_id = uuid4()
        dto = TaskDTO(
            id=id,
            title='Hello',
            extras=[
                TaskDTO.TaskListExtra(task_list_id=task_list_id)
            ]
        )
        cmd.update(dto)

        dto = cmd.get(id)
        assert dto is not None
        assert dto.title == 'Hello'
