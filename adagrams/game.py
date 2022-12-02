import random
LETTER_POOL = list("A"*9 + "B"*2 + "C"*2 + "D"*4 + "E"*12 + "F"*2 + "G"*3 + "H"*2 + "I"*9 + "J"*1 + "K"*1 + "L"*4 + "M"*2 + "N"*6 + "O"*8 + "P"*2 + "Q"*1 + "R"*6 + "S"*4 + "T"*6 + "U"*4 + "V"*2 + "W"*2 + "X"*1 + "Y"*2 + "Z"*1)
SCORE_DICT = { 'A': 1, 
'B': 3, 
'C': 3, 
'D': 2, 
'E': 1, 
'F': 4, 
'G': 2,  
'H': 4, 
'I': 1, 
'J': 8, 
'K': 5, 
'L': 1, 
'M': 3, 
'N': 1, 
'O': 1, 
'P': 3, 
'Q': 10, 
'R': 1, 
'S': 1,
'T': 1, 
'U': 1, 
'V': 4, 
'W': 4, 
'X': 8, 
'Y': 4, 
'Z': 10}

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
    # hand = [letter.upper() for letter in letter_bank]
    hand_dict = {}

    #Generates a counter dictionary for letters in the hand
    for hand_letter in letter_bank:
        if hand_letter in hand_dict:
            hand_dict[hand_letter] += 1
        else:
            hand_dict[hand_letter] = 1

    #Checks validity of user's word letters against the counter dictionary
    # for player_letter in players_letters_list:
    for letter in word.upper():
        if letter not in hand_dict:
            return False

        if hand_dict[letter] == 0:
            return False
        else:
            hand_dict[letter] -= 1
    #Assumes a valid word if the function does not return False
    return True

def score_word(word):    
    players_word_score = 0

    #Adds each letter's points to the word score 
    for player_letter in word.upper():
        players_word_score += SCORE_DICT[player_letter]
    
    #Adds 8 points to the word score if the word is 7 letters or longer
    if len(word) > 6:
        players_word_score += 8
        
    return players_word_score

def get_highest_word_score(word_list):
    #assigns an initial max score
    max_score = 0
    
    for word in word_list:
        current_score = score_word(word)
        #returns early if a word uses all 10 letters, because there cannot
        #be a higher scoring word
        if len(word) == 10:
            return word, current_score

        # checks if current score is higher than the previously stored max score 
        # then assigns a new winner and max score if needed
        if current_score > max_score:
            max_score = current_score
            winner_word = word
        # checks if current score is the same as the max score and if the current 
        # word has less letters than the previous word then assigns a new winner 
        # if needed
        elif current_score == max_score and len(word) < len(winner_word):
            winner_word = word
    return winner_word, max_score