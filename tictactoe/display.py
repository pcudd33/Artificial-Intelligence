# Provides a graphical interface for tic-tac-toe.
from minimax import *
import pygame

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# State
turn = 0
state = start_state()

# Display
pygame.init()
display = pygame.display.set_mode([300, 400])
text = pygame.font.SysFont("comicsansms", 72).render('AI Move', False, black)

# Game loop
displaying = True
while displaying:

    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Window closed
            displaying = False
        elif event.type == pygame.MOUSEBUTTONDOWN:  # Mouse clicked
            if pygame.mouse.get_pressed()[0] and utility(state) is None:
                x, y = pygame.mouse.get_pos()

                # AI move selection
                if y > 300:
                    if turn % 2 == 0:
                        value, action = max_value(state, alpha=-1, beta=+1)
                    else:
                        value, action = min_value(state, alpha=-1, beta=+1)

                # Human move selection
                else:
                    row = y // 100
                    col = x // 100
                    action = row * 3 + col

                # State update
                if action in action_list(state):
                    if turn % 2 == 0:
                        state = max_next_state(state, action)
                    else:
                        state = min_next_state(state, action)

                    turn += 1

    # Display update
    display.fill(white)
    display.blit(text, (0, 300))
    pygame.draw.line(display, black, (100, 0), (100, 300))
    pygame.draw.line(display, black, (200, 0), (200, 300))
    pygame.draw.line(display, black, (0, 100), (300, 100))
    pygame.draw.line(display, black, (0, 200), (300, 200))

    for i in range(9):
        y = i // 3 * 100
        x = i % 3 * 100

        if state[i] == 1:
            pygame.draw.line(display, black, (x+10, y+10), (x+90, y+90))
            pygame.draw.line(display, black, (x+90, y+10), (x+10, y+90))
        elif state[i] == -1:
            pygame.draw.circle(display, black, (x+50, y+50), 40, width=1)

    pygame.display.flip()

pygame.quit()