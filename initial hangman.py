# Importing the libraries
import pygame
import sys
import random
import time

# Initializing the pygame
pygame.init()

# Frames per second
clock = pygame.time.Clock()

# Window parameters
width = 800
height = 500

# Creating the window
screen = pygame.display.set_mode((width, height))

# Setting the title and icon
pygame.display.set_caption("Hangman")
icon = pygame.image.load("img_9.png")
pygame.display.set_icon(icon)

game_over = False

row = 2
col = 13
gap = 20
size = 40
boxes = []

# To draw boxes
for row in range(row):
    for col in range(col):
        x = ((col * gap) + gap) + (size * col)
        y = ((row * gap) + gap) + (size * row) + 330
        box = pygame.Rect(x, y, size, size)
        boxes.append(box)

buttons = []
A = 65

# To display alphabets
for ind, box in enumerate(boxes):
    letter = chr(A + ind)
    button = [box, letter]
    buttons.append(button)


# To draw buttons
def draw_buttons(buttons):
    for box, letter in buttons:
        btn_text = font.render(letter, True, (0, 0, 0))
        btn_rect = btn_text.get_rect(center=(box.x + 20, box.y + 20))
        screen.blit(btn_text, btn_rect)
        pygame.draw.rect(screen, (0, 0, 0), box, 2)


# To display the word...to be added


images = []
hangman_status = 0

# creating the words list
words = ['PYGAME', 'PYTHON', 'JAVA', 'HELLO', 'WORLD', 'HANGMAN', 'TIME', 'TURTLE', 'RANDOM']
word = random.choice(words)
guessed = []

# Display the initial image
image = pygame.image.load("img_21.png")
images.append(image)

# setting the font style
font = pygame.font.SysFont("arial", 30)
game_font = pygame.font.SysFont("arial", 80)
letter_font = pygame.font.SysFont("arial", 60)

# Title parameters
title = "Hangman"
title_text = game_font.render(title, True, (0, 0, 0))
title_rect = title_text.get_rect(center=(width // 2, title_text.get_height() // 2 + 10))


# Game loop
running = True
while running:
    screen.fill((255, 255, 255))
    # Checking for event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # quit event
            running = False
        # Checking for mouse position
        if event.type == pygame.MOUSEBUTTONDOWN:
            click_pos = event.pos

            # Checking  for correct letter...to be added

            # displaying the images accordingly
            for i in range(5):
                if hangman_status == 1:
                    image = pygame.image.load("img_23.png")
                    images.append(image)
                elif hangman_status == 2:
                    image = pygame.image.load("img_22.png")
                    images.append(image)
                elif hangman_status == 3:
                    image = pygame.image.load("img_24.png")
                    images.append(image)
                elif hangman_status == 4:
                    image = pygame.image.load("img_25.png")
                    images.append(image)
                elif hangman_status == 5:
                    image = pygame.image.load("img_26.png")
                    images.append(image)
                elif hangman_status == 6:
                    running = False
    screen.blit(image, (150, 150))
    for box in boxes:
        pygame.draw.rect(screen, (0, 0, 0), box, 2)

    # Win and Lost
    won = True
    for letter in word:
        if letter not in guessed:
            won = False
    if won:
        game_over = True
        game_text = "YOU WON!"
    else:
        game_text = "YOU LOST!"

    draw_buttons(buttons)
    #display_guess()
    screen.blit(title_text, title_rect)
    clock.tick(50)
    pygame.display.update()

    # Displaying the result text...to be added
pygame.quit()