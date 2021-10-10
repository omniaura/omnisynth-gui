from kivy.uix.button import Button

from omniapp.constants import OMNISYNTH_PATH
from kivy.properties import BooleanProperty, NumericProperty, StringProperty

from kivy.app import App

class LedButton(Button):
    active = BooleanProperty()

    def on_touch_down(self, touch):
        omni = App.get_running_app().root.omni_instance
        if self.collide_point(*touch.pos):
            self.background_color = [0, 85, 255, 1]
            pattern_action = 'stop' if self.active else 'start'
            omni.pattern_sel(
                self.text, pattern_action, OMNISYNTH_PATH)
            self.active = not self.active

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            self.background_color = [1, 1, 1, 1]
