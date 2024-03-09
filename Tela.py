import sys
import time



def digitar_texto_lentamente(texto, velocidade=0.1):
    for caractere in texto:
        sys.stdout.write(caractere)
        sys.stdout.flush()
        time.sleep(velocidade)
    print()

print("Seja bem vindo, eu sou o pazuco!")
time.sleep(0.5)
print("deseja começar o jogo?")
resposta1 = str(input("(S/N)"))

if resposta1 == "s":
    texto = "Carregando..."
    digitar_texto_lentamente(texto, 0.05)

    nomeUsu = input("Qual vai ser o nome do seu personagem?:")
    time.sleep(0.5)
    print("-----------------------------------------")
    print("Seja bem vindo ao meu mundo " + nomeUsu + "!")
    time.sleep(0.5)

    print("Vou te explicar um pouco como funciona esse mundo " + nomeUsu)
    print("basicamente você esta no momento em um mundo medieval de marombas...")
    print("Boa sorte!")

    avancar = (0)

    while avancar != "":

        avancar = input("Aperte |ENTER| para avançar")


    if avancar == "":


        print("-----------------------------------------")

        textoAcordou = "Você acordou finalmente...."
        digitar_texto_lentamente(textoAcordou, 0.1)

        quebrawhile = 0

        while quebrawhile != 6:

            dialogo1 = int(input("Escolha as opções de fala.\n1: Onde eu estou??\n2: Quem é você??\n3: Porque eu estou pelado??\nResposta:"))

            if dialogo1 == 1:
                print("-----------------------------------------")
                print("Você esta em Maryland um distrito de Uberland")
                print("-----------------------------------------")

            if dialogo1 == 2:
                print("-----------------------------------------")
                print("Me chamo Lazaro levrone da silva, mas isso não importa agora!")
                print("-----------------------------------------")
                quebrawhile = 6
            if dialogo1 == 3:
                print("-----------------------------------------")
                print("Foi mal me empolguei... Tome ja suas roupas!")
                print("-----------------------------------------")

            time.sleep(2)


        dialogo2 = int(input("1: Oque esta acontecendo?\nResposta:"))

        if dialogo2 == 1:
            print("-----------------------------------------")
            print("Eu estava saindo da academia apos um treino\npesado de gluteos, enquanto andava pelas ruas de maryland\nencontrei você desmaiado no chão... Então te dei uma dose\nde pre treino e você acordou!")
            print("-----------------------------------------")

            time.sleep(2)

            print("Quando te vi logo percebi que você não era do reino...\nvocê é magro.. cade os seus musculos??")
            print("-----------------------------------------")
            print("me diga quanto de biceps você tem?")
            biceps = int(input("Resposta: "))

            if biceps < 40:
                print("-----------------------------------------")
                print("É... realmente você não é daqui mesmo.")

            if biceps >= 40:
                print("-----------------------------------------")
                print("Wow, ate que você não é tão magrinho assim!")

            print("-----------------------------------------")

            time.sleep(1)

            print("Bom... seja bem vindo a Uberland.")



















