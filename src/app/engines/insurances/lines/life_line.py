from app.data.contants import insurances_line
from app.engines.insurances.common.insurance_line import InsuranceLine
from app.engines.insurances.lines.rules import personal


class LifeInsuranceLine(InsuranceLine):

    key = insurances_line.InsurancesLineKey.LIFE
    rules = (
        personal.OldAgeRule,
        personal.YoungAgeRule,
        personal.AdultAgeRule,
        personal.HighIncomeRule,
        personal.HasDependentsRule,
        personal.MarriedRule,
    )
