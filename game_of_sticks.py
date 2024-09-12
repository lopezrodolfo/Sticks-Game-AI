"""
Module: game_of_sticks

Author: Rodolfo Lopez (rodolfolopez@sandiego.edu)
"""

import random


def initialize_hats(num_sticks):
    """
    Initializes the hats dictionary with the possible moves for each number of sticks.

    Parameters:
    num_sticks (type: int) - The initial number of sticks in the game.

    Returns:
    dict - A dictionary representing the hats, where keys are the number of sticks
           and values are lists of possible moves.
    """

    hats = {}
    hats[2] = [1]
    hats[3] = [1, 2]

    for i in range(4, num_sticks + 1):
        hats[i] = [1, 2, 3]

    return hats


def update_hats(hats, beside, ai_won):
    """
    Modifies the hats' contents depending on the outcome of the AI's victory and the balls located beside the hats.

    Parameters:
    hats (type: dict) - The dictionary of hats to update.
    beside (type: dict) - A dictionary of balls beside each hat.
    ai_won (type: bool) - Whether the AI won the game.

    Returns:
    None
    """

    for hat_num, ball_num in beside.items():
        if ai_won:
            hats[hat_num].append(ball_num)
            hats[hat_num].append(ball_num)

        elif ball_num not in hats[hat_num]:
            hats[hat_num].append(ball_num)


def write_hat_contents(hats, filename):
    """
    # Writes the hats' contents to a file in the specified format.

    Parameters:
    hats (type: dict) - The dictionary of hats to write.
    filename (type: str) - The name of the file to write to.

    Returns:
    None
    """

    with open(filename, "w", encoding="utf-8") as f:
        f.write("Hat Number: (1's, 2's, 3's)\n")

        for hat_num, hat_contents in hats.items():
            f.write(
                f"{hat_num}: ({hat_contents.count(1)}, {hat_contents.count(2)}, {hat_contents.count(3)})\n"
            )


def get_ai_selection(sticks_left, hats, beside):
    """
    Retrieves a selection made by the AI player.

    Parameters:
    sticks_left (type: int) - The number of sticks left in the game.
    hats (type: dict) - The dictionary of hats to choose from.
    beside (type: dict) - A dictionary to store the selected ball beside the hat.

    Returns:
    int - The number of sticks selected by the AI.
    """

    if sticks_left == 1:
        return 1

    hat_content = hats[sticks_left]
    selection = random.choice(hat_content)
    hats[sticks_left].remove(selection)
    beside[sticks_left] = selection
    return selection


def get_player_selection(player_number, sticks_left):
    """
    Retrieves a selection from a human player.

    Parameters:
    player_number (type: int) - The number of the current player.
    sticks_left (type: int) - The number of sticks left in the game.

    Returns:
    int - The number of sticks selected by the player.
    """

    num_sticks = 0
    max_sticks = min(3, sticks_left)
    while num_sticks not in range(1, max_sticks + 1):
        selection = input(
            f"Player {player_number}: How many sticks do you take? (1 - {max_sticks}) "
        )
        num_sticks = int(selection)

    return num_sticks


def pretrain_ai(init_num_sticks, num_rounds):
    """
    Trains an AI by engaging it in a predetermined number of rounds against another AI competitor.

    Parameters:
    init_num_sticks (type: int) - The initial number of sticks in each game.
    num_rounds (type: int) - The number of rounds to play for training.

    Returns:
    dict - The trained hats for the AI.
    """

    ai1_hats = initialize_hats(init_num_sticks)
    ai2_hats = initialize_hats(init_num_sticks)

    for _ in range(num_rounds):
        num_sticks = init_num_sticks
        ai1_besides = {}
        ai2_besides = {}
        turn = 1

        while num_sticks > 0:
            if turn % 2 == 1:
                num_sticks -= get_ai_selection(num_sticks, ai1_hats, ai1_besides)
            else:
                num_sticks -= get_ai_selection(num_sticks, ai2_hats, ai2_besides)

            turn += 1

        if turn % 2 == 0:
            update_hats(ai1_hats, ai1_besides, False)
            update_hats(ai2_hats, ai2_besides, True)

        else:
            update_hats(ai1_hats, ai1_besides, True)
            update_hats(ai2_hats, ai2_besides, False)

    return ai2_hats


def player_vs_ai(num_sticks, training_rounds):
    """
    Begins a human vs AI game.

    Parameters:
    num_sticks (type: int) - The initial number of sticks in the game.
    training_rounds (type: int) - The number of rounds to pre-train the AI.

    Returns:
    None
    """
    init_num_sticks = num_sticks

    hats = pretrain_ai(init_num_sticks, training_rounds)
    write_hat_contents(hats, "hat-contents.txt")

    play_again = True
    while play_again:
        num_sticks = init_num_sticks
        besides = {}
        turn = 1

        while num_sticks > 0:
            print(f"There are {num_sticks} on the board.")
            if turn % 2 == 1:
                num_sticks -= get_player_selection(1, num_sticks)
            else:
                ai_selection = get_ai_selection(num_sticks, hats, besides)
                print(f"AI selects: {ai_selection}")
                num_sticks -= ai_selection

            turn += 1

        if turn % 2 == 0:
            print("You lose.")
            update_hats(hats, besides, True)
        else:
            print("AI loses.")
            update_hats(hats, besides, False)

        response = input("Play another round? (yes/no) ")
        if response != "yes":
            play_again = False


def player_vs_player(num_sticks):
    """
    Begins a game between two human players.

    Parameters:
    num_sticks (type: int) - The initial number of sticks in the game.

    Returns:
    None
    """
    turn = 1
    while num_sticks > 0:
        print(f"Number of remaining sticks: {num_sticks}")
        if turn % 2 == 1:
            num_sticks -= get_player_selection(1, num_sticks)
        else:
            num_sticks -= get_player_selection(2, num_sticks)

        turn += 1

    if turn % 2 == 1:
        print("Player 1 Wins!")
    else:
        print("Player 2 Wins!")


def main():
    """
    The main function to run the Game of Sticks program.

    Parameters:
    None

    Returns:
    None
    """

    print("Welcome to the Game of Sticks!")

    init_num_sticks = int(
        input("How many sticks are there on the table initially (10-100)? ")
    )
    while init_num_sticks < 10 or init_num_sticks > 100:
        print("Please enter a number between 10 and 100")
        init_num_sticks = int(
            input("How many sticks are there on the table initially (10-100)? ")
        )

    print("Options:")
    print(" (1) Play against a friend")
    print(" (2) Play against the computer")
    print(" (3) Play against the trained computer")
    selection = int(input("What option do you choose? "))

    if selection == 1:
        player_vs_player(init_num_sticks)
    elif selection == 2:
        player_vs_ai(init_num_sticks, 0)
    elif selection == 3:
        player_vs_ai(init_num_sticks, 1000)


if __name__ == "__main__":
    main()
