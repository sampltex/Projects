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

circle_center = [768,270] # MODIFY HOWEVER
circle_radius = 75 # MODIFY HOWEVER

while True:
    # Process inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        
    # Do logical updates here.
    # ...

    posx,posy = pygame.mouse.get_pos()

    startVal = 1000 # DO NOT TOUCH
    endVal = 1000 # DO NOT TOUCH
    rayNumber = 40 # DO NOT TOUCH

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            circle_center[0] -= 2
        elif event.key == pygame.K_RIGHT:
            circle_center[0] += 2
        elif event.key == pygame.K_UP:
            circle_radius += 5
        elif event.key == pygame.K_DOWN:
            circle_radius -= 5
        elif event.key == pygame.K_BACKSPACE:
            circle_center = [768,270] 
            circle_radius = 75

    
    screen.fill("black")

    # Render the graphics here.
    # ...

    clock.tick(60)

    pygame.draw.circle(screen, (255, 255, 255), (posx,posy), 10)  
    pygame.draw.circle(screen, (255, 255, 255), circle_center, circle_radius)

    for i in range(rayNumber):
        line_start = (posx+1000,posy+startVal)
        line_end = (posx-1000,posy-endVal)

        if line_circle_collision(line_start, line_end, circle_center, circle_radius):
            if posx < circle_center[0]:
                newposx,newposy = line_circle_collision(line_start, line_end, circle_center, circle_radius)
                pygame.draw.line(screen, (255, 255, 255), (posx,posy), (newposx,newposy), 3)
                # print(newposx)
                # print(newposy)
            else:
                pygame.draw.line(screen, (255, 255, 255), (posx,posy), line_start, 3)
        else:
            pygame.draw.line(screen, (255, 255, 255), (posx,posy), line_start, 3)

        startVal -= 50
        endVal -= 50

    pygame.display.update()