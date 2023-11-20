import random
lista1 = ['pedra','papel','tesoura']
lista = ['1','2','3']
escolha_pc = random.choice(lista)
indice = lista.index(escolha_pc)
escolha = lista1[indice]
escolha_user = input("Vamos jogar? \nEscolha:\n1-Pedra 2-Papel 3-Tesoura\n")
if escolha_user == '1' and escolha_pc == '2':
    print(f"A máquina escolheu: {escolha}")
    print("Você perdeu!")
elif escolha_user == '2' and escolha_pc == '3':
    print(f"A máquina escolheu: {escolha}")
    print("Você perdeu!")
elif escolha_user == '3' and escolha_pc == '1':
    print(f"A máquina escolheu: {escolha}")
    print("Você perdeu!")
#usuário perde
elif escolha_user == '2' and escolha_pc == '1':
    print(f"A máquina escolheu: {escolha}")
    print("Você venceu!")
elif escolha_user == '3' and escolha_pc == '2':
    print(f"A máquina escolheu: {escolha}")
    print("Você venceu!")
elif escolha_user == '1' and escolha_pc == '3':
    print(f"A máquina escolheu: {escolha}")
    print("Você venceu!")
elif escolha_user == escolha_pc:
    print(f"A máquina escolheu: {escolha}")
    print("Empate")

#usuário vence