import random
lista_caractere = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','ç','z','x','c','v','b','n','m','1','2','3','4','5','6','7','8','9','!','@','$','%','&','*','(',')']
#lista com os caracteres

caracteres_aleatorios = random.sample(lista_caractere, 10)
# Pega 10 caracteres aleatórios da lista

string_aleatoria = ''.join(caracteres_aleatorios)
#retiro as aspas da lista para transforma-lá em uma string

print(string_aleatoria)
# Exibe os caracteres aleatórios