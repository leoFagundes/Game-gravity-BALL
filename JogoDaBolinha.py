from graphics import *
import random

player = str()

#Criar a janela
win = GraphWin("Jogo da Bolinha - Os Melhores", 800, 600)
win.setBackground(color_rgb(163,255,189))

#INTEFACE INICIAL
#Retângulo Branco Superior
RBranco = Rectangle (Point(0, 0), Point(800, 40))
RBranco.setFill("White")
RBranco.setOutline("White")
RBranco.draw(win)

#Retângulo Branco Inferior
RBranco1 = Rectangle (Point(0, 550), Point(800, 600))
RBranco1.setFill("White")
RBranco1.setOutline("White")
RBranco1.draw(win)

#Título - Jogo da Bolinha
Tit=Text(Point(400, 18), "Jogo da Bolinha")
Tit.setSize(18)
Tit.draw(win)

#Bordas - As linhas pretas em volta
linhaSuperior = Line(Point(0, 40), Point(800, 40))
linhaSuperior.setWidth(6)
linhaSuperior.setFill("Black")
linhaSuperior.draw(win)

linhaInferior = Line(Point(0, 550), Point(800, 550))
linhaInferior.setWidth(6)
linhaInferior.setFill("Black")
linhaInferior.draw(win)

linhaEsquerda = Line(Point(2, 40), Point(2, 550))
linhaEsquerda.setWidth(6)
linhaEsquerda.setFill("Black")
linhaEsquerda.draw(win)

linhaDireita = Line(Point(798,40), Point(798, 550))
linhaDireita.setWidth(6)
linhaDireita.setFill("Black")
linhaDireita.draw(win)

#Borda preta em volta de onde escreve o nome
q = Rectangle(Point(300, 225), Point(500, 275))
q.setWidth(1)
q.setOutline("black")
q.draw(win)

#Texto - Digite seu nome:
Title = Text(Point(400, 210), "Digite o seu nome: ")
Title.setSize(15)
Title.draw(win)

#Vai salvar o que você escrever na variável "Nome"
Nome = Entry(Point(400,250), 15)
Nome.setFill("White")
Nome.setSize(15)
Nome.draw(win)

#Texto "Jogar" dentro do botão pressionável
Enviar = Text(Point(400,290), "Jogar")
Enviar.setSize(12)
Enviar.draw(win)

#Posição inicial da bola que se move na tela inicial
colunaExtra = 250
linhaExtra = 40

#Definindo "Extra"
Extra1 = Circle(Point(linhaExtra, colunaExtra), 20)

#Definindo as variáveis que vou usar para a animação da bolinha na interface inicial
verdadeMaster = True
verdade = True
verdade1 = False
verdade2 = False
verdade3 = False


#Botão Pressionável da tela inicial "Jogar"
#------------------------------------------------------------
def apagar(): #Função para apagar toda a tela inicial (Vai ser chamada mais para frente)
   q.undraw()
   Title.undraw()
   Nome.undraw()
   Enviar.undraw()
   Ret.undraw()
   RBranco.undraw()
   RBranco1.undraw()
   seta.undraw()

def buttons(): #Função para a área do botão pressionável (É a área que fica em volta do "Jogar")
   Ret = Rectangle(Point(375,280), Point(425, 300))
   Ret.setOutline("Black")
   Ret.draw(win)
   return Ret

def inside(point, rectangle):

   ie = rectangle.getP1()  # (lower left)
   sd = rectangle.getP2()  # (upper right)

   return ie.getX() < point.getX() < sd.getX() and ie.getY() < point.getY() < sd.getY()

Ret = buttons()

#Definindo "seta" e "clique"
seta = Line(Point(300, 340), Point(365, 300))
clique = Text (Point(225,350), "Clique aqui \npara começar o jogo")

