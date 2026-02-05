# Write your solution here
def play_turn(game_board: list, x: int,y:int, piece: str):
    if (x < 3 and x >= 0) and (y < 3 and y >=0) and game_board[y][x] == "" :
        game_board[y][x] = piece
        return True
    return False

if __name__ == "__main__":
    game_board = [["", "", ""], ["O", "O", ""], ["", "", ""]]
    print(play_turn(game_board, 2, -1, "X"))
    print(game_board)
