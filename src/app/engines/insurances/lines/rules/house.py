from app.data.schemas.personal.house import HouseSchema
from app.engines.insurances.common.base.base_rule import BaseRule
from app.data.contants.insurances_line import InsurancesLineKey

__all__ = (
    'NotHaveHouseRule',
    'HouseMortgagedRule',
)


class NotHaveHouseRule(BaseRule):

    def apply(self, data, score):

        if self.line_key is InsurancesLineKey.HOME and not data.house:
            return None

        return score


class HouseMortgagedRule(BaseRule):

    def apply(self, data, score):

        if not data.house:
            return score

        house: HouseSchema = data.house

        if self.line_key in (
            InsurancesLineKey.DISABILITY,
            InsurancesLineKey.HOME,
        ) and house.ownership_status == 'mortgaged':
            return score + 1

        return score