#Movimento da bola na interface inicial + clique do botão pressionável
while verdadeMaster == True:

   while verdade == True: #Enquanto verdade for true o movimentod a bolinha nessa diagonal vai continuar
       if win.checkMouse() == None:
           verdade = True
       else:
           Extra1.undraw()
           #Seta apontado para o "Jogar"
           seta = Line(Point(300, 340), Point(365, 300))
           seta.setFill("Black")
           seta.setWidth(3)
           seta.setArrow("last")
           seta.draw(win)

           #Texto "Clique aqui para começar o jogo"
           clique = Text (Point(225,350), "Clique aqui \npara começar o jogo")
           clique.setSize(13)
           clique.draw(win)
           clique.setFace("courier")

           clickPoint = win.getMouse()

           if clickPoint is None: #Se o clique for fora do "Jogar" então continua o movimento da bolinha
               Nome.setText("")
           elif inside(clickPoint, Ret): #Se o clique for dentro do "Jogar" então ele salva o nome escrito e vai para a próxima interface
               print(Nome.getText())
               player = Nome.getText()
               apagar() #Apaga toda a interface inicial menos as bordas e o nome: "Jogo da bolinha"
               verdadeMaster = False
               verdade = False
               verdade1 = False
               verdade2 = False
               verdade3 = False
       seta.undraw()
       seta.undraw()  # Apagar seta
       clique.undraw()  # Apagar texto do "Clique aqui para começar o jogo"

       # Movimento da bolinha na PRIMEIRA diagonal
       Extra1.undraw()
       colunaExtra += 10
       linhaExtra += 10
       Extra1 = Circle(Point(linhaExtra, colunaExtra), 20)
       Extra1.setFill("Black")
       Extra1.setOutline("Black")
       Extra1.draw(win)
       time.sleep(0.1)
       if colunaExtra > 520:
           Extra1.undraw()
           win.setBackground(color_rgb(194,205,225))
           verdade = False
           if win.checkMouse() == None:
               verdade1 = True

       while verdade1 == True: #Enquanto verdade1 for true o movimento da bolinha nessa diagonal vai continuar
           if win.checkMouse() == None: #Se você NÃO clicou no mouse então o "else" abaixo é ignorado
               verdade1 = True
           else: #Se você CLICOU no mouse então o que está abaixo acontece
               Extra1.undraw()

               # Seta apontado para o "Jogar"
               seta = Line(Point(300, 340), Point(365, 300))
               seta.setFill("Black")
               seta.setWidth(3)
               seta.setArrow("last")
               seta.draw(win)

               # Texto "Clique aqui para começar o jogo"
               clique = Text(Point(225, 350), "Clique aqui \npara começar o jogo")
               clique.setSize(13)
               clique.draw(win)
               clique.setFace("courier")

               clickPoint = win.getMouse()

               if clickPoint is None: #Se o clique for fora do "Jogar" então continua o movimento da bolinha
                   Nome.setText("")
               elif inside(clickPoint, Ret): #Se o clique for dentro do "Jogar" então ele salva o nome escrito e vai para a próxima interface
                   print(Nome.getText())
                   player = Nome.getText()
                   apagar() #Apaga toda a interface inicial menos as bordas e o nome: "Jogo da bolinha"
                   verdadeMaster = False
                   verdade = False
                   verdade1 = False
                   verdade2 = False
                   verdade3 = False
           seta.undraw() #Apagar seta
           clique.undraw() #Apagar texto do "Clique aqui para começar o jogo"

           #Movimento da bolinha na SEGUNDA diagonal
           colunaExtra -= 8
           linhaExtra += 16
           Extra1.undraw()
           Extra1 = Circle(Point(linhaExtra, colunaExtra), 20)
           Extra1.setFill("Black")
           Extra1.setOutline("Black")
           Extra1.draw(win)
           time.sleep(0.1)
           if linhaExtra > 768:
               Extra1.undraw()
               win.setBackground(color_rgb(127,255,238))
               verdade1 = False
               if win.checkMouse() == None:
                   verdade2 = True

           while verdade2 == True: #Enquanto verdade2 for true o movimentod a bolinha nessa diagonal vai continuar
               if win.checkMouse() == None:
                   verdade2 = True
               else:
                   Extra1.undraw()
                   # Seta apontado para o "Jogar"
                   seta = Line(Point(300, 340), Point(365, 300))
                   seta.setFill("Black")
                   seta.setWidth(3)
                   seta.setArrow("last")
                   seta.draw(win)

                   # Texto "Clique aqui para começar o jogo"
                   clique = Text(Point(225, 350), "Clique aqui \npara começar o jogo")
                   clique.setSize(13)
                   clique.draw(win)
                   clique.setFace("courier")

                   clickPoint = win.getMouse()

                   if clickPoint is None: #Se o clique for fora do "Jogar" então continua o movimento da bolinha
                       Nome.setText("")
                   elif inside(clickPoint, Ret): #Se o clique for dentro do "Jogar" então ele salva o nome escrito e vai para a próxima interface
                       print(Nome.getText())
                       player = Nome.getText()
                       apagar() #Apaga toda a interface inicial menos as bordas e o nome: "Jogo da bolinha"
                       verdadeMaster = False
                       verdade = False
                       verdade1 = False
                       verdade2 = False
                       verdade3 = False
               seta.undraw()  # Apagar seta
               clique.undraw()  # Apagar texto do "Clique aqui para começar o jogo"

               # Movimento da bolinha na TERCEIRA diagonal
               colunaExtra -= 10
               linhaExtra -= 16
               Extra1.undraw()
               Extra1 = Circle(Point(linhaExtra, colunaExtra), 20)
               Extra1.setFill("Black")
               Extra1.setOutline("Black")
               Extra1.draw(win)
               time.sleep(0.1)
               if colunaExtra < 68:
                   Extra1.undraw()
                   win.setBackground(color_rgb(205,255,82))
                   verdade2 = False
                   if win.checkMouse() == None:
                       verdade3 = True


               while verdade3 == True: #Enquanto verdade3 for true o movimentod a bolinha nessa diagonal vai continuar
                   if win.checkMouse() == None:
                       verdade3 = True
                   else:
                       Extra1.undraw()

                       # Seta apontado para o "Jogar"
                       seta = Line(Point(300, 340), Point(365, 300))
                       seta.setFill("Black")
                       seta.setWidth(3)
                       seta.setArrow("last")
                       seta.draw(win)

                       # Texto "Clique aqui para começar o jogo"
                       clique = Text(Point(225, 350), "Clique aqui \npara começar o jogo")
                       clique.setSize(13)
                       clique.draw(win)
                       clique.setFace("courier")

                       clickPoint = win.getMouse()

                       if clickPoint is None: #Se o clique for fora do "Jogar" então continua o movimento da bolinha
                           Nome.setText("")
                       elif inside(clickPoint, Ret): #Se o clique for dentro do "Jogar" então ele salva o nome escrito e vai para a próxima interface
                           print(Nome.getText())
                           player = Nome.getText()
                           apagar() #Apaga toda a interface inicial menos as bordas e o nome: "Jogo da bolinha"
                           verdadeMaster = False
                           verdade = False
                           verdade1 = False
                           verdade2 = False
                           verdade3 = False
                   seta.undraw()  # Apagar seta
                   clique.undraw()  # Apagar texto do "Clique aqui para começar o jogo"

                   # Movimento da bolinha na QUARTA diagonal
                   colunaExtra += 10
                   linhaExtra -= 16
                   Extra1.undraw()
                   Extra1 = Circle(Point(linhaExtra, colunaExtra), 20)
                   Extra1.setFill("Black")
                   Extra1.setOutline("Black")
                   Extra1.draw(win)
                   time.sleep(0.1)
                   if linhaExtra < 30:
                       Extra1.undraw()
                       win.setBackground(color_rgb(163,255,189))
                       verdade3 = False
                       if win.checkMouse() == None:
                           verdade = True

