import random
LETTER_POOL = list("A"*9 + "B"*2 + "C"*2 + "D"*4 + "E"*12 + "F"*2 + "G"*3 + "H"*2 + "I"*9 + "J"*1 + "K"*1 + "L"*4 + "M"*2 + "N"*6 + "O"*8 + "P"*2 + "Q"*1 + "R"*6 + "S"*4 + "T"*6 + "U"*4 + "V"*2 + "W"*2 + "X"*1 + "Y"*2 + "Z"*1)
SCORE_DICT = { 'a': 1, 
'b': 3, 
'c': 3, 
'd': 2, 
'e': 1, 
'f': 4, 
'g': 2,  
'h': 4, 
'i': 1, 
'j': 8, 
'k': 5, 
'l': 1, 
'm': 3, 
'n': 1, 
'o': 1, 
'p': 3, 
'q': 10, 
'r': 1, 
's': 1,
't': 1, 
'u': 1, 
'v': 4, 
'w': 4, 
'x': 8, 
'y': 4, 
'z': 10}

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
        lowercase_hand_letter = hand_letter.lower()
        if lowercase_hand_letter in hand_dict:
            hand_dict[lowercase_hand_letter] += 1
        else:
            hand_dict[lowercase_hand_letter] = 1

    #Checks validity of user's word letters against the counter dictionary
    for player_letter in players_letters_list:
        lowercase_player_letter = player_letter.lower()
        if lowercase_player_letter not in hand_dict:
            return False

        if hand_dict[lowercase_player_letter] == 0:
            return False
        else:
            hand_dict[lowercase_player_letter] -= 1
    #Assumes a valid word if the function does not return False
    return True

def score_word(word):    
    players_letters_list=list(word.lower())
    letter_count=len(players_letters_list)
    players_word_score = 0

    #Adds each letter's points to the word score 
    for player_letter in players_letters_list:
        players_word_score += SCORE_DICT[player_letter.lower()]
    
    #Adds 8 points to the word score if the word is 7 letters or longer
    if letter_count >= 7:
        players_word_score += 8
        
    return players_word_score

def get_highest_word_score(word_list):
    pass
    #Create an empty dictionary to add words and scores to later
    #Create an empty list for words with the max score
    #Create an empty list for letter counts of words with the max score
    
    #Create a for loop through the word_list
    #Create an empty variable for the max score
    #In the loop, use the score_word() function from wave 3 to save the current score to a variable
    #Also in the loop, add each word as the dictionary keys and add the score variable as the dictionary values
    #Also in the loop, use conditional to determine if the current score is higher than the previous
        #If it is, assign it to the max score variable
    #Also in the loop, use a conditional to 
        #(1) append all words that have a dictionary value equal to the max score to the list
        #and (2) append the letter count of all words that have a dictionary value equal to the max score to the list
    
    #Save the minimum letter count from the letter count list to a variable
    
    #Create another for loop through the enumerate object letter counts of words with the max score
    #In the loop, use a conditional to determine if the letter count is 10
        #If it is, return a tuple of (1) the word at the enumerate object index from the list of words with the max score and (2) the high score
    #Use another conditional to determine if the letter count is equal to the minimum letter count
        #If it is, return a tuple of (1) the word at the enumerate object index from the list of words with the max score and (2) the high score


