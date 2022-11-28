"""
Helps pair people up for secret santa
"""
import random
from typing import Tuple, List
from .people import Person
import logging

MAX_TRIES = 10


def make_pairs(all_people: Tuple[Person]) -> List[Tuple[Person, Person]]:
    pairs = []
    tries = 0

    # Basically we loop because it's not always perfect when we assign someone to a gifter. It's possible we exhaust
    # the valid receivers before we do all of the gifters because people life in the same household or something.
    # So we loop and this seems to work (almost) all of the time. At the low, low cost of CPU!
    while tries < MAX_TRIES:
        tries += 1
        try:
            pairs = _try_pair(all_people)
        except IndexError as ie:
            logging.info(
                "IndexError because we cannot always slice people into pairs evenly. Trying again... (%d)",
                tries,
            )
        else:
            break

    if not pairs:
        raise ValueError(f"After {MAX_TRIES} tries we failed to make valid pairs.")
    return pairs


def _try_pair(all_people):
    receivers = list(all_people)[:]  # copy
    pairs = []

    # Assign each giver one receiver that is not from their household
    for giver in all_people:
        # Sometimes this throws an IndexError because unluckily there is NO receiver not in the giver's household
        receiver = random.choice(
            [r for r in receivers if r.household != giver.household]
        )

        receivers.remove(receiver)
        pairs.append((giver, receiver))

    return pairs
