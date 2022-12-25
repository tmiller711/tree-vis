import pygame

WIDTH, HEIGHT = 900, 600
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
        self.color = WHITE

    def draw_node(self):
        pygame.draw.circle(WIN, self.color, (self.x, self.y), self.radius, 1)

        text_surface = font.render(self.val, 1, self.color)
        text_rect = text_surface.get_rect()
        text_rect.center = (self.x, self.y)

        WIN.blit(text_surface, text_rect)

def build_tree():
    root = TreeNode("5", WIDTH//2, 50)
    root.left = TreeNode("8", WIDTH//2-75, 125)
    root.right = TreeNode("3", WIDTH//2+75, 125)

    root.left.left = TreeNode("9", WIDTH//2-150, 200)
    root.left.right = TreeNode("12", WIDTH//2-100, 200)

    return root

def connect_nodes(node1, node2):
    line_start = (node1.x, node1.y+node1.radius)
    line_end = (node2.x, node2.y-node2.radius)
    line_color = WHITE
    pygame.draw.line(WIN, line_color, line_start, line_end, 2)

def draw_window(root):
    WIN.fill(BLACK)

    queue = [root]

    while queue:
        current = queue.pop()
        current.draw_node()
        if current.left:
            connect_nodes(current, current.left)
            queue.append(current.left)
        if current.right:
            connect_nodes(current, current.right)
            queue.append(current.right)

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

        root = build_tree()

        draw_window(root)

    main()

if __name__ == "__main__":
    main()
