def create_tuple(x : int, y : int, z : int ):
    lists = [x,y,z]
    smallest = min(lists)
    largest = max(lists)
    sum = x + y + z
    

        
    tupled = (smallest,largest,sum)
    

    return tupled
    

if __name__ == "__main__":
    print(create_tuple(1, 4, 2))