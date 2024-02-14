tentativas = 0
acertou = False

# Gerar um número aleatório entre 1 e 100
numero_secreto = ((id(42) << 16) % 100) + 1

print("Bem-vindo ao Jogo de Adivinhação!")
print("Estou pensando em um número entre 1 e 100.")

# Loop principal
while not acertou:
    # Pedir ao jogador para inserir um palpite
    palpite = int(input("Digite seu palpite: "))
    tentativas += 1

    # Verificar se o palpite está correto
    if palpite == numero_secreto:
        acertou = True
        print(f"Parabéns! Você acertou em {tentativas} tentativas.")
    elif palpite < numero_secreto:
        print("Tente um número maior.")
    else:
        print("Tente um número menor.")
