"""
Definitions for households
"""


class Household:
    def __init__(self, address_1: str, address_2: str, notes: str = None):
        """
        Describes a home/address.
        :param address_1:  Addr line 1
        :param address_2:  Addr line 2
        :param notes: Any special notes for this address for the delivery people to know.
        """
        self.address_1 = address_1
        self.address_2 = address_2
        self.notes = notes

    def __hash__(self):
        return hash((self.address_1, self.address_2, self.notes))

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __repr__(self):
        return self.address_1 + " " + self.address_2

# TODO create households and put them here
