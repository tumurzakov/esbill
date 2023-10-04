from uuid import UUID
from esbill.api import app
from esbill.crm import InqueryApp, Inquery, Call

inquery_app = InqueryApp()

@app.get("/crm/inquery/call/{call_id}")
def get_call(call_id: UUID):
    try:
        call = inquery_app.get_call(call_id)
    except Exception as e:
        return {"error": e.__class__.__name__}
    return call

@app.post("/crm/inquery/call")
def register_call(call: Call):
    try:
        call_id = inquery_app.register_call(call.callerid)
    except Exception as e:
        return {"error": e.__class__.__name__}
    return call_id

@app.post("/crm/inquery/{call_id}")
def update_inquery(inquery: Inquery.Updated):
    try:
        inquery_app.update(inquery)
    except Exception as e:
        return {"error": e.__class__.__name__}


