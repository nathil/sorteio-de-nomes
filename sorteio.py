import random 

acertos = 0 
erros = 0
    

while erros < 6: 

    numero_sorteado = random.randint(1,6)
    valor_inserido = int(input('Insira o número:')) 

    if valor_inserido == numero_sorteado: 
        print('Você Acertou!\n')
        acertos += 1

    else: 
        print('Você Errou...\n')
        erros += 1
           
    if erros == 6: 
        print('Suas Chances Acabaram... Tente Novamente.\n\n')
        print(f'----- PLACAR -----\n\nAcertos     Erros\n   {acertos}          {erros}\n')