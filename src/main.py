from player import Player
from dice import Dice
from random import choice


def main():
    print("Welcome to snake and ladder game")

    input("Press enter to start the game")

    player1 = Player()

    count = 0

    while player1.position < 100:
        options = ("NoPlay", "Ladder", "Snake")

        roll = Dice.roll()
        count += 1

        match choice(options):
            case "NoPlay":
                player1.position += 0
            case "Ladder":
                if player1.position + roll > 100:
                    continue
                player1.position += roll
            case "Snake":
                player1.position -= roll

        if player1.position < 0:
            player1.position = 0

        print(f"Count: {count} You rolled {roll} and moved to {player1.position}")

    print("You Won!")


if __name__ == "__main__":
    main()
