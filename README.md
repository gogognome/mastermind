# Mastermind

This application implements the game Mastermind, the game where a player
has to guess a code. In the original game, the code consists of colors.
In this game, the code consists of strings of digits, e.g. '5412'.

This application lets a human player guess a code and it can let the computer
guess a code.

To switch between human or computer player, change the `guess_producer`
at the bottom of `mastermind.cui`.

To install the dependencies with pipenv:

    pipenv sync

To run:

    pipenv run python -m mastermind.cui

To run the testsL

    pipenv run pytest
