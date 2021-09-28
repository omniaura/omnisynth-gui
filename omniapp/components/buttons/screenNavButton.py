from kivy.uix.button import Button
from kivy.properties import ObjectProperty


class ScreenNavButton(Button):
    screenmanager = ObjectProperty()

    def __init__(self, screen_name):
        super().__init__(text='>', size_hint=[
            0.08, 0.7], pos_hint={'x': 0.91, 'y': 0.15})
        self.screen_name = screen_name

    def on_release(self):
        self.screenmanager.current = self.screen_name
