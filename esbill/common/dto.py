from typing import Optional, Any, Dict
from typing_extensions import Self
from pydantic import BaseModel
from uuid import UUID

from .aggregate import Aggregate

class DTO(BaseModel):
    id: Optional[UUID] = None

    @classmethod
    def from_aggregate(cls, aggregate: Aggregate) -> Self:
        obj = vars(aggregate)
        obj['id'] = obj['_id']
        return cls.parse_obj(obj)

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        return cls.parse_obj(obj)

