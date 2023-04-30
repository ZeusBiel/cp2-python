#Gabriel Oliveira Rodrigues RM98565
#Leandro Ferreira de Morais RM99064
#Gabriel Riqueto Reis RM98685



primo = 1
valor = 1


def calcular(valor):  #função para calcular a aproximação de numero primo

    primo = valor * 2

    return primo



while(valor != 0): #menu

    valor = int(input("Digite um valor entre 1 e 1000 para iniciar, ou 0 para sair: "))

    if valor == 0: #encerrar programa quando valor = 0
        break

    elif valor < 1 or valor > 1000: #mensagem de erro e repetir "input" caso "valor" ser negativo ou maior que 1000
        print("Valor inválido.")
        continue

    else:   #executar a funçao de aproximação e mostrar mensagem
        primo = calcular(valor)
        print(f"Número primo mais próximo: {primo}")

print("Programa encerrado") #fim do programa
