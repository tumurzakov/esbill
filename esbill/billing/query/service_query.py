from typing import List
from esbill.billing.models import Service, ServiceDTO
from esbill.common import db, Projection, singledispatchmethod

import logging

class ServiceQuery(Projection):
    @singledispatchmethod
    def policy(self, domain_event, process_event):
        """Default policy"""

    @policy.register(Service.Created)
    def _(self, domain_event, process_event):
        service_dto = domain_event.service_dto
        service_dto['id'] = domain_event.originator_id
        db.save('services', service_dto)

    @policy.register(Service.Updated) # type: ignore[attr-defined]
    def _(self, domain_event, process_event):
        service_dto = domain_event.service_dto
        db.save('services', service_dto)

    def read_all(self) -> List[ServiceDTO]:
        entries = db.read_all('services')
        return [ServiceDTO.from_dict(entries[key]) for key in entries]


