from random import randint

PLAYER1 = "Human"
PLAYER2 = "Bot"


def get_pencil_count():
    """Prompt user for the number of pencils and validate the input."""
    while True:
        string_input = input()

        if not string_input.isdigit():
            print("The number of pencils should be numeric")
            continue

        number = int(string_input)
        
        if number == 0:
            print("The number of pencils should be positive")
            continue
            
        return number


# Choose between player1 and player2
def get_player():
    """Prompt user to select the starting player and validate the choice."""
    while True:
        player_string = input()
        
        if player_string.strip() not in (PLAYER1, PLAYER2):
            print(f"Choose between '{PLAYER1}' and '{PLAYER2}'")
            continue
        
        return player_string


def take_turn(player, pencils_available):
    """Manage a player's turn and validate pencil count."""
    print(f"{player}\'s turn!")
    
    while True:
        if player == PLAYER1:
            pencils_taken = input()
            if pencils_taken not in ("1", "2", "3"):
                print("Possible values: '1', '2' or '3'")
                continue

            if int(pencils_taken) > pencils_available:
                print("Too many pencils were taken")
                continue
        else:
            # PLAYER2 is always the bot
            pencils_taken = calculate_move(pencils_available)
            print(pencils_taken)
            
        return pencils_available - int(pencils_taken)


def calculate_move(number_of_pencils):
    """Calculate the optimal move for the bot based on pencil count.

    If the bot is in a losing position (i.e., remaining pencils is a
    multiple of 4 plus 1), it takes a random number of pencils between 1 and 3.
    Otherwise, it follows a strategy to force the opponent into the losing position.
    """
    # If only 1 pencil is left, the bot should not try to take more than 1
    if number_of_pencils == 1:
        return 1

    if (number_of_pencils - 5) % 4 == 0:
        return randint(1, 3)
    if (number_of_pencils - 4) % 4 == 0:
        return 3
    if (number_of_pencils - 3) % 4 == 0:
        return 2
    if (number_of_pencils - 2) % 4 == 0:
        return 1


def take_turns(pencils_count):
    """Manage the game loop, alternating player turns and determining the winner."""
    print(f"Who will be the first ({PLAYER1}, {PLAYER2}):")
    player = get_player()
    
    while pencils_count > 0:
        print("|" * pencils_count)  # Display remaining pencils visually
        pencils_count = take_turn(player, pencils_count)  # Player takes a turn
        player = PLAYER2 if player == PLAYER1 else PLAYER1  # Switch players

    # Announce the winner (the player who avoids picking the last pencil wins)
    print(f"{player} won!")
    

def main():
    print("How many pencils would you like to use:")
    pencils_number = get_pencil_count()
    take_turns(pencils_number)


if __name__ == "__main__":
    main()
