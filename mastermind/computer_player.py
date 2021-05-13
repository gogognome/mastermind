import itertools
import random
from typing import Sequence, Set, Iterable, Tuple

from mastermind.game import Game, Score


def suggest_next_guess(game: Game) -> Sequence:
    """
    Suggest a new guess based on the game.

    :param game: the game.
    :return: the guess
    """
    remaining_codes: Set[Sequence] = set()
    for permutation in itertools.permutations(game.symbols):
        remaining_codes.add(permutation[: game.code_len])

    # Remove codes based on scores.
    remaining_codes = {
        code
        for code in remaining_codes
        if fits_guesses_and_scores(code, game.guesses_and_scores)
    }

    print(f"Number of possible codes remaining: {len(remaining_codes)}")

    return list(remaining_codes)[random.randint(0, len(remaining_codes) - 1)]


def fits_guesses_and_scores(
    code: Sequence, guesses_and_scores: Iterable[Tuple[Sequence, Score]]
) -> bool:
    """
    Check if the code fits with `guesses_and_scores`.
    :param code: a code.
    :param guesses_and_scores: the guesses and scores played so far.
    :return: `True` if the code fits; `False` if it does not fit.
    """
    for guess, score in guesses_and_scores:
        if Score.determine(guess, code) != score:
            return False

    return True
