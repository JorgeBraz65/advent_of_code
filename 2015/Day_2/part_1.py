from pathlib import Path

PATH = Path(__file__).resolve().parent / "input.txt"

with PATH.open("r") as file:
    entrada = file.readlines()

area_total = 0


for linha in entrada:
    dimensoes = linha.split("x")
    length, width, height = map(int, dimensoes)
    lados = [length*width, width*height, height*length]

    area_total += 2*lados[0] + 2*lados[1] + 2*lados[2] + min(lados[0], lados[1], lados[2])

print("A área total necessária é:", area_total)
