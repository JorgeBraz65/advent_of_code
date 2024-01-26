from pathlib import Path

PATH = Path(__file__).resolve().parent / "input.txt"

def check_nice_string(input: str) -> bool:
    two_letters_set = set()

    has_two_letters = False
    has_between = False

    penultimate_letter = " "
    last_letter = " "

    for character in input:
        if character == penultimate_letter and character != last_letter:
            has_between = True

        if (last_letter + character) in two_letters_set and not (character == penultimate_letter and character == last_letter):
            has_two_letters = True

        two_letters_set.add(last_letter + character)

        penultimate_letter = last_letter
        last_letter = character

    if has_two_letters and has_between:
        return True

    else:
        return False

num_nice_str = 0

with PATH.open("r") as file:
    input = file.readlines()
    for line in input:
        if check_nice_string(line):
            num_nice_str += 1

print(f"The number of nice strings is: {num_nice_str}")
