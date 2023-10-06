from eventsourcing.system import ProcessApplication
from eventsourcing.dispatch import singledispatchmethod

class Projection(ProcessApplication):
    @singledispatchmethod
    def policy(self, domain_event, process_event):
        """Default policy"""

