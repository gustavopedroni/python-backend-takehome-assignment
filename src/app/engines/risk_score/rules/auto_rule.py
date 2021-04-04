from datetime import datetime

from .base_rule import BaseRiskScoreRule


class AutoRiskScoreRule(BaseRiskScoreRule):

    key = 'auto'

    def calculate(self):

        if not self.user_data.vehicle:
            self._num_score = None
            return self.final_score

        if self.user_data.age < 30:
            self._num_score -= 2

        if 30 <= self.user_data.age <= 40:
            self._num_score -= 1

        if self.user_data.income > 200000:
            self._num_score -= 1

        if self.user_data.vehicle and self.user_data.vehicle.year >= (datetime.now().year - 5):
            self._num_score += 1
