# Start in Room 1, treasure is in Room 5

currRoom = 1
print("Welcome to the Maze! Go find your treasure!\n")

while currRoom != 5:
    print("You are in Room", currRoom)

    if currRoom == 1:
        print("You can go East (E) to Room 2")
        move = input("Direction: ")
        if move == "E":
            currRoom = 2

    elif currRoom == 2:
        print("You can go West (W) to Room 1, East (E) to Room 3, South (S) to Room 4")
        move = input("Direction: ")
        if move == "W":
            currRoom = 1
        elif move == "E":
            currRoom = 3
        elif move == "S":
            currRoom = 4

    elif currRoom == 3:
        print("You can go West (W) to Room 2")
        move = input("Direction: ")
        if move == "W":
            currRoom = 2

    elif currRoom == 4:
        print("You can go North (N) to Room 2, East (E) to Room 5")
        move = input("Direction: ")
        if move == "N":
            currRoom = 2
        elif move == "E":
            currRoom = 5


print("\nCongratulations, you found the treasure!")
