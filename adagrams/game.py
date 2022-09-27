def draw_letters():
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
    players_letters_list = list(word)
    hand_dict = {}

    for hand_letter in letter_bank:
        lowercase_local_letter = hand_letter.lower()
        if hand_letter in hand_dict:
            hand_dict[lowercase_local_letter] += 1
        else:
            hand_dict[lowercase_local_letter] = 1

    for letter in players_letters_list:
        lowercase_local_letter_2 = letter.lower()
        if lowercase_local_letter_2 not in hand_dict:
            return False
        if lowercase_local_letter_2 in hand_dict:
            if hand_dict[lowercase_local_letter_2] == 0:
                return False
            else:
                hand_dict[lowercase_local_letter_2] -= 1
            continue
    return True

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass