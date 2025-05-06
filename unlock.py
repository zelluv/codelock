# This code solves the "Unlock" puzzle by checking all possible combinations of digits against the clues provided.

def is_valid_code(code, clues, code_length=3):
    code_str = str(code).zfill(code_length)  # Ensure the code is a string of the correct length
    for clue_code, correct_digits, correct_positions in clues:
        clue_str = str(clue_code).zfill(code_length)
        correct_count = 0
        position_count = 0

        for i in range(code_length):
            if code_str[i] == clue_str[i]:
                position_count += 1
            elif code_str[i] in clue_str:
                correct_count += 1

        if position_count != correct_positions or correct_count != correct_digits:
            return False
    return True

def find_correct_code(clues, code_length=3):
    for code in range(10**code_length):  # Iterate through all combinations for the given code length
        if is_valid_code(code, clues, code_length):
            return str(code).zfill(code_length)  # Return the correct code as a string of the correct length
    return None  # If no code is found

# Define all puzzles and their clues in a dictionary
puzzles = {
    "puzzle1": [
        (291, 0, 1),  # Clue 1: One digit is right and in its place
        (245, 1, 0),  # Clue 2: One digit is right and in the wrong place
        (463, 2, 0),  # Clue 3: Two digits are right but both in the wrong place
        (578, 0, 0),  # Clue 4: No digit is correct
        (569, 1, 0),  # Clue 5: One digit right but in the wrong place
    ],
    "puzzle2": [
        (682, 0, 1),  # Clue 1: One number is correct and well placed
        (614, 1, 0),  # Clue 2: One number is correct but wrong placed
        (206, 2, 0),  # Clue 3: Two numbers are correct but wrong placed
        (738, 0, 0),  # Clue 4: Nothing is correct
        (780, 1, 0),  # Clue 5: One number is correct but wrong placed
    ],
    "puzzle3": [
        (265, 0, 1),  # Clue 1: One number is correct and well placed
        (387, 0, 0),  # Clue 2: Nothing is correct
        (234, 1, 0),  # Clue 3: One number is correct but wrong placed
        (471, 2, 0),  # Clue 4: Two numbers are correct but wrong placed
    ],
    "puzzle4": [  # New 4-digit puzzle
        (8951, 2, 0),  # Clue 1: Two digits right but both are at wrong positions
        (2169, 1, 1),  # Clue 2: One digit right and in the right place, another right but wrong place
        (3694, 1, 1),  # Clue 3: One digit right and in the right place, another right but wrong place
        (4721, 1, 1),  # Clue 4: One digit right and in the right place, another right but wrong place
        (1237, 3, 0),  # Clue 5: Three digits are right but all are at wrong place
    ],
}

# Solve and print the correct code for each puzzle
for puzzle_name, clues in puzzles.items():
    # Deduce code_length from the first clue
    first_clue_code = clues[0][0]
    code_length = len(str(first_clue_code))  # Determine the length of the first clue's code
    correct_code = find_correct_code(clues, code_length)
    print(f"The correct code for {puzzle_name} is: {correct_code}")