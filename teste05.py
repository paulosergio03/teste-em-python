# Função para inverter os caracteres de uma string
def inverter_string(string):
    inverted_string = ""
    for i in range(len(string) - 1, -1, -1):
        inverted_string += string[i]
    return inverted_string

# String a ser invertida
string_original = input("Digite uma string para inverter: ")

# Chamando a função para inverter a string
string_invertida = inverter_string(string_original)

# Imprimindo a string invertida
print("String invertida:", string_invertida)
