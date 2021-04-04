from .base_rule import BaseRiskScoreRule


class HomeRiskScoreRule(BaseRiskScoreRule):

    key = 'home'

    def calculate(self):

        if not self.user_data.house:
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
