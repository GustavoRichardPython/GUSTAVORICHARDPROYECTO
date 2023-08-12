import pygame
import random

# Configuración de la ventana
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego de Plataformas")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Jugador
PLAYER_WIDTH, PLAYER_HEIGHT = 50, 50
PLAYER_SPEED = 7
GRAVITY = 1

# Plataforma
PLATFORM_WIDTH, PLATFORM_HEIGHT = 100, 20
PLATFORM_SPEED = 5

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 100)
        self.velocity = 0

    def update(self):
        self.velocity += GRAVITY
        self.rect.y += self.velocity

        if self.rect.top <= 0:
            self.rect.top = 0
            self.velocity = 0

        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
            self.velocity = 0

    def jump(self):
        self.velocity = -20

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.direction = random.choice((-1, 1))

    def update(self):
        self.rect.x += PLATFORM_SPEED * self.direction

        if self.rect.right >= WIDTH or self.rect.left <= 0:
            self.direction *= -1

def main():
    player = Player()
    platforms = pygame.sprite.Group()

    for i in range(5):
        platform = Platform(random.randint(0, WIDTH - PLATFORM_WIDTH), random.randint(100, HEIGHT - 100))
        platforms.add(platform)

    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    all_sprites.add(platforms)

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.jump()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            player.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            player.rect.x += PLAYER_SPEED

        # Colisión con plataformas
        if pygame.sprite.spritecollide(player, platforms, False):
            player.rect.y = platforms.sprites()[0].rect.top
            player.velocity = 0

        player.update()
        platforms.update()

        WIN.fill(BLACK)
        all_sprites.draw(WIN)
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    pygame.init()
    main()