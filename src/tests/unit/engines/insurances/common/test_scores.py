import pytest

from app.data.contants.final_score import FinalScoreEnum
from app.engines.insurances.common.final_score import FinalScore


@pytest.mark.parametrize(
    "value,response",
    (
        (-100, FinalScoreEnum.ECONOMIC),
        (0, FinalScoreEnum.ECONOMIC),
        (1, FinalScoreEnum.REGULAR),
        (2, FinalScoreEnum.REGULAR),
        (3, FinalScoreEnum.RESPONSIBLE),
        (100, FinalScoreEnum.RESPONSIBLE),
        (None, FinalScoreEnum.INELIGIBLE),
    ),
)
def test_final_score(value, response, final_score: FinalScore):
    """Test if FinalScore respects the business rule

    score is None       - FinalScoreEnum.INELIGIBLE
    num_score >= 0      - FinalScoreEnum.ECONOMIC
    1 <= num_score <= 2 - FinalScoreEnum.REGULAR
    score >= 3          - FinalScoreEnum.RESPONSIBLE
    """

    final_score.num_score = value
    assert final_score.get_final_score() == response
