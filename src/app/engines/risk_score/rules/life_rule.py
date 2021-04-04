from .base_rule import BaseRiskScoreRule


class LifeRiskScoreRule(BaseRiskScoreRule):

    key = 'life'

    def calculate(self):

        if self.user_data.age > 60:
            self._num_score = None
            return self.final_score

        if self.user_data.age < 30:
            self._num_score -= 2

        if 30 <= self.user_data.age <= 40:
            self._num_score -= 1

        if self.user_data.income > 200000:
            self._num_score -= 1

        if self.user_data.dependents and self.user_data.dependents >= 1:
            self._num_score += 1

        if self.user_data.marital_status == 'married':
            self._num_score += 1
