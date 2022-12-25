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
    def __init__(self, val, x, y):
        self.radius = 30
        self.val = val
        self.x = x
        self.y = y
        self.left = None
        self.right = None

    def draw_node(self):
        # x = WIDTH//2
        # y = 50
        pygame.draw.circle(WIN, WHITE, (self.x, self.y), self.radius, 1)

        text_surface = font.render(self.val, 1, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (self.x, self.y)

        WIN.blit(text_surface, text_rect)

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

        node1 = TreeNode("5", WIDTH//2, 50)
        node2 = TreeNode("8", WIDTH//2-50, 100)
        node3 = TreeNode("3", WIDTH//2+50, 100)

        draw_window([node1, node2, node3])

    main()

if __name__ == "__main__":
    main()
