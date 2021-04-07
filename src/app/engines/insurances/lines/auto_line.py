from app.data.contants import insurances_line
from app.engines.insurances.common.insurance_line import InsuranceLine
from app.engines.insurances.lines.rules import personal, vehicle


class AutoInsuranceLine(InsuranceLine):

    key = insurances_line.InsurancesLineKey.AUTO
    rules = (
        vehicle.NotHaveVehicleRule,
        personal.YoungAgeRule,
        personal.AdultAgeRule,
        personal.HighIncomeRule,
        vehicle.VehicleProducedLast5YearsRule,
    )
