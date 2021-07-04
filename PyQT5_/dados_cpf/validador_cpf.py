import re


def valida_cpf(cpf):
    cpf = str(cpf)

    cpf = re.sub(r'[^0-9]', '', cpf)

    if not cpf or len(cpf) != 11:
        return False

    novo_cpf = cpf[:-2]
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
    sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)  # Fazer validação da sequência.
    if cpf == novo_cpf:
        return True
    else:
        return False
