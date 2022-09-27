import random
LETTER_POOL = list("A"*9 + "B"*2 + "C"*2 + "D"*4 + "E"*12 + "F"*2 + "G"*3 + "H"*2 + "I"*9 + "J"*1 + "K"*1 + "L"*4 + "M"*2 + "N"*6 + "O"*8 + "P"*2 + "Q"*1 + "R"*6 + "S"*4 + "T"*6 + "U"*4 + "V"*2 + "W"*2 + "X"*1 + "Y"*2 + "Z"*1)

def draw_letters():
    adjusted_letter_pool=LETTER_POOL.copy()
    hand_list = []
    
    #Appends 10 random letters to the hand
    for _ in range(10):
        current_letter = random.choice(adjusted_letter_pool)
        adjusted_letter_pool.remove(current_letter)
        hand_list.append(current_letter)

    return hand_list

def uses_available_letters(word, letter_bank):
    players_letters_list = list(word)
    hand_dict = {}

    #Generates a counter dictionary for letters in the hand
    for hand_letter in letter_bank:
        lowercase_local_letter = hand_letter.lower()
        if hand_letter in hand_dict:
            hand_dict[lowercase_local_letter] += 1
        else:
            hand_dict[lowercase_local_letter] = 1

    #Checks validity of user's word letters against the counter dictionary
    for letter in players_letters_list:
        lowercase_local_letter_2 = letter.lower()
        if lowercase_local_letter_2 not in hand_dict:
            return False

        if hand_dict[lowercase_local_letter_2] == 0:
            return False
        else:
            hand_dict[lowercase_local_letter_2] -= 1
    #Assumes a valid word if the function does not return False
    return True

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass