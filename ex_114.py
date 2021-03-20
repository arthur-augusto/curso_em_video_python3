# Informa se o site google está disponível na máquina do usuário
import urllib.request
import urllib.error
try:
    site = urllib.request.urlopen('https://www.google.com')
except urllib.error.URLError:
    print('O site Google não está acessível no momento.')
else:
    print('Consegui acessar o site Google com sucesso!')
