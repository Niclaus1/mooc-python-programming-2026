# Write your solution here
def who_won(game_board : list):
    player_one = 0
    player_two = 0
    
    for row in range(len(game_board)):
        for col in range(len(game_board[row])):
            if game_board[row][col] == 1:
                player_one += 1
            elif game_board[row][col] == 2:
                player_two += 1
    
    if player_one > player_two:
        return 1
    elif player_one < player_two:
        return 2
    
    return 0

