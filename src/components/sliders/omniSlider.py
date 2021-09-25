from omniapp import KnobCoords, OmniSynth
from kivy.uix.slider import Slider

class OmniSlider(Slider):
    def __init__(self, name):
        super().__init__(
            background_disabled_vertical = 'atlas://data/images/defaulttheme/sliderv_background',
            cursor_disabled_image = '../../../assets/sliderV3.png',
            orientation = 'vertical',
            size_hint_y = 0.75,
            size_hint_x = 0.25,
            pos_hint = {'x':0.5, 'y': 0.25},
            range = [0,127],
            step = 1
        )
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
