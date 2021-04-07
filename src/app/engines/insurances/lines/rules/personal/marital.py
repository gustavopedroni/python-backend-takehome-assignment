from app.data.contants.insurances_line import InsurancesLineKey
from app.engines.insurances.common.base.base_rule import BaseRule

__all__ = ("MarriedRule",)


class MarriedRule(BaseRule):
    def apply(self, data, score):

        if not isinstance(data.marital_status, str):
            return score

        marital_status: str = data.marital_status

        if marital_status == "married":

            if self.line_key is InsurancesLineKey.LIFE:
                return score + 1

            if self.line_key is InsurancesLineKey.DISABILITY:
                return score - 1

        return score
