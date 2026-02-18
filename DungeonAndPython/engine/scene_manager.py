class SceneManager:
#Inicia con la escena actual y la guarda en current_scene
    def __init__(self, initial_scene):
        self.current_scene = initial_scene(self)
        self.next_scene = None

#cambia las escenas por la nueva escena
    def change_scene(self, new_scene_class):
        self.next_scene = new_scene_class

#Obtiene el llamado de evento de la escena actual
    def handle_event(self, events):
        self.current_scene.handle_event(events)

#detecta si hay una nueva escena y cambia por la nueva escena
    def update(self):
        if self.next_scene:
            self.current_scene = self.next_scene()
            self.next_scene = None

        self.current_scene.update()

#renderiza la nueva escena
    def render(self, screen):
        self.current_scene.render(screen)
