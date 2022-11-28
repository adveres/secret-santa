"""
Common test fixtures.
"""
import pytest

from santa_common.people import Person
from santa_common.houses import Household


@pytest.fixture
def email() -> str:
    return "fakeEmail@fakeEmailsRus.com"


@pytest.fixture
def email2() -> str:
    return "fakeEmail2@fakeEmailsRus.com"


@pytest.fixture
def household() -> Household:
    house = Household("2222 Robot Lane", "Epcot, FL 99999")
    return house


@pytest.fixture
def household_w_notes() -> Household:
    house_w_notes = Household(
        "1111 Robot Lane",
        "Epcot, FL 99999",
        "Some Amazon companies won't ship to a PO box, so the gifter may need to use the Amazon store "
        "that's downtown for pickups.",
    )
    return house_w_notes


@pytest.fixture
def person_simple(email: str, household: Household) -> Person:
    person = Person("Simple", "Person", email, household)
    return person


@pytest.fixture
def person_parent(email: str, household_w_notes: Household) -> Person:
    person = Person("Parent", "Person", email, household_w_notes)
    return person


@pytest.fixture
def person_child_w_parent(
    email: str, email2: str, household_w_notes: Household
) -> Person:
    person = Person("Child", "Person", email, household_w_notes, cc=[email2])

    return person
