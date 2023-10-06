from eventsourcing.system import SingleThreadedRunner
from .system import system

runner = SingleThreadedRunner(system)
