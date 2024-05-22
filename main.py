import random
import requests
import json




Nome = ' Banco Tigger Brasil '
print(Nome.center(50, '-'))

usuario = input('Digite seu usuario:')
banco_caractrres = ['5497', '3211', '4951', '3894', '5492']
conta_corrente = random.choice(banco_caractrres)
print(f'Bem vindo - {usuario}, Sua conta corrente é: {conta_corrente}')

saldo = requests.get('https://327b4f43-7e96-48b8-94a6-ede5f3c16171-00-2tu5uqlejwbeg.kirk.replit.dev/saldo').json()

print('Escolha uma das opções abaixo:')
print('1 - Depositar')
print('2 - Sacar')
print('3 - Extrato')
print('4 - zerar saldo')
print(f'Saldo atual: {saldo["saldo"]}')

opcao = input('Digite o numero da opção:')

if opcao == '1':
    valor_deposito = input('Digite o valor a ser depositado:')
    url = "https://327b4f43-7e96-48b8-94a6-ede5f3c16171-00-2tu5uqlejwbeg.kirk.replit.dev/saldo"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "saldo": valor_deposito
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    print(response.status_code)
    print(response.json())



elif opcao == '2':
    valor_saque = input('Digite o valor para sacar:')
    valor_escolhido_saque = int(valor_saque)

    url = "https://327b4f43-7e96-48b8-94a6-ede5f3c16171-00-2tu5uqlejwbeg.kirk.replit.dev/saldo"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "saldo": int(saldo['saldo']) - valor_escolhido_saque
    }

    response = requests.put(url, headers=headers, data=json.dumps(data))

    print(response.status_code)
    print(response.json())

elif opcao == '3':
    print(f'Seu saldo atual é:{saldo}')

elif opcao == '4':

    url = "https://327b4f43-7e96-48b8-94a6-ede5f3c16171-00-2tu5uqlejwbeg.kirk.replit.dev/saldo"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "saldo": 0
    }

    response = requests.put(url, headers=headers, data=json.dumps(data))

    print(response.status_code)
    print(response.json())











