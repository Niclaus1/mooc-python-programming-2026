# Write your solution here
def chessboard(count):
    step = 0
    while step < count:
        state = 0
        
        if step % 2 == 0:
            state = 1
        i = 0
        
        while i < count:
            print(state, end="")
            if state == 1:
                state = 0
            else:
                state = 1
            i += 1
        
        print()
        step += 1

# Testing the function
if __name__ == "__main__":
    chessboard(4)
