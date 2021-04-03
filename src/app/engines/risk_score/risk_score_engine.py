from app.data.schemas.risk_profile import personal_information
from app.data.schemas.risk_score import score
from app.engines.risk_score import rules as risk_rules


class RiskScoreEngine:

    def __init__(self, user_data: personal_information.PersonalInformationSchema, rules: list = None):
        self.user_data = user_data

        self._rules_classes = set(rules) if rules else (
            risk_rules.LifeRiskScoreRule,
            risk_rules.DisabilityRiskScoreRule,
            risk_rules.HomeRiskScoreRule,
            risk_rules.AutoRiskScoreRule
        )

        self._rules = []

    def get_scores(self) -> score.RiskNumberScoreSchema:

        scores = {}

        for rule in self._rules:
            scores[rule.key] = rule.score

        return score.RiskNumberScoreSchema(**scores)

    def calculate(self) -> score.RiskFinalScoreSchema:

        response = {}

        for rule_classes in self._rules_classes:
            rule_instance = rule_classes(self.user_data)
            response[rule_classes.key] = rule_instance.calculate()

            self._rules.append(rule_instance)

        return score.RiskFinalScoreSchema(**response)
