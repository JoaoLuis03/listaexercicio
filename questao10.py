import random

escolha_usuario = input("Escolha: Pedra, Papel ou Tesoura? ").lower()

opcoes = ["pedra", "papel", "tesoura"]
escolha_computador = random.choice(opcoes)

print("Computador escolheu:", escolha_computador)

if escolha_usuario == escolha_computador:
    print("Empate!")
elif (escolha_usuario == "pedra" and escolha_computador == "tesoura") or \
     (escolha_usuario == "papel" and escolha_computador == "pedra") or \
     (escolha_usuario == "tesoura" and escolha_computador == "papel"):
    print("Você venceu!")
else:
    print("O computador venceu!")