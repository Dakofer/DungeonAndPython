import pygame
from engine.scene_manager import SceneManager
from scenes.main_menu_scene import MainMenuScene

class Game:
    def __init__(self):
        pygame.init()
        # 2. Configuración de pantalla
        ANCHO, ALTO = 800, 600
        self.screen = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption("Dungeon & Python")

        #reloj de fps
        self.clock = pygame.time.Clock()

        # Definición de colores
        BLANCO = (255, 255, 255)

        self.scene_manager = SceneManager(MainMenuScene)

        #determina si el programa esta vivo
        self.is_running = True
     
    def handle_event(self):
        for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.is_running = False

    def update(self):
        events = pygame.event.get()

        self.scene_manager.handle_event(events)
        self.scene_manager.update()
        self.scene_manager.render(self.screen)

    def render(self):
        self.screen.fill((0, 0, 0))
        pygame.display.flip()

    def run(self):
       while self.is_running:
            self.handle_event()
            self.update()
            self.render()
            self.clock.tick(60)
