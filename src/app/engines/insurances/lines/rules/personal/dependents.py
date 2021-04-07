from app.data.contants.insurances_line import InsurancesLineKey
from app.engines.insurances.common.base.base_rule import BaseRule

__all__ = (
    'HasDependentsRule',
)


class HasDependentsRule(BaseRule):

    def apply(self, data, score):

        if not isinstance(data.dependents, int):
            return score

        dependents: int = data.dependents

        if self.line_key in (
            InsurancesLineKey.DISABILITY,
            InsurancesLineKey.LIFE,
        ) and dependents >= 1:
            return score + 1

        return score

