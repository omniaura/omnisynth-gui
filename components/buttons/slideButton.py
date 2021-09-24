from omniapp import KnobCoords, OmniSynth
from kivy.uix.button import Button

class SlideButton(Button):
    def __init__(self, name):
        super().__init__()
        self.button_name = name

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.background_color = [0, 85, 255, 1]
            if OmniSynth.mapMode:
                if len(OmniSynth.knob_table) != 0:
                    with self.canvas:
                        self.opacity = 1
                    src = OmniSynth.control_evnt[2]
                    chan = OmniSynth.control_evnt[3]
                    KnobCoords[self.button_name] = (src, chan)
                    OmniSynth.map_knob((src,chan), self.button_name)

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            self.background_color = [1, 1, 1, 1]
