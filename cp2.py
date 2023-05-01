#Gabriel Oliveira Rodrigues RM98565
#Leandro Ferreira de Morais RM99064
#Gabriel Riqueto Reis RM98685

#Definindo uma função que utiliza o método matemático para verificar e listar todos números primos dentro dos parametros
def crivo_eratostenes(n):
   
    primos = [True] * (n + 1)
    p = 2 #O menor número primo é 2 então usaremos ele para verificar quais são os outros usando o crivo  
    while (p * p <= n):
        if (primos[p] == True):
            for i in range(p * 2, n + 1, p):
                primos[i] = False
        p += 1
    return [p for p in range(2, n + 1) if primos[p]]

while True:
    num = int(input("Digite um número entre 1 e 1000 para encontrar o número primo mais próximo, ou 0 para encerrar o programa: "))

    if num == 0:  #Caso o usuário escolha o número 0 o programa é encerrado
        print("Programa encerrado.")
        break

    if num < 1 or num > 1000: #Caso o usuário escolha um número menor que 1 ou maior que 1000 a mensagem de erro é mostrada
        print("Número inválido. Por favor, tente novamente.")
        continue

    primos = crivo_eratostenes(num) #Chama a funçao para listar os números primos encontrados 
    menorDistancia = num #A menor distância até o momento é o número inserido portanto não tem um primo mais proximo ainda 
    primoMaisProximo = None

    for p in primos: #Este loop acontece em todos os numeros primos encontrados
        if abs(p - num) < menorDistancia: # Utlilizamos a função abs para medir a distância entre o menor primo atual e o número fornecido
            menorDistancia = abs(p - num) #Se a distância encontrada for menor do que (menorDistancia) o valor das variaveis (menorDistancia) e (primoMaisProximo) são atualizados
            primoMaisProximo = p
        elif abs(p - num) == menorDistancia and p < primoMaisProximo:
            primoMaisProximo = p #Se a menor distância entre o primo atual e o número fornecido for igual a (menorDistancia) mas se o primo atual for menor que (primoMaisProximo) o valor de (primoMaisProximo) é atualizado

    print(f"O número primo mais próximo de {num} é {primoMaisProximo}.")