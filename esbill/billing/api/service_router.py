from fastapi import FastAPI, APIRouter
from uuid import UUID
from esbill.common import Runner
from esbill.billing import ServiceCommand, ServiceQuery
from esbill.billing.models import ServiceDTO
import logging

logger = logging.getLogger(__name__)

class ServiceRouter:
    def __init__(self, runner: Runner):
        self.runner = runner
        self.router = APIRouter()
        self.router.add_api_route("/billing/service", self.list, methods=["GET"])
        self.router.add_api_route("/billing/service/{id}", self.get, methods=["GET"])
        self.router.add_api_route("/billing/service", self.create, methods=["POST"])
        self.router.add_api_route("/billing/service/{id}", self.update, methods=["POST"])

    def list(self):
        query = self.runner.get(ServiceQuery)
        return query.read_all()

    def get(self, id: UUID):
        cmd = self.runner.get(ServiceCommand)
        try:
            dto = cmd.get(id)
        except Exception as e:
            return {"error": e.__class__.__name__}
        return dto

    def create(self, dto: ServiceDTO):
        cmd = self.runner.get(ServiceCommand)
        try:
            id = cmd.create(dto)
        except Exception as e:
            return {"error": e.__class__.__name__}
        return id

    def update(self, id: UUID, dto: ServiceDTO):
        cmd = self.runner.get(ServiceCommand)
        try:
            dto.id = id
            cmd.update(dto)
        except Exception as e:
            return {"error": e.__class__.__name__}

