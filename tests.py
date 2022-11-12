import pytest
from controlers.create_investment import create_investment
from time import time


class UnitTests:
    def __init__(self):
        self.now = int(time())

    def test_create_investment_can_be_today(self):
        investment = create_investment("test", self.now, 500.00)
        assert investment['message'] == "Investment created succesfuly"

    def test_create_investment_cant_be_after_now(self):
        future = self.now + 500
        investment = create_investment("test", future, 500.00)
        assert investment['message'] == "Creation date can't be in future"

    def test_create_investment_can_be_on_past(self):
        past = self.now - 500
        investment = create_investment("test", past, 500.00)
        assert investment['message'] == "Investment created succesfuly"

    def test_create_investment_cant_have_negative_amount(self):
        investment = create_investment("test", self.now, -100.00)
        assert investment['message'] == "Investment can't have negative amount"

    def test_create_investment_cant_have_empty_owner(self):
        investment = create_investment("", self.now, 500.00)
        assert investment['message'] == "Investment owner can't be empty"

    def test_create_investment_with_invalid_owner(self):
        investment = create_investment("INVALID", self.now, 500.00)
        assert investment['message'] == "The owner is invalid"
