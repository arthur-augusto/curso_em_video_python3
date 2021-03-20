# Recebe o sexo de uma pessoa e caso informe uma opção inválida pede para informar o sexo novamente
sexo = str(input('Informe o seu sexo: [M/F] ')).strip().upper()[0]
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso!')
