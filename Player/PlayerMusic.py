# import playsound
import pygame

pygame.mixer.init()
pygame.base.init()
print('1 - Monster')
print('2 - Menina Linda')
print('3 - Planeta Sonho')
print('4 - Sutilmente')
print('5 - Save Me')

escolha = int(input('Qual musica tocar: '))

if escolha == 1:
    musica = 'Monster.mp3'
elif escolha == 2:
    musica = 'MeninaLinda.mp3'
elif escolha == 3:
    musica = 'PlanetaSonho.mp3'
elif escolha == 4:
    musica = 'Sutilmente.mp3'
elif escolha == 5:
    musica = 'SaveMe.mp3'

pygame.mixer.music.load(musica)
pygame.mixer.music.play()

print('Tocando...')
print('Digite \'stop\' para Parar!')
print('Digite \'pause\' para Pausar!')

while pygame.mixer.music.get_busy():
    if input() == 'stop':
        pygame.mixer.music.stop()
        # break
    if input() == 'pause':
        print('Pausado...')
        pygame.mixer.music.pause()
        print('Digite \'play\' para Continuar!')
        if input() == 'play':
            pygame.mixer.music.unpause()
    pygame.time.Clock()

print('\nStop')

print(len(musica))

# playsound.playsound(musica)
