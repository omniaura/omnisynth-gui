from omniapp import KnobCoords, OmniSynth
from kivy.uix.slider import Slider
from kivy.properties import BooleanProperty, NumericProperty, StringProperty


class OmniSlider(Slider):
    slider_name = StringProperty()
    hold_value = NumericProperty()
    prev_value = NumericProperty()
    disabled = BooleanProperty()
    updater_slider_on = BooleanProperty()

    def on_touch_move(self, touch):
        if self.collide_point(*touch.pos):
            self.updater_slider_on = False
            self.value_pos = touch.pos
            self.hold_value = self.value
            self.hold_value = max(0, min(self.hold_value, 127))
            self.value = self.hold_value
            if self.slider_name in KnobCoords:
                self.prev_val = self.manager.omni_instance.knob_table[KnobCoords[self.slider_name]]
                self.manager.omni_instance.filter_sel(
                    self.slider_name, self.value)
