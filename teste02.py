
#2) Dado a sequência de Fibonacci, 
#onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores 
#(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, 
#ele calcule a sequência 
#de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

def verifica_fibonacci(numero):
    fibonacci = [0, 1]
    while fibonacci[-1] < numero:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    if numero in fibonacci:
        return f"O número {numero} pertence à sequência de Fibonacci."
    else:
        return f"O número {numero} não pertence à sequência de Fibonacci."

numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
print(verifica_fibonacci(numero))

                      #<<<-----------Explicação: --------------->>

#Este programa solicita ao usuário que insira um número e, em seguida, verifica se esse número está na 
#sequência de Fibonacci. Se estiver, ele retorna uma mensagem indicando que o número pertence à sequência; 
#caso contrário, retorna uma mensagem indicando que não pertence.







