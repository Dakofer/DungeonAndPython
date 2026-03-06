from textual.app import App
from textual.widgets import ListView, ListItem, Label

class Menu(App):

    def compose(self):
        yield ListView(
            ListItem(Label("Start Game")),
            ListItem(Label("Load Game")),
            ListItem(Label("Exit"))
        )

Menu().run()
