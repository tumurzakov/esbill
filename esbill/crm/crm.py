from eventsourcing.application import Application
from uuid import UUID

from esbill.crm.models import (
        Customer, CustomerDTO,
        Point,
)

class CRMApp(Application):
    def register_customer(self) -> UUID:
        customer = Customer()
        self.save(customer)
        return customer.id

    def get_customer(self, customer_id: UUID) -> CustomerDTO:
        customer: Customer = self.repository.get(customer_id)
        return CustomerDTO.from_aggregate(customer)

    def register_point(self) -> UUID:
        customer = Point()
        self.save(customer)
        return customer.id
