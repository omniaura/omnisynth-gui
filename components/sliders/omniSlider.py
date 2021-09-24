from omniapp import KnobCoords, OmniSynth
from kivy.uix.slider import Slider

class OmniSlider(Slider):
    def __init__(self, name):
        super().__init__()
        self.slider_name = name
        self.hold_value = 0

        # Had to "disable" the sliders to avoid touch interference
        self.disabled = True
        self.updateSliderOn = True
        self.prev_val = 0

    def on_touch_move(self, touch):
        if self.collide_point(*touch.pos):
            self.updateSliderOn = False
            self.value_pos = touch.pos
            self.hold_value = self.value
            self.hold_value = max(0, min(self.hold_value, 127))
            self.value = self.hold_value
            if self.slider_name in KnobCoords:
                self.prev_val = OmniSynth.knob_table[KnobCoords[self.slider_name]]
                OmniSynth.filter_sel( self.slider_name, self.value )
