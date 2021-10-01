from kivy.uix.button import Button

from constants import OMNISYNTH_PATH


class LedButton(Button):
    def __init__(self):
        super().__init__()
        self.active = False

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.background_color = [0, 85, 255, 1]
            pattern_action = 'stop' if self.active else 'start'
            self.manager.omni_instance.pattern_sel(
                self.text, pattern_action, OMNISYNTH_PATH)
            self.active = not self.active

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            self.background_color = [1, 1, 1, 1]