Extra1.undraw() #Apaga a bolinha depois de clicar em "Jogar"
#------------------------------------------------------------

#INTERFACE DA DIFICULDADE v v v v

win.setBackground(color_rgb(194,205,225)) #Define o fundo da janela para a cor mencionada

#Pegando o nome escrito na primeira interface e colocando no canto inferior direito + o texto " está jogando..."
if player.strip() == "": #Se não escrever nada então o nome vira Anônimo
   player = "Anônimo"
   ply = Text(Point(680, 585), player + " está jogando...")
   ply.setSize(12)
   ply.draw(win)
   ply.setFace("courier")
else:
   ply=Text(Point(680, 585), player + " está jogando...")
   ply.setSize(12)
   ply.draw(win)
   ply.setFace("courier")

#Retangulo de fundo verde
fundoDif = Rectangle (Point(3, 42), Point(266, 548))
fundoDif.setFill(color_rgb(0, 255, 33))
fundoDif.draw(win)

#Retângulo de fundo vermelho
fundoDif2 = Rectangle (Point(533, 42), Point(796, 548))
fundoDif2.setFill("Red")
fundoDif2.draw(win)

#Retângulo de fundo azul
fundoDif1 = Rectangle (Point(266, 42), Point(548, 548))
fundoDif1.setFill(color_rgb(0, 148, 255))
fundoDif1.draw(win)

