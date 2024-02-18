import pygame
from pygame.locals import *

def subdivide(v, p, q, r, col, level):
    if level >= 10:
        pixel_col = (min(col[0], 255), min(col[1], 255), min(col[2], 255))
        pygame.draw.polygon(surface, pixel_col, ((int(p.pos[0]), int(p.pos[1])),
                                                 (int(q.pos[0]), int(q.pos[1])),
                                                 (int(r.pos[0]), int(r.pos[1]))))
        return

    col = (randint(col[0], col[0] + 6), randint(col[1], col[1] + 6), randint(col[2], col[2] + 6))
    m = Point(((p.pos[0] + q.pos[0]) / 2, (p.pos[1] + q.pos[1]) / 2), col)
    n = Point(((q.pos[0] + r.pos[0]) / 2, (q.pos[1] + r.pos[1]) / 2), col)
    o = Point(((p.pos[0] + r.pos[0]) / 2, (p.pos[1] + r.pos[1]) / 2), col)

    subdivide(v, m, n, o, p.col if v[0] == 0 else col, level + 1)
    subdivide(v, p, o, m, p.col if v[1] == 0 else col, level + 1)
    subdivide(v, m, n, q, p.col if v[2] == 0 else col, level + 1)
    subdivide(v, o, r, n, p.col if v[3] == 0 else col, level + 1)

    
def main():
    pygame.init()
    surface = pygame.display.set_mode((800, 600))

    subdivide(surface, (400, 100), (100, 500), (700, 500), 0)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return

if __name__ == "__main__":
    main()