from uuid import UUID
from esbill.api import app
from esbill.crm import CRMApp
crm = CRMApp()

@app.get("/crm/customer/{customer_id}")
def get_customer(customer_id: UUID):
    try:
        customer = crm.get_customer(customer_id)
    except Exception as e:
        return {"error": e.__class__.__name__}
    return customer


@app.post("/crm/customer")
def register_customer():
    try:
        customer_id = crm.register_customer()
    except Exception as e:
        return {"error": e.__class__.__name__}
    return customer_id

