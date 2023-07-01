import random


words_file = open("words.txt","r")
words = words_file.readlines()
words = [s.strip() for s in words]

word = random.choice(words).strip()
# word = "stops"
print(word)

yellow = "\U0001F7E8"
green = '\U0001f7e9'
red = "\U0001F7E5"

def game(word,user_word):
    word_copy = [s for s in word]
    
    output = ''
    if user_word == word:
        output+= green*5
        print(" ".join(user_word))
        print(output)
        
        return True
    
    for j in range(len(user_word)):
        user_letter = user_word[j]

        same = False
        for i in range(len(word_copy)):
            main_letter = word_copy[i]
            if main_letter==user_letter:
                same = True
                if i == j:
                    output+= green

                    
                    word_copy[i] = "`"
                    break
                else:
                    if i == len(word)-1 and same:
                        output+=yellow
                        break
                    else:
                        continue
                
            if i == len(word)-1:
                if same:
                    output+=yellow
                else:
                    output+=red
                    


    print(" ".join(user_word))
    print(output)
    

turns = 0
print(green*10+yellow*10+"  WORDLE  "+red*10+yellow*10)
print()
print("-"*90)
print()

while turns <= 5:
    print(f"Lives left: {5-turns}")
    user_word = input("Please type a 5 letter word: ")

    if len(user_word) != 5:
        print("Word is not 5 letter long")
        continue
    elif user_word not in words:
        print("not in the list")
        continue
    if game(word.upper(),user_word.upper()):
        print("You win!")
        break
    else:
        turns += 1
    if turns == 5:
        print("You lost")