from typing import List
from esbill.common import db, Projection, singledispatchmethod

from esbill.crm.models import (
    Inquery,
    InqueryDTO,
)

import logging

class InqueryQuery(Projection):
    @singledispatchmethod
    def policy(self, domain_event, process_event):
        """Default policy"""

    @policy.register(Inquery.Created)
    def _(self, domain_event, process_event):
        dto = domain_event.inquery_dto
        dto['id'] = domain_event.originator_id
        db.save('inquery', dto)

    @policy.register(Inquery.Updated) # type: ignore[attr-defined]
    def _(self, domain_event, process_event):
        dto = domain_event.inquery_dto
        db.save('inquery', dto)

    def read_all(self) -> List[InqueryDTO]:
        entries = db.read_all('inquery')
        return [InqueryDTO.from_dict(entries[key]) for key in entries]
