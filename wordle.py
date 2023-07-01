#generate word
#show board
#play game
    #chech board with player

from glob import glob
import random
from turtle import color

#taking all the words from all_words
with open('all_words.txt') as file:
    all_words = [line.strip().upper() for line in file]

#'words' is now a list from the word_list file
with open('word_list.txt') as file:
    words = [line.strip().upper() for line in file]

board = ["-", "-", "-", "-", "-"]
color_board = ['','','','','']

green = '\U0001F7E9'
yellow = "\U0001F7E1"
gray = '\U00002B1C'

print(green + yellow + gray)

game_still_on = True
tries, letter, yellow = 6, 0, 0
green_list, yellow_list = [], []

chosen_word = words[random.randint(0, 212)]
allias_chosen_word = []
allias_chosen_word += chosen_word

def showboard():

    print(f"|| {board[0]} || {board[1]} || {board[2]} || {board[3]} || {board[4]} ||")

def player_turn():

    global tries
    global letter
    global board

    if tries > 0:
        print(f"lives left: {tries}")
        while board[letter] == "-":        
            board = input("Make your 5 letter guess: ").upper()
            if len(board) >= 6 or len(board) <= 4:
                print("It needs to be a 5 letter word!")
                board = ["-", "-", "-", "-", "-"]
            elif board not in all_words:
                print("It needs to be a valid word!")
                board = ["-", "-", "-", "-", "-"]
            elif board in all_words:
                pass
        letter += 1
        greens()
        print(f"\n{green_list} <-- Green")
        yellows()
        print(f"{yellow_list} <-- Yellow\n")
        c_gray()
        print(f'{color_board[0]} {color_board[1]} {color_board[2]} {color_board[3]} {color_board[4]}')

def greens():

    global board
    global green_list
    global color_board

    if board[0] == chosen_word[0]:
        green_list += board[0]
        color_board[0] = green
        allias_chosen_word.remove(board[0])
        allias_chosen_word.append('-')
    elif board[0] != chosen_word[0]:
        green_list += "-"

    if board[1] == chosen_word[1]:
        green_list += board[1]
        color_board[1] = green
        allias_chosen_word.remove(board[1])
        allias_chosen_word.append('-')
    elif board[1] != chosen_word[1]:
        green_list += "-"

    if board[2] == chosen_word[2]:
        green_list += board[2]
        color_board[2] = green
        allias_chosen_word.remove(board[2])
        allias_chosen_word.append('-')
    elif board[2] != chosen_word[2]:
        green_list += "-"

    if board[3] == chosen_word[3]:
        green_list += board[3]
        color_board[3] = green
        allias_chosen_word.remove(board[3])
        allias_chosen_word.append('-')
    elif board[3] != chosen_word[3]:
        green_list += "-"

    if board[4] == chosen_word[4]:
        green_list += board[4]
        color_board[4] = green
        allias_chosen_word.remove(board[4])
        allias_chosen_word.append('-')
    elif board[4] != chosen_word[4]:
        green_list += "-"

    return green_list, color_board

def yellows():

    global yellow_list
    global color_board

    if board[0] in green_list[0]:
        pass

    elif board[0] == allias_chosen_word[0] or board[0] == allias_chosen_word[1] or board[0] == allias_chosen_word[2] or board[0] == allias_chosen_word[3] or board[0] == allias_chosen_word[4]:
        
        yellow_list += board[0]
        color_board[0] = yellow
        allias_chosen_word.remove(board[0])
        allias_chosen_word.append('-')
        

    if board[1] in green_list[1]:
        pass

    elif board[1] == allias_chosen_word[0] or board[0] == allias_chosen_word[1] or board[1] == allias_chosen_word[2] or board[1] == allias_chosen_word[3] or board[1] == allias_chosen_word[4]:
        
        yellow_list += board[1]
        color_board[1] = yellow
        allias_chosen_word.remove(board[1])
        allias_chosen_word.append('-')
        

    if board[2] in green_list[2]:
        pass

    elif board[2] == allias_chosen_word[0] or board[2] == allias_chosen_word[1] or board[2] == allias_chosen_word[2] or board[2] == allias_chosen_word[3] or board[2] == allias_chosen_word[4]:
        
        yellow_list += board[2]
        color_board[2] = yellow
        allias_chosen_word.remove(board[2])
        allias_chosen_word.append('-')
        
    
    if board[3] in green_list[3]:
        pass

    elif board[3] == allias_chosen_word[0] or board[3] == allias_chosen_word[1] or board[3] == allias_chosen_word[2] or board[3] == allias_chosen_word[3] or board[3] == allias_chosen_word[4]:
        
        yellow_list += board[3]
        color_board[3] = yellow
        allias_chosen_word.remove(board[3])
        allias_chosen_word.append('-')
        

    if board[4] in green_list[4]:
        pass

    elif board[4] == allias_chosen_word[0] or board[4] == allias_chosen_word[1] or board[4] == allias_chosen_word[2] or board[4] == allias_chosen_word[3] or board[4] == allias_chosen_word[4]:
        
        yellow_list += board[4]
        color_board[4] = yellow
        allias_chosen_word.remove(board[4])
        allias_chosen_word.append('-')
        
    
    return yellow_list

def c_gray():

    if color_board[0] == '':
        color_board[0] = gray
    if color_board[1] == '':
        color_board[1] = gray
    if color_board[2] == '':
        color_board[2] = gray
    if color_board[3] == '':
        color_board[3] = gray
    if color_board[4] == '':
        color_board[4] = gray
    


def win_loss():

    global game_still_on

    if board == chosen_word:
        print("You've got it!")
        print(f"{chosen_word} <--- Answer")
        game_still_on = False
    elif tries == 0:
        print("Game Over!\n")
        print(f"{chosen_word} <--- Answer")
        game_still_on = False
    
def reset():

    global tries
    global letter
    global yellow_list
    global green_list
    global board
    global allias_chosen_word
    global color_board

    tries -= 1
    
    letter = 0
    
    yellow_list, green_list = [], []
    
    board = ["-", "-", "-", "-", "-"]

    color_board = ['','','','','']
    
    allias_chosen_word.clear()
    allias_chosen_word += chosen_word

def play_game():

    showboard()
    
    while game_still_on:

#        if tries > 0:


        player_turn()

        win_loss()

        reset()

print(chosen_word)
play_game()