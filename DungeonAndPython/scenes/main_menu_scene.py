#from base_scene import Base
import pygame

class MainMenuScene():
    def __init__(self, scene_manager):
        self.scene_manager = scene_manager
        
        # Estado interno del menú
        self.font = pygame.font.SysFont(None, 60)

    def handle_event(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    print("Start pressed")
                    # Aquí luego cambiarás a otra escena
                    # self.scene_manager.change_scene(CombatScene)

    def update(self):
        pass

    def render(self, screen):
        screen.fill((30, 30, 30))

        text = self.font.render("DUNGEON & PYTHON", True, (200, 200, 200))
        screen.blit(text, (150, 200))
