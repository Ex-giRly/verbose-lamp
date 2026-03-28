import pygame

pygame.init()

screen = pygame.display.set_mode((600,800))

clock = pygame.time.Clock()

colors = {
    "L": (0, 0, 255),
    "R": (255, 255, 0),
    "T": (0, 255, 0),
    "B": (0, 255, 0),
    "D": (255, 255, 255)
}
x, y, w, h = 30, 30, 60, 60

running = True

while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 3
    y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * 3

    x = max(0, min(x, 500 - w))
    y = max(0, min(y, 500 - h))

    color = colors["D"]
    if x == 0: color = colors["L"]
    elif x == 500 - w: color = colors["R"]
    elif y == 0: color = colors["T"]
    elif y == 500: color = colors["B"]

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, color, (x, y, w, h))
    pygame.display.flip()
    clock.tick(60)
pygame.Quit()