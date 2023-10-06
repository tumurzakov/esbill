from typing import List
from esbill.common import db, Projection, singledispatchmethod

from esbill.crm.models import (
    InqueryChannel,
    InqueryChannelDTO,
)

import logging

class InqueryChannelQuery(Projection):
    @singledispatchmethod
    def policy(self, domain_event, process_event):
        """Default policy"""

    @policy.register(InqueryChannel.Created)
    def _(self, domain_event, process_event):
        dto = domain_event.inquery_channel_dto
        dto['id'] = domain_event.originator_id
        db.save('inquery_channel', dto)

    @policy.register(InqueryChannel.Updated)  # type: ignore[attr-defined]
    def _(self, domain_event, process_event):
        dto = domain_event.inquery_channel_dto
        db.save('inquery_channel', dto)

    def read_all(self) -> List[InqueryChannelDTO]:
        entries = db.read_all('inquery_channel')
        return [InqueryChannelDTO.from_dict(entries[key]) for key in entries]
