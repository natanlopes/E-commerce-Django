import re  # Importa o módulo 're' para trabalhar com expressões regulares

def valida_cpf(cpf):
    cpf = str(cpf)  # Converte o CPF para string
    cpf = re.sub(r'[^0-9]', '', cpf)  # Remove caracteres não numéricos do CPF utilizando expressão regular

    if not cpf or len(cpf) != 11:  # Verifica se o CPF está vazio ou não tem 11 dígitos
        return False  # Retorna False indicando um CPF inválido

    novo_cpf = cpf[:-2]  # Obtém os 9 primeiros dígitos do CPF (exceto os dígitos verificadores)
    reverso = 10  # Inicializa o valor do peso/reverso

    total = 0  # Inicializa a variável de soma dos produtos

    for index in range(19):  # Loop de cálculo dos dígitos verificadores
        index -= 9  # Ajusta o índice para obter os próximos dígitos do CPF

        total += int(novo_cpf[index]) * reverso  # Multiplica o dígito pelo peso/reverso e soma ao total

        reverso -= 1  # Decrementa o valor do peso/reverso
        if reverso < 2:  # Verifica se o peso/reverso atingiu o valor mínimo
            reverso = 11  # Reinicia o valor do peso/reverso

            d = 11 - (total % 11)  # Calcula o dígito verificador

            if d > 9:  # Verifica se o dígito verificador é maior que 9
                d = 0  # Ajusta o dígito verificador para 0

            total = 0  # Reinicia a variável de soma dos produtos
            novo_cpf += str(d)  # Adiciona o dígito verificador ao novo CPF

    sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)  # Verifica se há uma sequência de dígitos repetidos

    if cpf == novo_cpf and not sequencia:  # Verifica se o CPF original é igual ao novo CPF e não há sequência
        return True  # Retorna True indicando um CPF válido
    else:
        return False  # Retorna False indicando um CPF inválido

