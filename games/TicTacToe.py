''' This game is designed for terminal '''

print("The beginning of the program.")

MAX_COUNT = 9

def print_numpad():
    print("1 | 2 | 3")
    print("- - - - - ")
    print("4 | 5 | 6")
    print("- - - - - ")
    print("7 | 8 | 9")

def game_explanation():
    print("The following is the structure of board:")
    print_numpad()
    
board = {"1":" ", "2":" ", "3":" ", 
         "4":" ", "5":" ", "6":" ",
         "7":" ", "8":" ", "9":" "}
    
def print_board():
    print(board["1"] , "|" , board["2"] , "|" , board["3"])
    print("- - - - - ")
    print(board["4"] , "|" , board["5"] , "|" , board["6"])
    print("- - - - - ")
    print(board["7"] , "|" , board["8"] , "|" , board["9"])
    

player1 = ""
player2 = ""
current_player = ""

def choose_user():
    global player1, player2, current_player
    player1 = input("Choose user. X or O ?").upper()
    while(player1 not in ["X","O"]):
        print("Selected user is invalid. Should be X or O")
        player1 = input("Choose user. X or O ?")
    
    player2 = "O" if player1 == "X" else "X"
    current_player = player1
    print(f"Current player is {player1}")

count = 0
player_positions = {"X": [], "O": []}

def choose_position():
    global count
    position = input("Choose position: ")
    
    while(not position.isdigit() or int(position) not in range(1,10)):
        print("Selected position is invalid. Should be in range 1-9.")
        position = input("Choose position: ")
    
    while(position in player_positions[player1] or position in player_positions[player2]):
        print("Selected position is already taken. Choose different position.")
        position = input("Choose position: ")
    
    player_positions[current_player].append(position)
    board[position] = current_player
    print_board()
    count += 1 

all_winner_list = [['1','2','3'], ['4','5','6'],['7','8','9'],['1','4','7'],['2','5','8'],
            ['3','6','9'],['1','5','9'],['3','5','7']]

def check_positions():
    if count < 5: return False
    for winner_list in all_winner_list:
        if(set(winner_list).issubset(player_positions[current_player])): 
            return True
    
    return False

def change_current_player():
    global current_player
    current_player = player2 if current_player == player1 else player1
    
def game_on():
    global current_player
    if count == MAX_COUNT:
        current_player = "No One"
        return False
    
    choose_position()
    if not check_positions():
        change_current_player()
        return True

    return False

def start_game():
    game_explanation()
    choose_user()
    
    while game_on():
        print(f"Current player is {current_player}")
    
    print(f"Winner is {current_player}")

start_game()
    
