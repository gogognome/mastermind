import random
from typing import Sequence, Tuple

import attr


@attr.s(auto_attribs=True)
class Score:
    correct_position: int
    wrong_position: int

    @classmethod
    def determine(cls, guess: Sequence, code: Sequence) -> "Score":
        if len(guess) != len(code):
            raise ValueError(f"The guess must have a length of {len(code)}.")

        correct_position = 0
        wrong_position = 0
        counted_positions = set()  # Tracks counted correct and wrong positions.

        # Count correct positions
        for i in range(len(guess)):
            if guess[i] == code[i]:
                correct_position += 1
                counted_positions.add(i)

        # Count wrong positions
        for i in range(len(guess)):
            for j in range(len(code)):
                if guess[i] == code[j] and j not in counted_positions:
                    wrong_position += 1
                    counted_positions.add(j)
                    break

        return Score(correct_position=correct_position, wrong_position=wrong_position)


class Game:
    def __init__(self, symbols: Sequence = "123456", code_len: int = 4) -> None:
        self.symbols = symbols
        self.code_len = code_len
        self._code = random.sample(symbols, code_len)
        self.guesses_and_scores: list[Tuple[Sequence, Score]] = []
        self.is_over = False

    def play(self, guess: Sequence) -> Score:
        """
        Play a guess. The guess and its score are stored.
        If the code is guessed, the `is_over` field is set to `True`.

        :param guess: the guess.
        :return: the score of the guess
        """
        score = Score.determine(guess, self._code)
        self.guesses_and_scores.append((guess, score))

        if score.correct_position == len(guess):
            self.is_over = True

        return score

    @property
    def number_attempts(self) -> int:
        """:return: the number of guessed made so far."""
        return len(self.guesses_and_scores)
