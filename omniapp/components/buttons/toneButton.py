from omniapp import OmniSynth
from kivy.uix.button import Button
from kivy.properties import ObjectProperty

from constants import OMNISYNTH_PATH


class ToneButton(Button):
    screenmanager = ObjectProperty()

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            App.get_running_app().omni_instance.synth_sel(self.text, OMNISYNTH_PATH)
            App.get_running_app().omni_instance.patchIndex = App.get_running_app(
            ).omni.patchListIndex[self.text]
            self.background_color = [0, 85, 255, 1]
            if touch.is_double_tap:
                if self.text == 'tone5':
                    self.screenmanager.current = 'Tone5Page'
                else:
                    self.screenmanager.current = 'KnobValPage'

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            self.background_color = [1, 1, 1, 1]
