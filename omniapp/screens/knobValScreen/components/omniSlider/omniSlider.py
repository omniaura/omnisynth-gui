from kivy.uix.slider import Slider
from kivy.properties import BooleanProperty, NumericProperty, StringProperty

from kivy.app import App


class OmniSlider(Slider):
    knob_name = StringProperty()
    hold_value = NumericProperty()
    prev_value = NumericProperty()
    disabled = BooleanProperty()
    update_slider_on = BooleanProperty()

    def on_touch_move(self, touch):
        if self.collide_point(*touch.pos):
            app = App.get_running_app()
            omni = app.root.omni_instance
            knob_coords = app.root.knob_coords

            self.update_slider_on = False
            self.value_pos = touch.pos
            self.hold_value = self.value
            self.hold_value = max(0, min(self.hold_value, 127))
            self.value = self.hold_value
            if self.knob_name in knob_coords:
                self.prev_val = omni.knob_table[
                    knob_coords[self.knob_name]]
                omni.filter_sel(
                    self.knob_name, self.value)
