from typing import Type, Tuple

from app.engines.insurances.common.base.base_insurance_line import BaseInsuranceLine
from app.engines.insurances.common.base.base_rule import BaseRule
from .final_score import FinalScore


class InsuranceLine(BaseInsuranceLine, FinalScore):

    rules: Tuple[Type[BaseRule]]

    def __init__(self, *args, **kwargs):

        super(InsuranceLine, self).__init__(*args, **kwargs)

        self.base_score = sum(self.user_data.risk_questions)
        self.num_score = self.base_score

    def calculate(self):

        for r in self.rules:

            self.num_score = r(line_key=self.key) \
                .check(data=self.user_data, score=self.num_score)
