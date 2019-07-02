# Play_music_Pygame
Player music using the API _pygame_
## Musics
- Eminem ft. Rihanna - The Monster
- Chiclete com Banana - Menina Linda ( I should Have No Better)
- 14 Bis - Planeta Sonho
- Skank - Sutilmente
- REMY ZERO - SAVE ME
## Code
```python
import pygame

pygame.mixer.init()
pygame.base.init()
print('1 - Monster')
print('2 - Menina Linda')
print('3 - Planeta Sonho')
print('4 - Sutilmente')
print('5 - Save Me')

choose = int(input('Which music to play?: '))
```
