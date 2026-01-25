# Copy here code of line function from previous exercise and use it in your solution
def line(triangle_number, triangle_string, square_number, square_string):
    tri_rows = 1
    
    while tri_rows < triangle_number + 1:
        print(triangle_string * tri_rows)
        tri_rows += 1
    
    squ_rows = 0
    while squ_rows < square_number:
        if square_number <= 0:
            break
        print(square_string * triangle_number)
        squ_rows += 1


def shape(triangle_number, triangle_rows, square_number, square_string):
    line(triangle_number, triangle_rows, square_number, square_string)
    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(3, ".", 0, ",")