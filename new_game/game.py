#importa o pygame
import pygame
#inicia o pygame
pygame.init()

#variaveis de localização
x = 400
y = 300
velocidade = 10

#cria janela
janela = pygame.display.set_mode((800,600))
#da um nome para a janela
pygame.display.set_caption("Criando um jogo em python")

#criando o loop principal
janela_aberta = True
while janela_aberta:

    pygame.time.delay(50)

    #capturando eventos
    for event in pygame.event.get():
        #condicional de fechamento
        if event.type == pygame.QUIT:
            janela_aberta = False

    # capturando as teclas pressionadas
    comandos = pygame.key.get_pressed()

    #movimentado o objeto
    if comandos[pygame.K_UP]:
        y -= velocidade
    if comandos[pygame.K_DOWN]:
        y += velocidade
    if comandos[pygame.K_RIGHT]:
        x += velocidade
    if comandos[pygame.K_LEFT]:
        x -= velocidade        

    #limpa a janela
    janela.fill((0,0,0))

    #criando um componente
    pygame.draw.circle(janela, (0,255,0), (x,y), 50)

    #atualizando a tela
    pygame.display.update()


#fecha a janela
pygame.quit()