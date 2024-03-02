import time
# Variaveis para o login
while True:
    nome = input("digite o seu nome de usuario:")
    senha = input("digite a sua senha:")
    deseja_logar = input(str("Sua conta foi criada,deseja logar no sistema? : "))

    if deseja_logar == "sim":
        print("Parabéns você logou no sistema! Seja bem vindo: " + nome)
    else:
        print("Você não foi logado no sistema")
        time.sleep(1)
        logar_novamente = input(str("deseja logar novamente? (sim/não): "))

    if logar_novamente.lower() != "sim":
        break









