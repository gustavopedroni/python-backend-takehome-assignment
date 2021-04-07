from app.data.contants.insurances_line import InsurancesLineKey
from app.engines.insurances.common.base.base_rule import BaseRule

__all__ = (
    'OldAgeRule',
    'AdultAgeRule',
    'YoungAgeRule',
)


class OldAgeRule(BaseRule):

    def apply(self, data, score):

        if not isinstance(data.age, int):
            return score

        age: int = data.age

        if self.line_key in (
            InsurancesLineKey.DISABILITY,
            InsurancesLineKey.LIFE,
        ) and age > 60:
            return None

        return score


class AdultAgeRule(BaseRule):

    def apply(self, data, score):

        if not isinstance(data.age, int):
            return score

        age: int = data.age

        if 30 <= age <= 40:
            return score - 1

        return score


class YoungAgeRule(BaseRule):

    def apply(self, data, score):

        if not isinstance(data.age, int):
            return score

        age: int = data.age

        if age < 30:
            return score - 2

        return score
