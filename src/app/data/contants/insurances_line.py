from enum import Enum


class InsurancesLineKey(str, Enum):
    AUTO = 'auto'
    DISABILITY = 'disability'
    HOME = 'home'
    LIFE = 'life'

    GENERIC = 'generic'

    @classmethod
    def _missing_(cls, value):
        return cls.GENERIC
