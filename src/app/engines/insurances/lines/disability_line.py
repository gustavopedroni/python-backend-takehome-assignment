from app.data.contants import insurances_line
from app.engines.insurances.common.insurance_line import InsuranceLine
from app.engines.insurances.lines.rules import house, personal


class DisabilityInsuranceLine(InsuranceLine):

    key = insurances_line.InsurancesLineKey.DISABILITY
    rules = (
        personal.NotHaveIncomeRule,
        personal.OldAgeRule,
        personal.AdultAgeRule,
        personal.YoungAgeRule,
        personal.HighIncomeRule,
        house.HouseMortgagedRule,
        personal.HasDependentsRule,
        personal.MarriedRule,
    )
