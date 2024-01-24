from pathlib import Path

PATH = Path(__file__).resolve().parent / "input.txt"

with PATH.open("r") as file:
    entrada = file.read().strip()

casas_entregues = 1

norte = 0
leste = 0

conjunto = { (norte, leste) }

for caractere in entrada:
    if caractere == "^":
        norte += 1

    elif caractere == "v":
        norte -= 1

    elif caractere == ">":
        leste += 1

    elif caractere == "<":
        leste -= 1

    if (norte, leste) not in conjunto:
        casas_entregues += 1
        conjunto.add( (norte, leste) )

print("O número de casas que receberam presentes é:", casas_entregues)
