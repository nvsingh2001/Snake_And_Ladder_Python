from player import Player
from dice import Dice
from random import choice


def main():
    print("Welcome to snake and ladder game")

    input("Press enter to start the game")

    player1 = Player()

    while player1.position < 100:
        if player1.position < 0:
            player1.position = 0

        options = ("NoPlay", "Ladder", "Snake")

        roll = Dice.roll()

        match choice(options):
            case "NoPlay":
                player1.position += 0
            case "Ladder":
                player1.position += roll
            case "Snake":
                player1.position -= roll

    print("You Won!")


if __name__ == "__main__":
    main()
