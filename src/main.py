from player import Player
from dice import Dice
from random import choice


def main():
    print("Welcome to snake and ladder game")

    input("Press enter to start the game")

    player1 = Player("Player 1")
    player2 = Player("Player 2")
    count = 0

    roll = 0

    player = choice((player1, player2))

    while player1.position < 100 and player2.position < 100:
        count += 1

        options = ("NoPlay", "Ladder", "Snake")

        roll = Dice.roll()

        print(
            f"Count: {count} Player: {player.name} rolled {roll} and is at {player.position}"
        )

        match choice(options):
            case "NoPlay":
                player = player2 if player == player1 else player1
            case "Ladder":
                if player.position + roll > 100:
                    continue
                player.position += roll
            case "Snake":
                player.position -= roll
                if player.position < 0:
                    player.position = 0

                player = player2 if player == player1 else player1

    print(f"Count: {count} Player: {player.name} and is at {player.position}")
    print(f"{player.name} won the game")


if __name__ == "__main__":
    main()
