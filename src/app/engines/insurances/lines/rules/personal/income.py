from app.data.contants.insurances_line import InsurancesLineKey
from app.engines.insurances.common.base.base_rule import BaseRule

__all__ = (
    'NotHaveIncomeRule',
    'HighIncomeRule',
)


class NotHaveIncomeRule(BaseRule):

    def apply(self, data, score):

        if self.line_key is InsurancesLineKey.DISABILITY and not data.income:
            return None

        return score


class HighIncomeRule(BaseRule):

    def apply(self, data, score):

        if not isinstance(data.income, int):
            return score

        income: int = data.income

        if income > 200_000:
            return score - 1

        return score

