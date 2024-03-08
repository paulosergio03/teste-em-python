
#1) Observe o trecho de código abaixo:

INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

print(SOMA)

#Ao final do processamento, qual será o valor da variável SOMA?
                         #--------Explicação: -----------------

#Esse código executa um loop enquanto o valor de K for menor que o valor de INDICE (que é 13 neste caso). Dentro do loop,
#K é incrementado em 1 a cada iteração, e o valor de SOMA é atualizado para incluir o valor atual de K.
#Ao final do processamento, o valor da variável SOMA será a soma de todos os números de 1 a 13,
#que é 91. Portanto, o valor impresso será 91.