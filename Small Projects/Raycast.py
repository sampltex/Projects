import pygame

pygame.init()

screen = pygame.display.set_mode((1024,576))

clock = pygame.time.Clock()

while True:
    # Process inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    # Do logical updates here.
    # ...

    posx,posy = pygame.mouse.get_pos()

    screen.fill("black")  # Fill the display with a solid color

    # Render the graphics here.
    # ...

    clock.tick(60)  # wait until next frame (at 60 FPS)

    pygame.draw.circle(screen, (255, 255, 255), (posx,posy), 10)  # Cursor circle
    pygame.draw.circle(screen, (255, 255, 255), (768,270), 75)

    pygame.draw.line(screen, (255, 255, 255), (posx-1000,posy+100000), (posx+1000,posy-100000), 3)
    pygame.draw.line(screen, (255, 255, 255), (posx-1000,posy-100000), (posx+1000,posy+100000), 3)

    pygame.display.update()
    