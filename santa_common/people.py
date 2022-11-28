"""
A module for describing people.
"""
from typing import List
from .houses import Household


class Person:
    def __init__(
        self,
        first: str,
        last: str,
        email: str,
        household: Household,
        cc: List[str] = None,
    ):
        self.first = first
        self.last = last
        self.email = email
        self.household = household
        self.cc = cc

    def __hash__(self):
        return hash((self.first, self.last, self.email, self.household))

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __repr__(self):
        return f"{self.first} {self.last}"


# TODO create people and put them in here
EVERYONE = ()
