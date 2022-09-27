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
    #Create dictionary of score chart with the letters as the keys and the points as the value
    #Convert player's word to a list of letters
    #Calculate the number of letters in the player's word
    #Create an empty variable to add points to as the score is calculated
    #Create a for loop through the player's list of letters
    #In the loop, use the dictionary to determine the points for each letter and add the points to the word score
    #After the loop is complete and the word is scored with the dictionary, add additional 8 points if the length is longer than 7
    #Return the word score
    score_dict = { 'a': 1, 
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
    
    word_letters_list=list(word.lower())
    word_letter_count=len(word_letters_list)
    word_score = 0

    for letter in word_letters_list:
        word_score += score_dict[letter.lower()]
    
    if word_letter_count >= 7:
        word_score += 8
        
    return word_score

def get_highest_word_score(word_list):
    pass
    #Create an empty dictionary to add words and scores to later
    #Create an empty list for words with the highest score
    #Create an empty list for letter counts of words with the highest score
    
    #Create a for loop through the word_list
    #In the loop, add each word as the dictionary keys and use the score_word function to add each score as the dictionary values
    
    #Create another for loop through the dictionary values
    #In the loop, save the max score to a variable
    
    #Create another for loop through the word_list
    #In the loop, append all words that have a value equal to the highest score to the list
    #Also in the loop, append the letter count of all words that have a value equal to the highest score to the list
    
    #Save the minimum letter count from the letter count list to a variable
    
    #Create another for loop through the letter counts with the max score
    #In the loop, use a conditional to determine if the letter count is 10
    #If the letter count is 10, return a tuple of the word at the same index from the list of words with the highest score and the high score
    #Also in the loop, use a conditional to determine if the letter count is equal to the minimum letter count
    #If the letter count is equal to the minimum count, return a tuple of the word at the same index from the list of words with the highest score and the high score