#Linha preta onde ficará por baixo dos nomes: "Moleza", "Aceitável" e "Impossível"
linhaPreta = Line (Point(0, 460), Point(800, 460))
linhaPreta.setFill("Black")
linhaPreta.setWidth(50)
linhaPreta.draw(win)

#Linha cinza entre oos retângulos verde e azul
linhaDif = Line (Point(266, 42), Point(266, 548))
linhaDif.setFill(color_rgb(110,110,110))
linhaDif.setWidth(5)
linhaDif.draw(win)

#Linha cinza entre oos retângulos azul e vermelho
linhaDif1 = Line (Point(548, 42), Point(548, 548))
linhaDif1.setFill(color_rgb(110,110,110))
linhaDif1.setWidth(5)
linhaDif1.draw(win)

#Abaixo tem os 3 textos da dificuldade: "Moleza", "Aceitável" e "Impossível"
TextoDif1 = Text (Point(133,460), "MOLEZA")
TextoDif1.setFill("White")
TextoDif1.setSize(25)
TextoDif1.draw(win)
TextoDif1.setFace("courier")

TextoDif2 = Text (Point(405,460), "ACEITÁVEL")
TextoDif2.setFill("White")
TextoDif2.setSize(25)
TextoDif2.draw(win)
TextoDif2.setFace("courier")

TextoDif3 = Text (Point(675,460), "IMPOSSÍVEL")
TextoDif3.setFill("White")
TextoDif3.setSize(25)
TextoDif3.draw(win)
TextoDif3.setFace("courier")

#Os 3 Botões Pressionáveis na interface da Dificuldade
#------------------------------------------------------------

#Essas duas variáveis é o que vai definir a dificuldade (Passo)
Di0 = 2
Di = 10

#Função para apagar tudo da interface da dificuldade (Vai ser chamada mais para frente)
def apagar():
   Dif1.undraw()
   Dif2.undraw()
   Dif3.undraw()
   TextoDif1.undraw()
   TextoDif2.undraw()
   TextoDif3.undraw()
   fundoDif.undraw()
   fundoDif1.undraw()
   fundoDif2.undraw()
   linhaPreta.undraw()
   linhaDif.undraw()
   linhaDif1.undraw()
   TextoJogar.undraw()
   TextoJogar1.undraw()
   TextoJogar2.undraw()

#Função dos 3 botões que vai ser chamada mais para frente
def buttons():
   Dif1 = Circle(Point(133, 225), 65) #Botão Dificuldade Fácil
   Dif1.setOutline("Black")
   Dif1.setFill("Black")
   Dif1.draw(win)

   Dif2 = Circle(Point(405, 225), 65) #Botão Dificuldade Média
   Dif2.setOutline("Black")
   Dif2.setFill(("Black"))
   Dif2.draw(win)

   Dif3 = Circle(Point(675, 225), 65) #Botão Dificuldade Impossível
   Dif3.setOutline("Black")
   Dif3.setFill("Black")
   Dif3.draw(win)

   return Dif1, Dif2, Dif3

def inside(point, rectangle):

   ie = rectangle.getP1()  # (lower left)
   sd = rectangle.getP2()  # (upper right)

   return ie.getX() < point.getX() < sd.getX() and ie.getY() < point.getY() < sd.getY()

Dif1, Dif2, Dif3 = buttons()

#Abaixo tem os 3 textos "Jogar" dentro dos botões pressionáveis (Inicialmente na cor branca)
TextoJogar = Text(Point(133, 225), "JOGAR")
TextoJogar.setSize(22)
TextoJogar.setFill("White")
TextoJogar.draw(win)
TextoJogar.setFace("arial")

TextoJogar1 = Text(Point(405, 225), "JOGAR")
TextoJogar1.setSize(22)
TextoJogar1.setFill("White")
TextoJogar1.draw(win)
TextoJogar1.setFace("arial")

TextoJogar2 = Text(Point(675, 225), "JOGAR")
TextoJogar2.setSize(22)
TextoJogar2.setFill("White")
TextoJogar2.draw(win)
TextoJogar2.setFace("arial")

