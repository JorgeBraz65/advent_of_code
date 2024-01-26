from pathlib import Path

PATH = Path(__file__).resolve().parent / "input.txt"

def check_nice_string(input: str) -> bool:
    vowels = {"a", "e", "i", "o", "u"}
    bad_strings = {"ab", "cd", "pq", "xy"}

    num_vowels = 0
    last_letter = " "

    has_double_character = False
    has_bad_string = False

    for character in input:
        if character in vowels:
            num_vowels += 1

        if character == last_letter:
            has_double_character = True

        if last_letter + character in bad_strings:
            has_bad_string = True
            break

        last_letter = character

    if num_vowels > 2 and has_double_character is True and has_bad_string is False:
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
