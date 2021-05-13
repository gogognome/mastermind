from typing import Sequence

import pytest

from mastermind.game import Score, Game


class TestScore:
    @pytest.mark.parametrize(
        "guess,code,expected_score",
        [
            ([1, 2, 3, 4], [1, 2, 3, 4], Score(4, 0)),
            ([1, 2, 3, 4], [4, 3, 2, 1], Score(0, 4)),
            ([1, 1, 1, 1], [1, 2, 1, 2], Score(2, 0)),
            ([1, 1, 1, 2], [3, 3, 3, 1], Score(0, 1)),
        ],
    )
    def test_score_valid_input(
        self, guess: Sequence, code: Sequence, expected_score: Score
    ) -> None:
        assert Score.determine(guess, code) == expected_score

    def test_score_different_lengths(self) -> None:
        with pytest.raises(ValueError) as cm:
            Score.determine([1], [2, 3])

        assert str(cm.value) == "The guess must have a length of 2."


class TestGame:
    def test_game_over_initially(self) -> None:
        game = Game()
        assert not game.is_over

    def test_game_not_over_after_invalid_guesses(self) -> None:
        game = Game("123456")
        game.play("1111")
        game.play("2222")
        assert not game.is_over

    def test_game_over_after_valid_guess(self) -> None:
        game = Game("111111", 3)
        game.play("111")
        assert game.is_over

    def test_game_stays_over_once_code_has_been_guessed(self) -> None:
        game = Game("111111", 3)
        game.play("111")
        game.play("222")
        assert game.is_over
