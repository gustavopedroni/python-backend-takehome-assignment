from datetime import datetime
from app.data.schemas.personal.vehicle import VehicleSchema
from app.engines.insurances.common.base.base_rule import BaseRule
from app.data.contants.insurances_line import InsurancesLineKey

__all__ = (
    'NotHaveVehicleRule',
    'VehicleProducedLast5YearsRule',
)


class NotHaveVehicleRule(BaseRule):

    def apply(self, data, score):

        if self.line_key is InsurancesLineKey.AUTO and not data.vehicle:
            return None

        return score


class VehicleProducedLast5YearsRule(BaseRule):

    def apply(self, data, score):

        if not data.vehicle:
            return score

        vehicle: VehicleSchema = data.vehicle

        if self.line_key is InsurancesLineKey.AUTO and vehicle.year >= (datetime.now().year - 5):
            return score + 1

        return score
