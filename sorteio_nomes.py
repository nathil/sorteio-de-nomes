import random

caminho = 'nome.txt'

def retorna_lista(caminho):
    nomes = []

    with open(caminho, 'r', encoding='utf-8') as arquivo:
        dados = arquivo.readlines()
    
    for dado in dados: 
        nomes.append(dado.strip())
    
    return nomes

print(retorna_lista(caminho))


def sorteio():
    nomes = retorna_lista(caminho)
    i_nome_sorteado = random.randint(0,len(nomes)-1)

    return nomes[i_nome_sorteado]

print(sorteio())