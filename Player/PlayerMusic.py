# import playsound
import pygame

pygame.mixer.init()
pygame.base.init()
print('1 - Monster')
print('2 - Menina Linda')
print('3 - Planeta Sonho')
print('4 - Sutilmente')
print('5 - Save Me')

choose = int(input('Which music to play?: '))

if choose == 1:
    song = 'Monster.mp3'
elif choose == 2:
    song = 'MeninaLinda.mp3'
elif choose == 3:
    song = 'PlanetaSonho.mp3'
elif choose == 4:
    song = 'Sutilmente.mp3'
elif choose == 5:
    song = 'SaveMe.mp3'

pygame.mixer.music.load(song)
pygame.mixer.music.play()

print('Playing...')
print('Type it \'stop\' to Stop!')
print('Type it \'pause\' to Pause!')

while pygame.mixer.music.get_busy():
    if input() == 'stop':
        pygame.mixer.music.stop()
        # break
    if input() == 'pause':
        print('Pausing...')
        pygame.mixer.music.pause()
        print('Type it \'play\' to Continue!')
        if input() == 'play':
            pygame.mixer.music.unpause()
    pygame.time.Clock()

print('\nStop')

print(len(song))

# playsound.playsound(song)
