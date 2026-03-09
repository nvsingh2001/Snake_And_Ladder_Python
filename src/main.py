from player import Player
from dice import Dice
from random import choice


def main():
    player1 = Player()

    options = ("NoPlay", "Ladder", "Snake")

    roll = Dice.roll()

    match choice(options):
        case "NoPlay":
            player1.position += 0
        case "Ladder":
            player1.position += roll
        case "Snake":
            player1.position -= roll


if __name__ == "__main__":
    main()
