from typing import List
from esbill.common import db, Projection, singledispatchmethod

from esbill.crm.models import (
    Person,
    PersonDTO,
)

import logging

class PersonQuery(Projection):
    @singledispatchmethod
    def policy(self, domain_event, process_event):
        """Default policy"""

    @policy.register(Person.Created)
    def _(self, domain_event, process_event):
        dto = domain_event.person_dto
        dto['id'] = domain_event.originator_id
        db.save('person', dto)

    @policy.register(Person.Updated)  # type: ignore[attr-defined]
    def _(self, domain_event, process_event):
        dto = domain_event.person_dto
        db.save('person', dto)

    def read_all(self) -> List[PersonDTO]:
        entries = db.read_all('person')
        return [PersonDTO.from_dict(entries[key]) for key in entries]
