#functionArea
def jogador(nome=None, gols=0):
    print(f"jogador(a) {nome} fez {gols}gol(s) no campeonato")

#main    
nomeJogador = input("Nome do jogador (pressione Enter para desconhecido): ")
numeroGols =  int(input("numero de gols: ")) 
if nomeJogador.strip() == "":
    nomeJogador =  "<jogador desconhecido>"
    jogador(nomeJogador ,numeroGols)
else:
    jogador(nomeJogador, numeroGols)