from kivy.uix.button import Button
from kivy.properties import StringProperty


class ScreenNavButton(Button):
    screen_name = StringProperty()

    def on_release(self):
        self.manager.current = self.screen_name
