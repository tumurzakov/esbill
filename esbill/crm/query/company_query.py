from typing import List
from esbill.common import db, Projection, singledispatchmethod

from esbill.crm.models import (
    Company,
    CompanyDTO,
)

import logging

class CompanyQuery(Projection):
    @singledispatchmethod
    def policy(self, domain_event, process_event):
        """Default policy"""

    @policy.register(Company.Created)
    def _(self, domain_event, process_event):
        dto = domain_event.company_dto
        dto['id'] = domain_event.originator_id
        db.save('company', dto)

    @policy.register(Company.Updated)  # type: ignore[attr-defined]
    def _(self, domain_event, process_event):
        dto = domain_event.company_dto
        db.save('company', dto)

    def read_all(self) -> List[CompanyDTO]:
        entries = db.read_all('company')
        return [CompanyDTO.from_dict(entries[key]) for key in entries]
