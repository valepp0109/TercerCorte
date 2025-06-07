import pygame
import random

# Inicializar pygame
pygame.init()

# Configuración de pantalla
WIDTH, HEIGHT = 300, 600
BLOCK_SIZE = 30
COLUMNS = WIDTH // BLOCK_SIZE
ROWS = HEIGHT // BLOCK_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris Retro Gamer")

# Colores
NEON_COLORS = [
    (255, 20, 147), (0, 255, 255), (0, 255, 0),
    (255, 255, 0), (255, 105, 180), (0, 191, 255), (255, 69, 0),
]
BG_COLOR = (18, 10, 30)
GRID_COLOR = (40, 40, 40)

# Formas de las piezas
SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[0, 1, 1], [1, 1, 0]],
    [[1, 1, 0], [0, 1, 1]],
    [[1, 0, 0], [1, 1, 1]],
    [[0, 0, 1], [1, 1, 1]],
    [[0, 1, 0], [1, 1, 1]],
]

class Piece:
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color
        self.rotation = 0
        self.x = COLUMNS // 2 - len(shape[0]) // 2
        self.y = 0

    def image(self):
        return self.shape[self.rotation % len(self.shape)]

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.shape)

def get_rotations(shape):
    rotations = [shape]
    for _ in range(3):
        shape = [list(row) for row in zip(*shape[::-1])]
        rotations.append(shape)
    return rotations

def create_grid(locked={}):
    grid = [[BG_COLOR for _ in range(COLUMNS)] for _ in range(ROWS)]
    for (x, y), color in locked.items():
        if y > -1:
            grid[y][x] = color
    return grid

def draw_grid(surface, grid):
    for y in range(ROWS):
        for x in range(COLUMNS):
            pygame.draw.rect(surface, grid[y][x], (x*BLOCK_SIZE, y*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)
    for y in range(ROWS):
        pygame.draw.line(surface, GRID_COLOR, (0, y*BLOCK_SIZE), (WIDTH, y*BLOCK_SIZE))
    for x in range(COLUMNS):
        pygame.draw.line(surface, GRID_COLOR, (x*BLOCK_SIZE, 0), (x*BLOCK_SIZE, HEIGHT))

def convert_shape(piece):
    positions = []
    shape = piece.image()
    for i, row in enumerate(shape):
        for j, val in enumerate(row):
            if val:
                positions.append((piece.x + j, piece.y + i))
    return positions

def valid_space(piece, grid):
    accepted = [[(x, y) for x in range(COLUMNS) if grid[y][x] == BG_COLOR] for y in range(ROWS)]
    accepted = [pos for row in accepted for pos in row]
    for pos in convert_shape(piece):
        if pos not in accepted:
            if pos[1] >= 0:
                return False
    return True

def check_lost(locked):
    return any(y < 1 for (_, y) in locked)

def clear_rows(grid, locked):
    cleared = 0
    for y in range(ROWS - 1, -1, -1):
        if BG_COLOR not in grid[y]:
            cleared += 1
            for x in range(COLUMNS):
                del locked[(x, y)]
            for (x2, y2) in sorted(locked.keys(), key=lambda k: k[1])[::-1]:
                if y2 < y:
                    locked[(x2, y2 + 1)] = locked.pop((x2, y2))
    return cleared

def get_shape():
    shape = random.choice(SHAPES)
    return Piece(get_rotations(shape), random.choice(NEON_COLORS))

def draw_text_middle(surface, text, size, color):
    font = pygame.font.SysFont("consolas", size)
    label = font.render(text, True, color)
    surface.blit(label, (WIDTH//2 - label.get_width()//2, HEIGHT//2 - label.get_height()//2))

def main():
    clock = pygame.time.Clock()
    fall_time = 0
    fall_speed = 0.5
    level = 1
    lines_cleared = 0
    score = 0
    locked = {}
    current = get_shape()
    next_piece = get_shape()
    grid = create_grid(locked)
    run = True
    lost = False

    while run:
        grid = create_grid(locked)
        fall_time += clock.get_rawtime()
        clock.tick()

        if fall_time / 1000 > fall_speed:
            fall_time = 0
            current.y += 1
            if not valid_space(current, grid):
                current.y -= 1
                for pos in convert_shape(current):
                    locked[(pos[0], pos[1])] = current.color
                current = next_piece
                next_piece = get_shape()
                cleared = clear_rows(grid, locked)
                score += cleared * 10
                lines_cleared += cleared
                if cleared > 0 and lines_cleared >= 5:
                    level += 1
                    fall_speed = max(0.1, fall_speed - 0.05)
                    lines_cleared = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and not lost:
                if event.key == pygame.K_LEFT:
                    current.x -= 1
                    if not valid_space(current, grid):
                        current.x += 1
                elif event.key == pygame.K_RIGHT:
                    current.x += 1
                    if not valid_space(current, grid):
                        current.x -= 1
                elif event.key == pygame.K_DOWN:
                    current.y += 1
                    if not valid_space(current, grid):
                        current.y -= 1
                elif event.key == pygame.K_UP:
                    current.rotate()
                    if not valid_space(current, grid):
                        current.rotation = (current.rotation - 1) % len(current.shape)

        screen.fill(BG_COLOR)
        draw_grid(screen, grid)

        for x, y in convert_shape(current):
            if y >= 0:
                pygame.draw.rect(screen, current.color, (x*BLOCK_SIZE, y*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)

        font = pygame.font.SysFont("consolas", 24)
        score_txt = font.render(f"Puntaje: {score}", True, (255, 255, 255))
        level_txt = font.render(f"Nivel: {level}", True, (255, 255, 255))
        screen.blit(score_txt, (10, 10))
        screen.blit(level_txt, (10, 40))

        pygame.display.update()

        if check_lost(locked):
            lost = True
            draw_text_middle(screen, "GAME OVER", 36, (255, 0, 0))
            pygame.display.update()
            pygame.time.delay(1500)
            waiting = True
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                        waiting = False
                        run = False

    pygame.quit()

main()
