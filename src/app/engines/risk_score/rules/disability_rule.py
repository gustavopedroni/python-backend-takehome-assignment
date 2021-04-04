from .base_rule import BaseRiskScoreRule


class DisabilityRiskScoreRule(BaseRiskScoreRule):

    key = 'disability'

    def calculate(self):

        if not self.user_data.income or self.user_data.income == 0:
            self._num_score = None
            return self.final_score

        if self.user_data.age > 60:
            self._num_score = None
            return self.final_score

        if self.user_data.age < 30:
            self._num_score -= 2

        if 30 <= self.user_data.age <= 40:
            self._num_score -= 1

        if self.user_data.income > 200000:
            self._num_score -= 1

        if self.user_data.house and self.user_data.house.ownership_status == 'mortgaged':
            self._num_score += 1

        if self.user_data.dependents and self.user_data.dependents >= 1:
            self._num_score += 1

        if self.user_data.marital_status == 'married':
            self._num_score -= 1
