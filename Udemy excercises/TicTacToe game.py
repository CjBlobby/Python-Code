def draw_board(values):
    print("\n\n\n")
    print(f"\t\t|{values[6]}|{values[7]}|{values[8]}|")
    print("\t\t_______")
    print(f"\t\t|{values[3]}|{values[4]}|{values[5]}|")
    print("\t\t_______")
    print(f"\t\t|{values[0]}|{values[1]}|{values[2]}|")
    print("\t\t\n\n\n\n")


def tilechoice(player, values):
    num = int(input(f"\tPlayer {player}, chose your tile:\t")) - 1

    if values[num] == " ":
        values[num] = player
    else:
        print("You can't do that, silly!")
        
    return values

def win_check(values):
    winCases = [[values[0], values[1], values[2]],
    [values[3], values[4], values[5]],
    [values[6], values[7], values[8]],
    [values[0], values[3], values[6]],
    [values[1], values[4], values[7]],
    [values[2], values[5], values[8]],
    [values[0], values[4], values[8]],
    [values[2], values[4], values[6]]]

    for case in winCases:
        if case[0] == case[1] == case[2] and case[0] != " ":
            return True

print("Welcome to tic, Tac, Toe!")

filledtiles = 0
playernum = -1
game = True
values  = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
draw_board(values)
players = {1:"O", -1:"X"}

while game:
    draw_board(tilechoice(players[playernum], values))
    
    if win_check(values):
        print(f"Congrats player {players[playernum]},"
              " you have won this game of amazing strategy!!!")
        game  = False
        
    for breliuh in values:
        if breliuh != " ":
            filledtiles += 1

    if filledtiles == 9:
        print("You have drawn!")
        values = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    
    filledtiles = 0
    playernum *= -1

    

    

    








    
