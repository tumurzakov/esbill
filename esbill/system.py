from eventsourcing.system import System

from esbill.crm import InqueryCommand, InqueryQuery
from esbill.billing import ServiceCommand, ServiceQuery

system = System(pipes=[
    [InqueryCommand, InqueryQuery],
    [ServiceCommand, ServiceQuery],
])
