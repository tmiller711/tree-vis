import pygame
import time

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
RED = (255, 0, 0)
GREEN = (0, 255, 0)

class TreeNode:
    def __init__(self, val, x, y, color=WHITE):
        self.radius = 30
        self.val = val
        self.x = x
        self.y = y
        self.left = None
        self.right = None
        self.color = color

    def draw_node(self):
        pygame.draw.circle(WIN, self.color, (self.x, self.y), self.radius, 1)

        text_surface = font.render(self.val, 1, self.color)
        text_rect = text_surface.get_rect()
        text_rect.center = (self.x, self.y)

        WIN.blit(text_surface, text_rect)

        if self.left:
            connect_nodes(self, self.left)

        if self.right:
            connect_nodes(self, self.right)

def build_tree():
    root = TreeNode("5", WIDTH//2, 50)
    root.left = TreeNode("8", WIDTH//2-75, 155)
    root.right = TreeNode("3", WIDTH//2+75, 155)

    root.left.left = TreeNode("9", WIDTH//2-150, 260)
    root.left.right = TreeNode("12", WIDTH//2-75, 260)

    root.right.left = TreeNode("21", WIDTH//2+150, 260)
    root.right.right = TreeNode("19", WIDTH//2+75, 260)

    return root

def connect_nodes(node1, node2, color=WHITE):
    line_start = (node1.x, node1.y+node1.radius)
    line_end = (node2.x, node2.y-node2.radius)
    line_color = color
    pygame.draw.line(WIN, line_color, line_start, line_end, 1)

def bfs(root):
    queue = [root]

    while queue:
        current = queue.pop(0)
        current.color = RED
        current.draw_node()
        pygame.display.update()

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
        time.sleep(1)

def dfs(root):
    stack = [root]

    while stack:
        current = stack.pop()
        current.color = RED
        current.draw_node()
        pygame.display.update()

        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
        time.sleep(1)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)

        root.color = RED
        root.draw_node()
        pygame.display.update()
        time.sleep(1)

def inorder(root):
    if root:
        inorder(root.left)

        root.color = RED
        root.draw_node()
        pygame.display.update()
        time.sleep(1)

        inorder(root.right)

def preorder(root):
    if root:
        root.color = RED
        root.draw_node()
        pygame.display.update()
        time.sleep(1)
        
        preorder(root.left)
        preorder(root.right)

def map_algo_text(algo):
    if algo == 1:
        return "Depth First Search"
    elif algo ==2:
        return "Breadth First Search"
    elif algo == 3:
        return "Preorder"
    elif algo == 4:
        return "Postorder"
    elif algo == 5:
        return "Inorder"

def draw_tree(root, algo):
    WIN.fill(BLACK)

    queue = [root]

    while queue:
        current = queue.pop()
        current.draw_node()
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    text_surface = font.render(map_algo_text(algo), 1, GREEN)
    width, height = text_surface.get_size()
    WIN.blit(text_surface, ((WIDTH//2)-(width//2), HEIGHT-200))

    text_surface = font.render("Press ENTER to return to menu", 1, WHITE)
    width, height = text_surface.get_size()
    WIN.blit(text_surface, ((WIDTH//2)-(width//2), HEIGHT-100))

    pygame.display.update()

    # replace with switch statement
    if algo == 1:
        dfs(root)
    elif algo == 2:
        bfs(root)
    elif algo == 3:
        preorder(root)
    elif algo == 4:
        postorder(root)
    elif algo == 5:
        inorder(root)

def draw_menu(algo):
    WIN.fill(BLACK)

    text_surface = font.render("Available Algorithms:", 1, WHITE)
    width, height = text_surface.get_size()
    WIN.blit(text_surface, ((WIDTH//2)-(width//2), 10))

    text_surface = font.render("DFS: 1  |  BFS: 2", 1, WHITE)
    width, height = text_surface.get_size()
    WIN.blit(text_surface, ((WIDTH//2)-(width//2), 100))

    text_surface = font.render("Preorder: 3  |  Postorder: 4  |  Inorder: 5", 1, WHITE)
    width, height = text_surface.get_size()
    WIN.blit(text_surface, ((WIDTH//2)-(width//2), 200))

    text_surface = font.render("Press enter to start", 1, WHITE)
    width, height = text_surface.get_size()
    WIN.blit(text_surface, ((WIDTH//2)-(width//2), 350))
    
    text_surface1 = font.render(f"Current selection: ", 1, WHITE)
    text_surface2 = font.render(f"{map_algo_text(algo)}", 1, GREEN)
    text1_width, _ = text_surface1.get_size()
    text2_width, _ = text_surface2.get_size()

    text1_x = (WIDTH//2)-((text1_width+text2_width)//2)
    text2_x = text1_x + text1_width + 10
    WIN.blit(text_surface1, (text1_x, 450))
    WIN.blit(text_surface2, (text2_x, 450))

    pygame.display.update()

def main():
    clock = pygame.time.Clock()

    run = True
    start = False
    algo = 1
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                # replace with swtich statement
                if event.key == pygame.K_RETURN:
                    start = not start
                if event.key == pygame.K_1:
                    algo = 1
                if event.key == pygame.K_2:
                    algo = 2
                if event.key == pygame.K_3:
                    algo = 3
                if event.key == pygame.K_4:
                    algo = 4
                if event.key == pygame.K_5:
                    algo = 5

        root = build_tree()

        if start == True:
            draw_tree(root, algo)
        else:
            draw_menu(algo)

    main()

if __name__ == "__main__":
    main()
