from typing import Optional

from value_objects.email import Email
from value_objects.money import Currency, Money


class Item:
    def __init__(self, price: Money):
        self.price = price


class Shop:
    def __init__(self, balance_currency: Optional[Currency] = Currency.USD):
        self.email_address: Optional[str] = None
        if not balance_currency:
            balance_currency = Currency.USD
        self.balance = Money(0, balance_currency)

    @property
    def email(self) -> Optional[Email]:
        return Email(self.email_address)

    @email.setter
    def email(self, email_address: str) -> None:
        self.email_address = Email(email_address).address

    def sell_item(self, item: Item) -> None:
        self.balance = self.balance.add(item.price)
