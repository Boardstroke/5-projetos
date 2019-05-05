# # Regras:
# Uma celula ativa com 0 ou 1 vizinho morre 
# Uma celula ativa com 2 ou 3 vizinhos continua viva
# Uma celular ativa com mais de 3 morre
# Uma celula morta com exatamente três vizinhos se torna ativa



import numpy as np 
from copy import deepcopy
import os as os 
import time as time
#Grid quadrada com 50 pontos
N = 10
#Célula viva == 1
#Célula morta == 0

class Jogo():
    

    def __init__(self,N):
        self.grid = np.zeros([N,N])
    
    def estado_inicial(self,arr):
        # Jogador inicializa células vivas
        for j in range(0,len(arr)):
            self.grid[arr[j][0]][arr[j][1]] = 1

    def mostrar(self):
        for i in range(0,N):
            for j in range(0,N):
                if(self.grid[i][j] == 1):
                    print("▄", end =" "),
                elif(self.grid[i][j] == 0):
                    print("•", end=" ")
            
            print(" ")

    def verificar(self):
        a = self.ativar()
        b = self.destruir()
        self.grid =  a - b


    def ativar(self):
        t = deepcopy(self.grid)
       

        for i in range(0,N):
            for j in range(0,N):
                if(self.grid[i][j] == 0):
                    s = 0
                   
                    for k in range(i-1, i+2):
                        for l in range(j-1, j+2):
                            
                            if((k != 0) and (l != 0)):
                                s = s + self.grid[k%N][l%N]
                            elif((k == 0) and (l !=0 )):
                                s = s + self.grid[k][l%N]
                            elif((k != 0) and (l ==0 )):
                                s = s + self.grid[k%N][l]

                    if (s == 3):
                        t[i][j] = 1
                    
                        

        return t

    def destruir(self):
        t = deepcopy(self.grid)

        for i in range(0,N):
            for j in range(0,N):
            
               if(self.grid[i][j] == 1):
                    soma = 0

                    for k in range(i-1, i+2):
                        for l in range(j-1, j+2):
                            soma = soma + self.grid[k%N][l%N]
        
                    if((soma-1 <= 1) and (soma-1 >= 4)):
                        t[i][j] = -1
                    elif((soma -1 >=2) and (soma -1 <= 3)):
                        t[i][j] = 0
                    

        return t


    def jogar(self):
        
        while(True):
            os.system("clear")
            print("!----------------------------------------!")
            print("!-------------Jogo da vida---------------!")
            print("!----------------------------------------!")
            print("\n")
           
            self.mostrar()
            self.verificar()
            time.sleep(2)
            
            

    
if __name__ == "__main__":
    interface = Jogo(N)
    inicial = [[4,5],[5,6],[6,4],[6,5],[6,6]]
    # inicial = [[9,7],[9,8],[9,9]]
    # inicial = [[4,2],[5,3],[6,1],[6,2],[6,3]]            
    interface.estado_inicial(inicial)
    interface.jogar()
    
    
    

    #TODO:
        #Implementar mundo infinito
            # A artimetica modular pode não estar sendo usada corretamente
            # Existe um caso especifico [[4,5],[5,6],[6,4],[6,5],[6,6]] em que quando chega na ponta as celulas vivas se separam uma em cada diagonal
        #Tentar receber o estado inicial de uma maneira mais simples
        #Tentar escrever alguma unidades de teste 
    
    
