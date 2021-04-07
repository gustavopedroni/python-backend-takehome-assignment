from pydantic import ConstrainedList


class RiskQuestionsSchema(ConstrainedList):
    item_type = bool
    min_items = 3
    max_items = 3
    __args__ = [bool]
