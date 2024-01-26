from hashlib import md5


def hash(input):
    return md5(input.encode()).hexdigest()

def calcular_menor_valor(input, total_leading_zeros):
    prefixo = '0' * total_leading_zeros
    sufixo = 1

    while not hash(input + str(sufixo)).startswith(prefixo):
        sufixo += 1

    return sufixo

# input = "abcdef"
# input = "pqrstuv"
input = "yzbqklnj"

# numero_zeros = 5
numero_zeros = 6

resultado = calcular_menor_valor(input, numero_zeros)
print(f"Resultado: {resultado}")
