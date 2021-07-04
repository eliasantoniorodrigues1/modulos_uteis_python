from random import randint


def gera_cpf():
    numero = str(randint(100000000, 999999999))
    novo_cpf = numero
    reverso = 10
    total = 0
    for index in range(19):
        if index > 8:
            index -= 9
        total += int(novo_cpf[index]) * reverso
        reverso -= 1

        digito = 11 - (total % 11)
        if digito > 9:
            digito = 0

        if reverso < 2:
            reverso = 11
            total = 0
            novo_cpf += str(digito)
    # Validação para evitar repetições no CPF
    # sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)  # Fazer validação da sequência.
    return novo_cpf


if __name__ == '__main__':
    print(gera_cpf())
