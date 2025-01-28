import pygame

import math

def line_circle_collision(line_start, line_end, circle_center, circle_radius):

    dx = line_end[0] - line_start[0]
    dy = line_end[1] - line_start[1]

    px = circle_center[0] - line_start[0]
    py = circle_center[1] - line_start[1]

    dot = dx * px + dy * py

    if dot < 0 or dot > (dx * dx + dy * dy):
        return False

    u = dot / (dx * dx + dy * dy)

    x_closest = line_start[0] + u * dx
    y_closest = line_start[1] + u * dy

    dist = math.sqrt((x_closest - circle_center[0]) ** 2 + (y_closest - circle_center[1]) ** 2)

    if dist <= circle_radius:
        return (x_closest, y_closest)
    return False


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

    line_start = (posx+1000,posy+1000)
    line_end = (posx-1000,posy-1000)
    circle_center = (768,270)
    circle_radius = 75

    screen.fill("black")

    # Render the graphics here.
    # ...

    clock.tick(60)

    pygame.draw.circle(screen, (255, 255, 255), (posx,posy), 10)  
    pygame.draw.circle(screen, (255, 255, 255), (768,270), 75)

    if line_circle_collision(line_start, line_end, circle_center, circle_radius):
        
        newposx,newposy = line_circle_collision(line_start, line_end, circle_center, circle_radius)
        if posx > 768:
            pygame.draw.line(screen, (255, 255, 255), line_start, (newposx,newposy), 3)
            print(newposx)
            print(newposy)
        else:
            pygame.draw.line(screen, (255, 255, 255), (newposx,newposy), line_end, 3)
            print(newposx)
            print(newposy)
    else:
        pygame.draw.line(screen, (255, 255, 255), line_start, line_end, 3)

    pygame.display.update()