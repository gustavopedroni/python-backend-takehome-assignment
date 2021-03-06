from typing import Iterable, Optional, Tuple, Type

from app.data.schemas.personal.information import PersonalInformationSchema
from app.data.schemas.score import FinalRiskScoreSchema, NumberRiskScoreSchema
from app.engines.insurances import lines
from app.engines.insurances.common.insurance_line import InsuranceLine


class InsurancesEngine:
    def __init__(
        self, insurances_lines: Optional[Iterable[Type[InsuranceLine]]] = None
    ):

        self.insurances_lines = (
            insurances_lines
            if insurances_lines
            else (
                lines.LifeInsuranceLine,
                lines.DisabilityInsuranceLine,
                lines.HomeInsuranceLine,
                lines.AutoInsuranceLine,
            )
        )

    def calculate(
        self, user_data: PersonalInformationSchema
    ) -> Tuple[FinalRiskScoreSchema, NumberRiskScoreSchema]:
        """Calculates the score for each of the insurance lines
        :param user_data: PersonalInformation
        :return: FinalRiskScoreSchema, NumberRiskScoreSchema
        """

        response_final = {}
        response_number = {}

        for rule_classes in self.insurances_lines:
            rule_instance = rule_classes(user_data=user_data)
            rule_instance.calculate()

            response_final[rule_classes.key.value] = rule_instance.get_final_score()
            response_number[rule_classes.key.value] = rule_instance.get_num_score()

        return (
            FinalRiskScoreSchema(**response_final),
            NumberRiskScoreSchema(**response_number),
        )
