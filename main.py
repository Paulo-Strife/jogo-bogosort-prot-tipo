import random

def esta_embaralhado(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr)-1))
# criando o bogosort

def bogosort(arr):
    tentativas = 0
    while not esta_embaralhado(arr):
        random.shuffle(arr)
        tentativas += 1
    return arr, tentativas

def jogar():
    saldo = 100
    objetivo = 200
    print('Bem vindo ao jogo do Bogosort!!!')
    print('Aqui você começa com um saldo inicial de R$100, faça sua aposta')
    
    while saldo > 0 and saldo < objetivo:
        print(f'Seu saldo atual é {saldo}')
        try:
            aposta = int(input('digite o valor da sua aposta: '))
        except ValueError:
            print('Valor inválido, coloque um valor inteiro como aposta!')
            continue
        if aposta < 0 or aposta > saldo:
            print('Aposta inválida!')
            continue

        lista = [random.randint(1, 9) for _ in range(5)]
        print(f'Lista Embaralhada {lista}')
        lista_ordenada, tentativas = bogosort(lista)
        print(f'A lista foi ordenada com {tentativas} tentativas: {lista_ordenada}')

        if tentativas <= aposta:
            saldo += aposta
            print(f'Você ganhou, R$ {aposta}')
        else:
            saldo -= aposta
            print(f'Você perdeu, R$ {aposta}')
    if saldo >= objetivo:
        print('Você venceu! parabéns!!!!')
    else:
        print('Você perdeu, tente outra vez!!!')

if __name__ == "__main__":
    jogar()
