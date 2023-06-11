import pygame

FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WIDTH = 800
HEIGHT = 600

class Position:

    def __init__(self, x, y):
        self.x=x
        self.y=y

class Player:
    
    def __init__(self, game_window: pygame.surface.Surface, width=50, height=50, speed=1):
        self.width=width
        self.height=height
        self.speed=speed
        self.position = Position(
            game_window.get_width() // 2 - self.width // 2,
            game_window.get_height() // 2 - self.height // 2
        )

    def set_pos(self, position: Position):
        self.position=position

    def draw_sprite(self, game_window, color=(123, 123, 123), radius=20):
        pygame.draw.circle(game_window, color, [self.position.x, self.position.y], radius)

    def move(self, key):
        match key:
            case pygame.K_LEFT:
                self.set_pos(
                    Position(
                        self.position.x - self.speed,
                        self.position.y
                    )
                )
            case pygame.K_RIGHT:
                self.set_pos(
                    Position(
                        self.position.x + self.speed,
                        self.position.y
                    )
                )
            case pygame.K_UP:
                self.set_pos(
                    Position(
                        self.position.x,
                        self.position.y - self.speed
                    )
                )
            case pygame.K_DOWN:
                self.set_pos(
                    Position(
                        self.position.x,
                        self.position.y + self.speed
                    )
                )

class Game:
    
    def __init__(self):
        # Initialize Pygame
        pygame.init()
        # Set up the game window
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Unnamed Farm Sim")
        # Set up the player
        self.PLAYER = Player(game_window = self.screen)
        # Set up game
        self.clock = pygame.time.Clock()

        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            else:
                keys = pygame.key.get_pressed()
                print(keys)
                # for key in keys:
                #     self.PLAYER.move(key)

    def update(self):
        pass

    def render(self):
        self.screen.fill(BLACK)
        self.PLAYER.draw_sprite(game_window=self.screen, radius=self.PLAYER.width//2)
        pygame.display.flip()

    def game_loop(self):
        self.is_running = True
        while self.is_running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.game_loop()