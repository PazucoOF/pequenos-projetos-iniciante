import time

# variaveis

ficar = True
app_name = input (str("Digite o nome do seu restaurante: "))
cardapio_cod = (str("Nome do produto - codigo - preço"))
cardapio = (str("Cachorro Quente - 100 - R$ 1,20\nBauru Simples   - 101 - R$ 1,30\nBauru com ovo   - 102 - R$ 1,50\nHambúrguer      - 103 - R$ 1,20\nCheeseburguer   - 104 - R$ 1,30\nRefrigerante    - 105 - R$ 1,00"))

# menu inicial

bem_vindo = input (str("Seja bem vindo! deseja entrar no app do restaurante " + app_name + "? (s/n): "))
if bem_vindo == "s":
    print("Carregando...")

    time.sleep(1)

    abrir_cardapio = input(str("Deseja abrir o cardapio? (s/n): "))
    if abrir_cardapio == ("s"):
     while ficar:
        print("-------------------------------")
        print(cardapio_cod)
        print(cardapio)
        print("-------------------------------")
        codigo_produtos = input("Porfavor digite os codigo do produto que você deseja: ")
        quantidade_produtos = int(input("Porfavor digite a quantidade: "))

# Calculo do resultado

        if codigo_produtos == ("100"):

                resultado = round(1.20 * quantidade_produtos,2)
                print("O valor da sua compra deu: " + "R$ " + str(resultado))

        if codigo_produtos == ("101"):

                resultado = round(1.30 * quantidade_produtos,2)
                print("O valor da sua compra deu: " + "R$ " + str(resultado))

        if codigo_produtos == ("102"):

                resultado = round(1.50 * quantidade_produtos,2)
                print("O valor da sua compra deu: " + "R$ " + str(resultado))

        if codigo_produtos == ("103"):

                resultado = round(1.20 * quantidade_produtos,2)
                print("O valor da sua compra deu: " + "R$ " + str(resultado))

        if codigo_produtos == ("104"):

                resultado = round(1.30 * quantidade_produtos,2)
                print("O valor da sua compra deu: " + "R$ " + str(resultado))

        if codigo_produtos ==("105"):

                resultado = round(1.00 * quantidade_produtos,2)
                print("O valor da sua compra deu: " + "R$ " + str(resultado))


        ficar = eval(input("Deseja fazer outra compra? (0 - não / 1 - sim)\n"))

        print("Muito obrigado pela compra!")



