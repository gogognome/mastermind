from typing import Callable, Sequence

from mastermind.computer_player import suggest_next_guess
from mastermind.game import Game


def play_game(produce_guess: Callable[[Game], Sequence]) -> None:
    """Play a single game of Mastermind using a character-based user interface."""
    game = Game()
    print(
        f"I chose a code of length {game.code_len} " f"from the symbols {game.symbols}"
    )
    while not game.is_over:
        print("Enter your guess:")
        guess = produce_guess(game)
        try:
            score = game.play(guess)
            print(
                f"At correct position: {score.correct_position}, "
                f"at wrong position: {score.wrong_position}"
            )
        except ValueError as e:
            print(e)

    print(f"You guessed the code in {game.number_attempts} attempts!")


def print_computer_guess(game: Game) -> Sequence:
    guess = suggest_next_guess(game)
    print("".join(guess))
    return guess


def get_human_guess(_: Game) -> Sequence:
    return input()


if __name__ == "__main__":
    # Select human or computer as guess producer.
    # guess_producer = get_human_guess
    guess_producer = print_computer_guess
    play_game(guess_producer)
