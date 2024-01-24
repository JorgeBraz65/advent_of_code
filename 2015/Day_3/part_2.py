from pathlib import Path

PATH = Path(__file__).resolve().parent / "input.txt"

with PATH.open("r") as file:
    entrada = file.read().strip()

casas_entregues = 1

coord_x_noel = 0
coord_y_noel = 0

coord_x_robo = 0
coord_y_robo = 0

conjunto = { (0, 0) }
papai_noel = True

for caractere in entrada:
    if caractere == "^":
        if papai_noel is True:
            coord_x_noel += 1
        else:
            coord_x_robo += 1

    elif caractere == "v":
        if papai_noel is True:
            coord_x_noel -= 1
        else:
            coord_x_robo -= 1

    elif caractere == ">":
        if papai_noel is True:
            coord_y_noel += 1
        else:
            coord_y_robo += 1

    elif caractere == "<":
        if papai_noel is True:
            coord_y_noel -= 1
        else:
            coord_y_robo -= 1

    if (coord_x_noel, coord_y_noel) not in conjunto:
        casas_entregues += 1
        conjunto.add( (coord_x_noel, coord_y_noel) )

    elif (coord_x_robo, coord_y_robo) not in conjunto:
        casas_entregues += 1
        conjunto.add( (coord_x_robo, coord_y_robo) )

    papai_noel = not papai_noel

print("O número de casas que receberam presentes é:", casas_entregues)
