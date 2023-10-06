from esbill.common import event, Aggregate, DTO, UUID
from typing import Optional, List
from typing_extensions import Self

_class_cache = {}

def construct(name:str, mixins:tuple, dict:dict):
    if name in _class_cache:
        return _class_cache[name]
    else:
        dict['__module__'] = __name__
        t = type(name, mixins, dict)
        _class_cache[name] = t
        return t

class TaskDTO(DTO):
    creator_id: Optional[UUID] = None
    assignee_id: Optional[UUID] = None
    title: Optional[str] = None
    description: Optional[str] = None
    status_id: Optional[UUID] = None
    mixins: Optional[List[str]] = None

    @staticmethod
    def construct(mixin_names, **kwargs):
        names = ['TaskDTO']
        mixins = [eval('TaskDTO')]
        for mixin in mixin_names:
            mixins.append(eval(mixin+"Mixin"))
            names.append(mixin)

        names.sort(reverse=True)

        task_mixins = [x.replace('DTO', '') for x in mixin_names]
        dto = construct(''.join(names), tuple(mixins), kwargs)(mixins=task_mixins, **kwargs)
        return dto


class Task(Aggregate):
    @event("Created")
    def __init__(self, dto: TaskDTO) -> None:
        self.__dict__.update(dto.__dict__)

    @staticmethod
    def construct(dto: TaskDTO) -> Self:
        names = ['Task']
        mixins = [eval('Task')]
        for mixin in dto.mixins:
            mixins.append(eval(mixin+'Mixin'))
            names.append(mixin)

        names.sort(reverse=True)

        task = construct(''.join(names), tuple(mixins), {})(dto)
        return task

    @event("Updated")
    def update(self, dto: TaskDTO) -> None:
        self.__dict__.update(dto.__dict__)

class TaskListDTOMixin:
    task_list_id: Optional[UUID]

class TaskListMixin:
    pass

class HierarchicalDTOMixin:
    parent_id: Optional[UUID]

class HierarchicalMixin:
    pass

class ProcessDTOMixin:
    process_id: Optional[UUID]

class ProcessMixin:
    pass
