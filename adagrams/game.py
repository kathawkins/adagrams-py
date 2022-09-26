def draw_letters():
    # pass
# Import random module
# Create pool list of letter strings with 9 A's, 2 B's, 2 C's etc.
# Create an empty list that will hold the hand of 10 letter strings
# Start a for loop with a range length == 9
# In the for loop, use random.choice() method to generate a random letter from the pool list and save it to a variable
# Append the variable with the random letter to the hand list
# Return hand list when the loop is complete
    import random
    LETTER_POOL = ["A", "A", "A", "A", "A", "A", "A", "A", "A", "B", "B", "C","C", "D", "D", "D", "D", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "F", "F", "G", "G", "G", "H", "H", "I", "I", "I",  "I", "I", "I",  "I", "I", "I", "J", "K", "L", "L", "L", "L", "M", "M", "N", "N", "N", "N", "N", "N", "O", "O", "O", "O", "O", "O", "O", "O", "P", "P", "Q", "R", "R", "R", "R", "R", "R", "S", "S", "S", "S", "T", "T", "T", "T", "T", "T", "U", "U", "U", "U", "V", "V", "W", "W", "X", "Y", "Y", "Z"]
    adjusted_letter_pool=LETTER_POOL.copy()
    hand_list = []
    for letter in range(10):
        current_letter = random.choice(adjusted_letter_pool)
        adjusted_letter_pool.remove(current_letter)
        hand_list.append(current_letter)
    return hand_list

def uses_available_letters(word, letter_bank):
    pass
#Save letters from player's word to a list of letters
#Save letters from the letter bank to a dictionary that uses the letter as the key and the number of times it's in the letter bank as the value (i.e {A:2,B:8})
#Start a for loop through the player's letters
#In the for loop, use conditinal to determine if player letter is in the letter bank dictionary
#If the player letter is not in the dictionary, return False
#If the player letter is in the dictionary, reduce that letter's dictionary value by 1 and continue looping
#Return True if loop completes


def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass