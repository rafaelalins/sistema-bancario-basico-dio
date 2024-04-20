#Projeto do Dio - Fundamentos do Python 
#Sistema bancário para sacar, depositar e ver extrato
def deposito(valor, saldo_atual):
    saldo_atual += valor
    return saldo_atual

def saque(valor, qtd, saldo_atual, lim_qtd, lim_saque):
    if valor > lim_saque:
        print(f'\033[91mO saque ultrapassa o limite de saque, tente um número menor que R${lim_saque}.\033[0m')
    elif valor > saldo_atual:
        print(f'\033[91mSaldo insuficiente, tente um número menor que R${saldo_atual:.2f}.\033[0m')
    elif qtd >= lim_qtd:
        print(f'\033[91mLimite de quantidade de saques ({lim_qtd}) excedido.\033[0m')
    else:
        saldo_atual -= valor
        qtd += 1
        print(f'\033[91mSaque de R${valor:.2f} realizado com sucesso! Seu novo saldo é R${saldo_atual:.2f}\033[0m')
    return saldo_atual, qtd

saldo = 0
extrato = ''
qtd_saques = 0
LIMITE_SAQUE = 500
LIMITE_QTD_SAQUE = 3

while True:
    print('''
    ---------------MENU----------------
        [0] Depósito
        [1] Saque
        [2] Extrato
        [3] Sair
    -----------------------------------
        ''')
    opcao = int(input('Digite sua opção: '))

    if opcao == 0:
        print('-----Depósito-----')
        valor_deposito = float(input('Valor do depósito: '))
        saldo = deposito(valor_deposito, saldo)
        extrato += f'\033[92mDepósito de R${valor_deposito:.2f}\033[0m\n'
        print(f'\033[92mDepósito de R${valor_deposito:.2f} feito com sucesso!\nNovo saldo: R${saldo:.2f}\033[0m')

    elif opcao == 1:
        print('----Saque----')
        if qtd_saques < LIMITE_QTD_SAQUE:
            valor_saque = float(input('Valor do saque: '))
            saldo, qtd_saques = saque(valor_saque, qtd_saques, saldo, LIMITE_QTD_SAQUE, LIMITE_SAQUE)
            extrato += f'\033[91mSaque de -R${valor_saque:.2f}\033[0m\n'
        else:
            print('\033[91mLimite de saques excedido.\033[0m')

    elif opcao == 2:
        print('----Extrato----')
        print(extrato)
        print(f'Saldo atual: R${saldo:.2f}')

    elif opcao == 3:
        print('Encerrando o programa...')
        break

    else:
        print('Opção inválida. Por favor, digite novamente.')

