from eventsourcing.system import System

from esbill.crm.command import (
        PersonCommand,
        CompanyCommand,
        InqueryChannelCommand,
        InqueryCommand,
)

from esbill.crm.query import (
        PersonQuery,
        CompanyQuery,
        InqueryChannelQuery,
        InqueryQuery,
)

from esbill.billing.command import (
        ServiceCommand,
)

from esbill.billing.query import (
        ServiceQuery,
)

# TODO: separate system for each boundary context
system = System(pipes=[
    # crm
    [PersonCommand, PersonQuery],
    [CompanyCommand, CompanyQuery],
    [InqueryChannelCommand, InqueryChannelQuery],
    [InqueryCommand, InqueryQuery],

    # billing
    [ServiceCommand, ServiceQuery],
])
