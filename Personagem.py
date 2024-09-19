class Personagem():
    def __init__(self,nome,encontrouTecnico,vidas):
        self.nome = nome
        self.encontrouTecnico = encontrouTecnico
        self.vidas = vidas


    def procurarSuporteTecnico(self):

        while True:
            self.vidas -= 1
            print(f"Olá, {self.nome}! Em qual sala gostaria de procurar o suporte técnico?\n a) Lab 1\n b) Lab 2\n c) Lab 3\n d) Lab 4\n e) Lab 5")
            resposta = input("")
    
            if self.vidas == 0:
                print(f"GAMER OVER,{self.nome}, você usou todas suas vidas e morreu.")
                break
            elif resposta == "a" or resposta == "A":
                print(f"{self.nome}, você entrou no lab 1 e foi obrigado a assistir a aula de direito constitucional!") 
                print(f"{self.nome}, vc ainda tem {self.vidas} vida(s)")
                self.controuTecnico = False
                continue
            elif resposta == "b" or resposta == "B":
                print(f"{self.nome}, você encontrou no lab 2 e participou da confratenização da turma de psicologia!")
                print(f"{self.nome}, vc ainda tem {self.vidas} vida(s)")
                self.encontrouTecnico = False
                continue
            elif resposta == "c" or resposta == "C":
                print(f"{self.nome}, você entrou no Lab 3 e encontrou o técnico de suporte, agora você precisa convencê-lo a reiniciar o roteador!")
                self.encontrouTecnico = True
                break
            elif resposta == "d" or resposta == "D":
                print(f"{self.nome}, você entrou no Lab 4 caiu em um portal do tempo e voltou para 1897.")
                print(f"{self.nome}, vc ainda tem {self.vidas} vida(s)")
                self.encontrouTecnico = False
                continue
            elif resposta == "e" or resposta == "E":
                print(f"{self.nome}, você entrou no Lab 5 e ganhou 2 ingressos para o rock in rio. ")
                print(f"{self.nome}, vc ainda tem {self.vidas} vida(s)")
                self.encontrouTecnico = False
                continue
            else:
                print(f"Opção inválida,{self.nome}. Tente novamente.")


    def falarComTecnico(self):
        if self.encontrouTecnico == True:
            print("Como deseja convencer o técnico a reiniciar o roteador?\n a) Oferecer ingressos para o rock in rio\n b) Dar em cima dele\n c) Ameaçá-lo de morte")
            r = input("")
            
            if r == "a" or r == "A":
                print("GAME OVER!\nO técnico é crente, e não aceita os ingressos.")
            elif r == "b" or r == "B":
                print("GAMER OVER.\nO técnico se sente ofendido e te denuncia por assédio na direção da faculdade.")
            elif r == "c" or r == "C":
                print("Parabéns,o técnico ficou morrendo de medo de você e reiniciou o roteador!")
            else:
                print("opção inválida.")
        else:
            print("Você PERDEU!")
