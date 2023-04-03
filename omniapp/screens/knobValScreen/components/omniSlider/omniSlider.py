from kivy.uix.slider import Slider
from kivy.properties import BooleanProperty, NumericProperty, StringProperty

from kivy.app import App


class OmniSlider(Slider):
    knob_name = StringProperty()
    hold_value = NumericProperty()
    prev_value = NumericProperty()
    update_slider_on = BooleanProperty()

    def on_touch_move(self, touch):
        app = App.get_running_app()
        if self.collide_point(*touch.pos):
            self.update_slider_on = False
            self.hold_value = self.value
            self.hold_value = max(0, min(self.hold_value, 127))
            self.value = self.hold_value
            app.root.OmniSynth.set_active_patch_param_value(
                self.knob_name, int(self.value))
