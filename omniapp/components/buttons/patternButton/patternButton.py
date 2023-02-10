from kivy.uix.button import Button

from omniapp.constants import OMNISYNTH_PATH
from kivy.properties import BooleanProperty, NumericProperty, StringProperty

from kivy.app import App


class PatternButton(Button):
    active = BooleanProperty(False)
    pattern_filename = StringProperty()

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.manager.OmniSynth.set_active_pattern(self.patch_filename)
            self.background_color = [0, 85, 255, 1]
            if self.active:
                self.manager.OmniSynth.stop_pattern(self.pattern_filename)
            else:
                self.manager.OmniSynth.start_pattern(self.pattern_filename)
            self.active = not self.active

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            self.background_color = [1, 1, 1, 1]
