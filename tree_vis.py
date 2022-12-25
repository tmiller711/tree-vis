import pygame

WIDTH, HEIGHT = 750, 450
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tree Visualization")
FPS = 60
pygame.init()

# game variables
font = pygame.font.Font('./assets/OpenSans.ttf', 36)

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class TreeNode:
    def __init__(self, val):
        self.radius = 30
        self.val = val
        self.left = None
        self.right = None

    def draw_node(self):
        x = WIDTH//2
        y = 50
        pygame.draw.circle(WIN, WHITE, (x, y), self.radius, 1)

        text_surface = font.render(self.val, 1, WHITE)
        WIN.blit(text_surface, (x-9, y//2))

def draw_window(nodes):
    WIN.fill(BLACK)
    for node in nodes:
        node.draw_node()


    # Set the line start and end points
    # line_start = (WIDTH//2, 50 + 30)
    # line_end = (100, 100)

    # Set the line color
    # line_color = WHITE

    # pygame.draw.line(WIN, line_color, line_start, line_end, 1)
    pygame.display.update()

def main():
    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        node = TreeNode(val="5")

        draw_window([node])

    main()

if __name__ == "__main__":
    main()
