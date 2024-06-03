import pygame
import random
import sys

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Shark Game (Snake Style)") 

#I learnt how to set the width and height of the game window from this wrbsite.  https://stackoverflow.com/questions/33963361/how-to-make-a-grid-in-pygame

background_pic = pygame.image.load("C:\\Users\\16474\\Downloads\\ocean.jpg")
background_pic = pygame.transform.scale(background_pic, (WINDOW_WIDTH, WINDOW_HEIGHT))
fish_pic = pygame.image.load("C:\\Users\\16474\\Downloads\\images (1).jpg")
fish_pic = pygame.transform.scale(fish_pic, (20, 20))
fish_pic.set_colorkey((255, 255, 255))

#I learnt how to upload images in the form of jpg. I also learnt how to make the images set to the background of the game and set to the different entities. https://www.geeksforgeeks.org/python-display-images-with-pygame/ 

pygame.mixer.music.load("C:\\Users\\16474\\Downloads\\Jaws theme!!.mp3")
eat_sound = pygame.mixer.Sound("C:\\Users\\16474\\Downloads\\Shark Eating Flesh Underwater Sound Effects No Copyright Claims ｜ All in U-TUBERS.wav")
gameover_sound = pygame.mixer.Sound("C:\\Users\\16474\\Downloads\GTA V - Wasted - Sound Effect [HQ].wav")

#This part uploads the different sound effcts and music to the game. https://www.makeuseof.com/pygame-add-sound-effects-music/#:~:text=Adding%20background%20music%20to%20a%20game%20is%20a,playing%20it.%20Here%E2%80%99s%20an%20example%3A%20pygame.mixer.music.load%28%22bgmusic.wav%22%29%20pygame.mixer.music.set_volume%280.3%29%20pygame.mixer.music.play%28%29

pygame.mixer.music.set_volume(1) 
eat_sound.set_volume(0.1)  
gameover_sound.set_volume(0.9)  

pygame.mixer.music.play(-1)

#This sets the music volume and tell it to start playing https://www.makeuseof.com/pygame-add-sound-effects-music/#:~:text=Adding%20background%20music%20to%20a%20game%20is%20a,playing%20it.%20Here%E2%80%99s%20an%20example%3A%20pygame.mixer.music.load%28%22bgmusic.wav%22%29%20pygame.mixer.music.set_volume%280.3%29%20pygame.mixer.music.play%28%29

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

def make_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

def initial_screen():
    window.blit(background_pic, (0, 0))
    make_text("Shark Game", pygame.font.Font(None, 75), (255, 0, 0), window, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 4) #Sets the title size, font and where it is on the grid
    make_text("Press any key on your keyboard to begin", pygame.font.Font(None, 40), (255, 0, 0), window, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2) #Sets the control size, font and where it is on the grid
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                waiting = False

#This is the code for the title screen of the game https://programmingpixels.com/handling-a-title-screen-game-flow-and-buttons-in-pygame.html

def wasted_screen():
    window.blit(background_pic, (0, 0))
    make_text("Wasted", pygame.font.Font(None, 100), (255, 0, 0), window, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 4) #Sets the death screen size, font and where it is on the grid
    make_text("You score was: " + str(score), pygame.font.Font(None, 40), (255, 0, 0), window, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2) #Sets the score size, font and where it is on the grid
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                waiting = False

initial_screen()

shark = [(10, 10)]
shark_direction = (1, 0)
fish = (random.randint(0, 29), random.randint(0, 19))
score = 0
fin_length = 1

#Sets the starting size, length, location and direction the snake starts in
#Also sets the score and where the fish spawns

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and shark_direction != (0, 1): #The 0, 1 here is the direction on the grid that the snake will face when the keybind is pressed. Same goes for the other three keybinds.
                shark_direction = (0, -1)
            elif event.key == pygame.K_DOWN and shark_direction != (0, -1):
                shark_direction = (0, 1)
            elif event.key == pygame.K_LEFT and shark_direction != (1, 0):
                shark_direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and shark_direction != (-1, 0):
                shark_direction = (1, 0)

#I learnt how to set the controls for the game from here. https://thepythoncode.com/article/make-a-snake-game-with-pygame-in-python 

    head = shark[0]
    dx, dy = shark_direction
    new_head = ((head[0] + dx) % 30, (head[1] + dy) % 20)
    if new_head in shark:
        running = False
    shark.insert(0, new_head)
    if new_head == fish:
        fish = (random.randint(0, 29), random.randint(0, 19))
        score += 1
        fin_length += 1
        eat_sound.play()
    else:
        if len(shark) > fin_length:
            shark.pop()

    window.blit(background_pic, (0, 0))
    for i, segment in enumerate(shark):
        pygame.draw.rect(window, GRAY, (segment[0] * 20, segment[1] * 20, 20, 20))
        if i == 0:
            pygame.draw.polygon(window, BLUE, [(segment[0] * 20 + 5, segment[1] * 20 + 5), 
                                                (segment[0] * 20 + 15, segment[1] * 20 + 5), 
                                                (segment[0] * 20 + 20, segment[1] * 20 + 10),
                                                (segment[0] * 20 + 15, segment[1] * 20 + 15),
                                                (segment[0] * 20 + 5, segment[1] * 20 + 15)])
            
            
    window.blit(fish_pic, (fish[0] * 20, fish[1] * 20))
    pygame.display.flip()

    clock.tick(10)

#This part of the code makes the shark longer each time it eats a fish. 

gameover_sound.play()

wasted_screen()

pygame.quit()