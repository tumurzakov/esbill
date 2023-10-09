from esbill.common import event, Aggregate, DTO, UUID, uuid4, DomainEvent
from typing import Any, Callable, Dict, Iterable, Optional, Tuple, TypeVar, List
from typing_extensions import Self
from dataclasses import dataclass

class TaskDTO(DTO):
    creator_id: Optional[UUID] = None
    assignee_id: Optional[UUID] = None
    title: Optional[str] = None
    description: Optional[str] = None
    status_id: Optional[UUID] = None
    extras: Optional[List[Any]] = None

    def __getattr__(self, name: str) -> Any:
        if name in self.__dict__:
            return self.__dict__[name]

        if self.extras is not None:
            for extra in self.extras:
                # due to ussing orjson decoder data could be returned as dict
                dict_ = extra if isinstance(extra, dict) else extra.__dict__
                if name in dict_:
                    return dict_[name]

        raise KeyError(name)

    @dataclass
    class TaskListExtra:
        task_list_id: Optional[UUID]

    @dataclass
    class HierarchicalExtra:
        parent_id: Optional[UUID]

    @dataclass
    class ProcessExtra:
        process_id: Optional[UUID]

    @dataclass
    class CreateCustomerExtra:
        customer_name: Optional[str]
        customer_address: Optional[str]

class Task(Aggregate):
    @event("Created")
    def __init__(self, dto: TaskDTO) -> None:
        self.__dict__.update(dto.__dict__)

    @event("Updated")
    def update(self, dto: TaskDTO) -> None:
        self.__dict__.update(dto.__dict__)
