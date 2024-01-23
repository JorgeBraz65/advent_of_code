from pathlib import Path

PATH = Path(__file__).resolve().parent / "input.txt"

with PATH.open("r") as file:
    entrada = file.readlines()

ribbon = 0


for linha in entrada:
    dimensoes_str = linha.split("x")
    dimensoes = sorted(list(map(int, dimensoes_str)))

    ribbon += 2*dimensoes[0] + 2*dimensoes[1] + dimensoes[0]*dimensoes[1]*dimensoes[2]

print("A quantidade de faixa nessessária é:", ribbon)
