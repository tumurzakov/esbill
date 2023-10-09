from unittest import TestCase
from esbill.common import UUID, uuid4
from esbill.crm  import InqueryCommand, TaskCommand
from esbill.crm.models import InqueryDTO, Task, TaskDTO

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

    def test_create_task(self) -> None:
        dto = InqueryDTO(channel_id=uuid4())
        cmd = InqueryCommand()
        cmd.task_cmd = TaskCommand()

        id = cmd.create(dto)
        assert id is not None
        assert isinstance(id, UUID)

        task_dto = TaskDTO(title='Hello')
        task_id = cmd.create_task(id, task_dto)
        assert task_id is not None

        tasks = cmd.get_tasks(id)
        assert len(tasks) == 1

    def test_create_customer_task(self) -> None:
        dto = InqueryDTO(
                channel_id=uuid4(),
                title='I want to subscribe',
                details='Name: John Smith, address: Chui Ave, 1, Apt. 1',
                )
        cmd = InqueryCommand()
        cmd.task_cmd = TaskCommand()

        id = cmd.create(dto)
        assert id is not None
        assert isinstance(id, UUID)

        task_dto = TaskDTO(
            title='Connect the customer',
            extras=[TaskDTO.CreateCustomerExtra(
                customer_name="John Smith",
                customer_address="Chui Ave, 1, Apt. 1",
            )]
        )
        task_id = cmd.create_task(id, task_dto)
        assert task_id is not None

        tasks = cmd.get_tasks(id)
        assert len(tasks) == 1

        task = cmd.task_cmd.get(tasks[0])
        assert task.customer_name == 'John Smith'
