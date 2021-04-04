from typing import Optional, Type

from app.data.schemas.risk_profile import personal_information as p_info
from app.data.schemas.risk_score import score
from app.engines.risk_score import rules as risk_rules
from app.engines.risk_score.rules import base_rule


class RiskScoreEngine:

    def __init__(self, rules: Optional[tuple] = None):

        self._rules_classes: tuple[Type[base_rule.BaseRiskScoreRule]] = rules if rules else (
            risk_rules.LifeRiskScoreRule,
            risk_rules.DisabilityRiskScoreRule,
            risk_rules.HomeRiskScoreRule,
            risk_rules.AutoRiskScoreRule,
        )

    def calculate(
        self,
        user_data: p_info.PersonalInformationSchema
    ) -> tuple[
        score.RiskFinalScoreSchema,
        score.RiskNumberScoreSchema,
    ]:

        response_final = {}
        response_number = {}

        for rule_classes in self._rules_classes:
            rule_instance = rule_classes(user_data=user_data)
            rule_instance.calculate()

            response_final[rule_classes.key] = rule_instance.final_score
            response_number[rule_classes.key] = rule_instance.num_score

        return (
            score.RiskFinalScoreSchema(**response_final),
            score.RiskNumberScoreSchema(**response_number)
        )
