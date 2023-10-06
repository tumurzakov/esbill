from esbill.api import app

from esbill.crm.api import InqueryRouter
from esbill.billing.api import ServiceRouter

from .runner import runner

app.include_router(InqueryRouter(runner).router)
app.include_router(ServiceRouter(runner).router)
