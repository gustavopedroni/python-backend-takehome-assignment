import pytest

from app.engines.insurances import lines
from app.engines.insurances.lines.rules import vehicle, personal, house


@pytest.mark.parametrize(
    "line,rules",
    [
        (
            lines.AutoInsuranceLine,
            (
                vehicle.NotHaveVehicleRule,
                personal.YoungAgeRule,
                personal.AdultAgeRule,
                personal.HighIncomeRule,
                vehicle.VehicleProducedLast5YearsRule,
            )
        ),
        (
            lines.DisabilityInsuranceLine,
            (
                personal.NotHaveIncomeRule,
                personal.OldAgeRule,
                personal.AdultAgeRule,
                personal.YoungAgeRule,
                personal.HighIncomeRule,
                house.HouseMortgagedRule,
                personal.HasDependentsRule,
                personal.MarriedRule,
            )
        ),
        (
            lines.HomeInsuranceLine,
            (
                house.NotHaveHouseRule,
                personal.YoungAgeRule,
                personal.AdultAgeRule,
                personal.HighIncomeRule,
                house.HouseMortgagedRule,
            )
        ),
        (
            lines.LifeInsuranceLine,
            (
                personal.OldAgeRule,
                personal.YoungAgeRule,
                personal.AdultAgeRule,
                personal.HighIncomeRule,
                personal.HasDependentsRule,
                personal.MarriedRule,
            )
        )
    ]
)
def test_check_rules_insurance_line(line, rules):
    """ Check if All Insurance Lines has all rules
    """
    assert all(r in line.rules for r in rules)
