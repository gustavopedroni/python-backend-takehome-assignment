from app.data.contants import insurances_line
from app.engines.insurances.common.insurance_line import InsuranceLine
from app.engines.insurances.lines.rules import house, personal


class HomeInsuranceLine(InsuranceLine):

    key = insurances_line.InsurancesLineKey.HOME
    rules = (
        house.NotHaveHouseRule,
        personal.YoungAgeRule,
        personal.AdultAgeRule,
        personal.HighIncomeRule,
        house.HouseMortgagedRule,
    )
