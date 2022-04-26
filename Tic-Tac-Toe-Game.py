# Tic-Tac-Toe is a game in which two players seek in alternate turns to complete a row, a column,
# or a diagonal with either three x's or three o's drawn in the spaces of a grid of nine squares.

#Author: Tulio Banegas

def main(): 
    winner_bool = False
    players = 0
    find = True
    grid = ["1","2","3","4","5","6","7","8","9"]
    while(winner_bool==False):
        while(find == True):
            value = get_value(players)
            print_grid(grid)
            print()
            selected = int(input(f"\n{value}'s turn to choose a square (1-9): "))
            find = find_selected(selected,grid)
            if find == True:
                print("\nThe value of the selected square is not correct or is already occupied, try again! \n")
        grid[selected-1] = value
        winner = find_winner(grid)
        if winner != " ":
            if winner == "x":
                print(f'\nGood game player {winner}. Thanks for playing!')
                winner_bool = True
            else:
                print(f'\nGood game player {winner}. Thanks for playing!')
                winner_bool = True

        if winner_bool == False:
            draw = find_draw(grid)
            if draw == True:
                print(f'\nThe play ends in a draw, see you later!')
                winner_bool = True

        find = True
        if players == 0:
            players = 1
        else:
            players = 0
        

def print_grid(grid):
    print()
    for i in range(0,9):
        if i in (3,6):
            print("\n-+-+-")
        print(grid[i], end="|")

def get_value(players):
    if players == 0:
        value = "x"
    else:
        value = "o"
    return value

def find_selected(selected,grid):
    find = False
    if  selected < 1 or selected > 9:
        find = True
    elif grid[selected-1] == "x" or grid[selected-1] == "o":
        find = True
    return find

def find_winner(grid):
     if (grid[0] == grid[1] and grid[0] == grid[2]):
         winner =  grid[0]
     elif (grid[3] == grid[4] and grid[3] == grid[5]):
         winner =  grid[0] 
     elif (grid[6] == grid[7] and grid[6] == grid[8]):
         winner =  grid[0] 
     elif (grid[0] == grid[3] and grid[0] == grid[6]):
         winner =  grid[0] 
     elif (grid[1] == grid[4] and grid[1] == grid[7]):
         winner =  grid[0] 
     elif  (grid[2] == grid[5] and grid[2] == grid[8]):
         winner =  grid[0] 
     elif  (grid[0] == grid[4] and grid[0] == grid[8]):
         winner =  grid[0] 
     elif (grid[2] == grid[4] and grid[2] == grid[6]):
         winner =  grid[0]
     else:
         winner =  " "
     return winner 

def find_draw(grid):
    draw = True
    for i in grid:
        if i != "x" and i != "o":
            draw = False
    return draw
        

main()

