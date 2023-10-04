from unittest import TestCase
from uuid import UUID
from esbill.crm import CRMApp

class TestCRMApp(TestCase):
    def test_register_customer(self) -> None:
        crm = CRMApp()
        customer_id = crm.register_customer()
        assert customer_id is not None
        assert isinstance(customer_id, UUID)

    def test_get_customer(self) -> None:
        crm = CRMApp()
        customer_id = crm.register_customer()
        assert customer_id is not None
        assert isinstance(customer_id, UUID)

        data = crm.get_customer(customer_id)
        assert data is not None
        assert data['id'] == customer_id

    def test_register_point(self) -> None:
        crm = CRMApp()
        point_id = crm.register_point()
        assert point_id is not None
        assert isinstance(point_id, UUID)
