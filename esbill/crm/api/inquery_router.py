from fastapi import FastAPI, APIRouter
from uuid import UUID
from esbill.common import Runner
from esbill.crm import InqueryCommand, InqueryQuery
from esbill.crm.models import InqueryDTO
import logging

logger = logging.getLogger(__name__)

class InqueryRouter:
    def __init__(self, runner: Runner):
        self.runner = runner
        self.router = APIRouter()
        self.router.add_api_route("/crm/inquery", self.list, methods=["GET"])
        self.router.add_api_route("/crm/inquery/{id}", self.get, methods=["GET"])
        self.router.add_api_route("/crm/inquery", self.create, methods=["POST"])
        self.router.add_api_route("/crm/inquery/{id}", self.update, methods=["POST"])

    def list(self):
        query = self.runner.get(InqueryQuery)
        return query.read_all()

    def get(self, id: UUID):
        cmd = self.runner.get(InqueryCommand)
        try:
            dto = cmd.get(id)
        except Exception as e:
            return {"error": e.__class__.__name__}
        return dto

    def create(self, dto: InqueryDTO):
        cmd = self.runner.get(InqueryCommand)
        try:
            id = cmd.create(dto)
        except Exception as e:
            return {"error": e.__class__.__name__}
        return id

    def update(self, id: UUID, dto: InqueryDTO):
        cmd = self.runner.get(InqueryCommand)
        try:
            dto.id = id
            cmd.update(dto)
        except Exception as e:
            return {"error": e.__class__.__name__}

