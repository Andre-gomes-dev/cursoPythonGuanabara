gols = []
jogadores = {}
acaoJogador = {}
nomeJogador = input("Nome do jogador: ")
partidasJog = int(input("Quantas partidas foram jogadas: "))

for partida in range(1, partidasJog+1):
   gol =  int(input(f"Quantos gols na partida {partida}? "))
   gols.append(gol) 
print(gols)
resposta = ""
while resposta not in ["S", "N"]:
    resposta =  input("Quer continuar? [S/N]: ").upper().strip()
    if resposta not in ["S", "N"]:
        print("D'igite apenas S ou N")
    elif resposta == "N":
        print("saindo")
        break   
    elif resposta == "S":
        print("continue")
        continue 
    
totalGols =  sum(gols)
jogadores = {"nome": nomeJogador, "gols": partidasJog, "total": "totalGols"}
print(jogadores.items())