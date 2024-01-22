from pathlib import Path

PATH = Path(__file__).resolve().parent / "part_1.txt"

with PATH.open("r") as file:
    entrada = file.read().strip()

andar = 0
position = 0

for caractere in entrada:
    if caractere == "(":
        andar += 1

    elif caractere == ")":
        andar -= 1

    position += 1

    if andar == -1:
        break

print("A posição do porão é:", position)
