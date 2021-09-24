from omniapp import OmniSynth
from kivy.uix.button import Button

from constants import OMNISYNTH_PATH

class ToneButton(Button):
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            OmniSynth.synth_sel(self.text, OMNISYNTH_PATH)
            OmniSynth.patchIndex = OmniSynth.patchListIndex[self.text]
            self.background_color = [0, 85, 255, 1]
            if touch.is_double_tap:
                if self.text == 'tone5':
                    sm.current = 'Tone5Page'
                else:
                    sm.current = 'KnobValPage'

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            self.background_color = [1, 1, 1, 1]
