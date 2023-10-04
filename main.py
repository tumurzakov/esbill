from esbill.api import app

import esbill.crm.api.routes_crm
import esbill.crm.api.routes_inquery

if __name__ == "__main__":
    import uvicorn
    import os

    os.environ['PERSISTENCE_MODULE'] = 'eventsourcing.sqlite'
    os.environ['SQLITE_DBNAME'] = ':memory:'

    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info", reload=True)
