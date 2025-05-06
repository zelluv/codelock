import random
from unlock import find_correct_code  # Import find_correct_code from unlock.py

def generate_clues(target_code, code_length=4, num_clues=5):
    target_str = str(target_code).zfill(code_length)
    clues = []

    while len(clues) < num_clues:
        # Generate a random code to compare with the target
        random_code = random.randint(0, 10**code_length - 1)
        random_str = str(random_code).zfill(code_length)

        # Calculate correct digits and positions
        correct_positions = sum(1 for i in range(code_length) if target_str[i] == random_str[i])
        correct_digits = sum(1 for digit in random_str if digit in target_str) - correct_positions

        # Add the clue if it's not a duplicate
        clue = (random_code, correct_digits, correct_positions)
        if clue not in clues:
            clues.append(clue)

        # Validate uniqueness after adding each clue
        solution = find_correct_code(clues, code_length)
        if solution != target_str:
            clues.pop()  # Remove the clue if it introduces ambiguity

    return clues

def validate_clues(clues, code_length=4):
    # Use the imported find_correct_code function to validate uniqueness
    solution = find_correct_code(clues, code_length)
    return solution

# Example usage
if __name__ == "__main__":
    target_code = 8951  # The unique code you want to generate clues for
    code_length = 4
    num_clues = 5

    # Generate clues
    clues = generate_clues(target_code, code_length, num_clues)
    print(f"Generated clues for target code {target_code}:")
    for clue in clues:
        print(clue)

    # Validate the clues
    solution = validate_clues(clues, code_length)
    print(f"Solution from generated clues: {solution}")