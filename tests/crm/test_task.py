from unittest import TestCase
from esbill.common import UUID, uuid4
from esbill.crm.models import Task, TaskDTO

class TestTask(TestCase):
    def test_create(self) -> None:
        task_list_id = uuid4()

        dto = TaskDTO(
            creator_id = uuid4(),
            extras = [
                TaskDTO.TaskListExtra(
                    task_list_id = task_list_id,
                )
            ]
        )

        assert dto.task_list_id == task_list_id
