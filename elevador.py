import time

atual = 0
destino = 0
maximo = 2
minimo = 0
Aberta = True

while True:
    print("Elevador no andar", atual)
    destino = int(input("Digite o andar que deseja ir (0, 1, 2) ou -1 para sair: "))


    if destino == -1:
        print("Porta abrindo..")
        time.sleep(2)
        print("A porta está aberta.")
        break

    elif destino < 0 or destino > 2:
        print("Andar inválido! Tente novamente.")

    else:

        while atual != destino:

            print("===============")
            print("Porta abrindo..")
            time.sleep(1)
            print("Porta aberta.")
            print('==========')
            print("Porta fechando..")
            time.sleep(1)
            print("Porta fechada.")


            if destino > atual:
                print('===============')
                print("Subindo...")
                time.sleep(3)
                atual = atual + 1

            elif destino < atual:
                print('===============')
                print("Descendo...") 
                time.sleep(3) 
                atual = atual - 1

            elif atual == destino:
                print("Porta abrindo..")
                time.sleep(1)
                print("A porta está aberta")    
            
            print("Chegamos ao andar:", atual)
            print('===============') 
