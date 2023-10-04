from unittest import TestCase
from uuid import UUID
from esbill.crm import InqueryApp, Call, CallDTO, Inquery, InqueryDTO

class TestInquery(TestCase):
    def test_register_call(self) -> None:
        inquery_app = InqueryApp()
        call = inquery_app.register_call("0555555555")
        assert call is not None
        assert isinstance(call, CallDTO)

    def test_update(self) -> None:
        inquery_app = InqueryApp()
        call_1 = inquery_app.register_call("0555555555")
        assert call_1 is not None

        inquery = InqueryDTO()
        inquery.id = call_1.id
        inquery.name = "name"
        inquery_app.update(inquery)

        call_2 = inquery_app.get_call(call_1.id)
        assert call_2 is not None
        assert call_1.id == call_2.id