#Ativando os botões pressionáveis ao clique
while True:
   clickPoint = win.getMouse()

   if clickPoint is None: #Se clicar fora dos botões nada acontece
       Nome.setText("")
   elif inside(clickPoint, Dif1): #BOTÃO DA DIFICULDADE "MOLEZA"
       print (Nome.getText())
       Di0 = 2
       Di = 7 #Dificuldade Fácil

       #Apagando o texto "Jogar" e o "MOLEZA" e reescrevendo eles de verde
       TextoJogar.undraw()
       TextoJogar = Text(Point(133, 225), "JOGAR")
       TextoJogar.setSize(22)
       TextoJogar.setFill("Green")
       TextoJogar.draw(win)
       TextoJogar.setFace("arial")

       TextoDif1.undraw()
       TextoDif1 = Text(Point(133, 460), "MOLEZA")
       TextoDif1.setFill("Green")
       TextoDif1.setSize(25)
       TextoDif1.draw(win)
       TextoDif1.setFace("courier")

       time.sleep(0.5) #Tempo para que posso ver os Textos acima virando verde
       apagar() #Apagando toda a interface da dificuldade menos as bordas e o texto "Jogo da Bolina"
       break
   elif inside(clickPoint, Dif2): #BOTÃO DA DIFICULDADE "ACEITÁVEL"
       print (Nome.getText())
       Di0 = 9
       Di = 15 #Dificuldade Médio

       # Apagando o texto "Jogar" e o "ACEITÁVEL" e reescrevendo eles de verde
       TextoJogar1.undraw()
       TextoJogar1 = Text(Point(405, 225), "JOGAR")
       TextoJogar1.setSize(22)
       TextoJogar1.setFill("Green")
       TextoJogar1.draw(win)
       TextoJogar1.setFace("arial")

       TextoDif2.undraw()
       TextoDif2 = Text(Point(405, 460), "ACEITÁVEL")
       TextoDif2.setFill("Green")
       TextoDif2.setSize(25)
       TextoDif2.draw(win)
       TextoDif2.setFace("courier")

       time.sleep(0.5) #Tempo para que posso ver os Textos acima virando verde
       apagar() #Apagando toda a interface da dificuldade menos as bordas e o texto "Jogo da Bolina"
       break
   elif inside(clickPoint, Dif3): #BOTÃO DA DIFICULDADE "IMPOSSÍVEL"
       print(Nome.getText())
       Di0 = 20
       Di = 40 #Dificuldade Impossível

       # Apagando o texto "Jogar" e o "IMPOSSÍVEL" e reescrevendo eles de verde
       TextoJogar2.undraw()
       TextoJogar2 = Text(Point(675, 225), "JOGAR")
       TextoJogar2.setSize(22)
       TextoJogar2.setFill("Green")
       TextoJogar2.draw(win)
       TextoJogar2.setFace("arial")

       TextoDif3.undraw()
       TextoDif3 = Text(Point(675, 460), "IMPOSSÍVEL")
       TextoDif3.setFill("Green")
       TextoDif3.setSize(25)
       TextoDif3.draw(win)
       TextoDif3.setFace("courier")

       time.sleep(0.5) #Tempo para que posso ver os Textos acima virando verde
       apagar() #Apagando toda a interface da dificuldade menos as bordas e o texto "Jogo da Bolina"
       break
#------------------------------------------------------------
#INTERFACE DO JOGO

#Retângulo que está sendo usado para deixar o fundo do jogo na cor azul clarinho
fundoDif1 = Rectangle (Point(4, 42), Point(795, 548))
fundoDif1.setFill(color_rgb(206, 255, 252))
fundoDif1.draw(win)

#Posição Inicial do Circulo
col = 390
lin = 80
raio = 15
circulo=Circle(Point(col, lin), raio)
circulo.setFill("Black")
circulo.draw(win)

#Quantidade de Pontos
pts = 0
pontos=Text(Point(55, 575), "Pontos: " + str(pts))
pontos.setSize(15)
pontos.draw(win)

#Quantidade de Vidas
vidas = 3
life=Text(Point(195, 575), "Vidas: " + str(vidas))
life.setSize(15)
life.draw(win)

