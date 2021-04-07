from enum import Enum


class FinalScoreEnum(str, Enum):
    ECONOMIC = 'economic'
    REGULAR = 'regular'
    RESPONSIBLE = 'responsible'
    INELIGIBLE = 'ineligible'
