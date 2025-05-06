def is_valid_code(code, clues):
    code_str = str(code).zfill(3)  # Ensure the code is a 3-digit string
    for clue_code, correct_digits, correct_positions in clues:
        clue_str = str(clue_code).zfill(3)
        correct_count = 0
        position_count = 0

        for i in range(3):
            if code_str[i] == clue_str[i]:
                position_count += 1
            elif code_str[i] in clue_str:
                correct_count += 1

        if position_count != correct_positions or correct_count != correct_digits:
            return False
    return True

def find_correct_code(clues):
    for code in range(1000):  # Iterate through all 3-digit combinations
        if is_valid_code(code, clues):
            return str(code).zfill(3)  # Return the correct code as a 3-digit string
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
}

# Solve and print the correct code for each puzzle
for puzzle_name, clues in puzzles.items():
    correct_code = find_correct_code(clues)
    print(f"The correct code for {puzzle_name} is: {correct_code}")