#Barra Controlável
corBarra = "Green"
colIni = 340
tamanho = 135
barra=Line(Point(colIni, 530), Point(colIni+tamanho, 530))
barra.setFill(corBarra)
barra.setWidth(10)
barra.draw(win)

#Velocidade da Bolinha
velocidade = 5

continuar = True
bateu = True
drt = 675
varPasso = 0.5

#Texto: Clique para Iniciar
Iniciar = Text(Point(400, 300), "Clique para iniciar")
Iniciar.setSize(23)
Iniciar.draw(win)
Iniciar.setFace("courier")

win.getMouse() #Esperar clicar antes de começar o jogo
Iniciar.undraw()
#----------------------------While--------------------------------------#
#Movimento da bolinha durante o jogo
while continuar:

 if bateu:
     passo = random.randrange(Di0, Di) #A dificuldade que foi definida anteriormente
     if random.random() < varPasso:
         passo = -passo
     bateu = False

#Quando bate nas linhas descritas abaixo a bolinha vai ser rebatida:
   #Linha Direita
 if (col + raio + passo) > 798:
     passo = -passo

   #Linha Esquerda
 if (col - raio + passo) < 2:
     passo = -passo

   #Linha Cima
 if lin < 60:
     velocidade = -velocidade

   #Linha Baixo (Barra controlável)
 if lin == 515 and col > colIni and col < (colIni+tamanho):
     velocidade = -velocidade

     pts += 1 #Se bater na barra controlável ganha 1 ponto
     pontos.undraw()
     pontos = Text(Point(55, 575), "Pontos: " + str(pts))
     pontos.setSize(15)
     pontos.draw(win)

   #Caso a Bolinha Caia
 if lin == 550:
   life.undraw()
   vidas -= 1 #Se a bolinha cair perde uma vida
   life = Text(Point(195, 575), "Vidas: " + str(vidas))
   life.setSize(15)
   life.draw(win)
   win.setBackground("Red")
   Continue = Text(Point(400, 300), "Clique para continuar...")
   Continue.setSize(22)
   Continue.draw(win)
   Continue.setFace("courier")

   #Caso as Vidas cheguem a 0
   if vidas == 0:
       fundoDif1.undraw()
       Continue.undraw()
       perdeu = Text(Point(400, 300), "VOCÊ PERDEU")
       perdeu.setSize(35)
       perdeu.draw(win)

       #Espera você clicar para mudar para a próxima interface
       win.getMouse()

       #INTERFACE DA TABELA FINAL!!!!!!!!!!!!!!!!!!!!!!!!!!
       #Apagando toda a interface do jogo
       win.setBackground(color_rgb(192, 192, 192))
       perdeu.undraw()
       circulo.undraw()
       barra.undraw()
       pontos.undraw()
       life.undraw()
       ply.undraw()
       Tit.undraw()
       linhaInferior.undraw()
       linhaSuperior.undraw()
       linhaEsquerda.undraw()
       linhaDireita.undraw()

       #Titulo: Pontuação
       Tit = Text(Point(400, 30), "Pontuação")
       Tit.setSize(18)
       Tit.draw(win)
       subLinha = Line(Point(300, 50), Point(500, 50))
       subLinha.setFill("Black")
       subLinha.setWidth(6)
       subLinha.draw(win)

       #Nome + Pontos
       if pts == 1:
           PontFinal = Text(Point(400, 100), ("-", player, "-", pts, "Ponto"))
           PontFinal.setSize(16)
           PontFinal.draw(win)
       else:
           PontFinal = Text(Point(400, 100), ("-", player, "-", pts, "Pontos"))
           PontFinal.setSize(16)
           PontFinal.draw(win)

       #Fundo preto dos dois lados
       linhaEsquerda = Line(Point(2, 0), Point(2, 600))
       linhaEsquerda.setWidth(500)
       linhaEsquerda.setFill("Black")
       linhaEsquerda.draw(win)

       linhaDireita = Line(Point(798, 0), Point(798, 600))
       linhaDireita.setWidth(500)
       linhaDireita.setFill("Black")
       linhaDireita.draw(win)


       # Função para apagar tudo da interface da pontuação
       def apagar():
           continuarJogo.undraw()
           continuarJ.undraw()
           sair.undraw()
           linhaDireita.undraw()
           linhaEsquerda.undraw()
           PontFinal.undraw()
           subLinha.undraw()
           Textosair.undraw()
           Tit.undraw()

       # Função dos 3 botões que vai ser chamada mais para frente
       def buttons():
           continuarJogo = Rectangle (Point(285, 500), Point(385, 525))  # Botão Dificuldade Fácil
           continuarJogo.setOutline("Black")
           continuarJogo.draw(win)

           sair = Rectangle (Point(415, 500), Point(515, 525))  # Botão Dificuldade Média
           sair.setOutline("Black")
           sair.draw(win)

           return continuarJogo, sair

       def inside(point, rectangle):

           ie = rectangle.getP1()  # (lower left)
           sd = rectangle.getP2()  # (upper right)

           return ie.getX() < point.getX() < sd.getX() and ie.getY() < point.getY() < sd.getY()


       continuarJogo, sair = buttons()

       continuarJ = Text (Point(335, 513), "Continuar")
       continuarJ.setSize(12)
       continuarJ.draw(win)

       Textosair = Text (Point(465, 513), "Sair do jogo")
       Textosair.setSize(12)
       Textosair.draw(win)

       # Ativando os botões pressionáveis ao clique
       while True:
           clickPoint = win.getMouse()

           if clickPoint is None:
               Nome.setText("")
           elif inside(clickPoint, continuarJogo):
               print(Nome.getText())

               continuarJ.undraw()
               continuarJ = Text(Point(335, 513), "Continuar")
               continuarJ.setSize(12)
               continuarJ.setFill("Green")
               continuarJ.draw(win)

               time.sleep(0.5)
               apagar()
               win.getMouse()
               break
           elif inside(clickPoint, sair):

               Textosair.undraw()
               Textosair = Text(Point(465, 513), "Sair do jogo")
               Textosair.setSize(12)
               Textosair.setFill("Green")
               Textosair.draw(win)


               time.sleep(0.5)
               win.close()
               break

       win.close()

   #Espera você clicar para reiniciar após perder UMA vida
   win.getMouse()
   Continue.undraw()
   win.setBackground(color_rgb(194,205,225))
   circulo.undraw()
   col = 390
   lin = 80
   raio = 15
   circulo = Circle(Point(col, lin), raio)
   circulo.setFill("Black")
   circulo.draw(win)
   win.getMouse()

 #Animação de movimento da bolinha durante o jogo
 circulo.undraw()
 col += passo
 lin += velocidade
 circulo = Circle(Point(col, lin), 15)
 circulo.setFill("Black")
 circulo.draw(win)

 # Movimento horizontal da barra pelas setas direita/esquerda
 tecla = win.checkKey()

 # Sair do joguinho com "esc"
 if tecla == "Escape":
     continuar = False
     continue

 #Abaixo tem o movimento da barra ao apertar (< ou d) e (> ou a)
 if tecla == "Right" or tecla == "d":
     if (colIni + 20) < drt:
         colIni = colIni + 20

     barra.undraw()
     barra = Line(Point(colIni, 530), Point(colIni + tamanho, 530))
     barra.setFill(corBarra)
     barra.setWidth(10)
     barra.draw(win)

 if tecla == "Left" or tecla == "a":
     if (colIni - 20) > -1:
         colIni = colIni - 20

     barra.undraw()
     barra = Line(Point(colIni, 530), Point(colIni + tamanho, 530))
     barra.setFill(corBarra)
     barra.setWidth(10)
     barra.draw(win)

 # A cada ponto a velocidade da bolinha aumenta
 if pts == 0:
   time.sleep(0.06)
 elif pts == 1:
   time.sleep(0.06)
 elif pts == 2:
   time.sleep(0.05)
 elif pts == 3:
   time.sleep(0.05)
 elif pts == 4:
   time.sleep(0.04)
 elif pts == 5:
   time.sleep(0.04)
 elif pts == 6:
   time.sleep(0.03)
 elif pts == 7:
   time.sleep(0.03)
 elif pts == 8:
   time.sleep(0.02)
 elif pts == 9:
   time.sleep(0.02)
 elif pts > 9: #Quando chega a 10 pontos
   varPasso = 1
   time.sleep(0.01)
   win.setBackground(color_rgb(150, 46, 65)) #A cor do fundo muda
   tamanho = 95 #O tamnanho da barra diminui
   drt = 705
   corBarra = "Red" #Cor da barra virar vermelha

win.close()


