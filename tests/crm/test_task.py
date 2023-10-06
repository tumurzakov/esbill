from unittest import TestCase
from esbill.common import UUID, uuid4
from esbill.crm.models import Task, TaskDTO

class TestTask(TestCase):
    def test_create(self) -> None:
        dto = TaskDTO.construct(
                mixin_names=['TaskList'],
                creator_id = uuid4(),
                task_list_id = uuid4(),
        )
        assert dto.__module__ == 'esbill.crm.models.task'
        assert dto.__class__.__name__ == 'TaskListTaskDTO'

        task = Task.construct(dto)
        assert task.__module__ == 'esbill.crm.models.task'
        assert task.__class__.__name__ == 'TaskListTask'

        events = task.collect_events()
        assert len(events) == 1
        assert events[0].__class__.__name__ == 'Created'
        assert events[0].dto == dto

