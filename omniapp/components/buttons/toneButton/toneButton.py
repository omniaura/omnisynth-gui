from kivy.uix.button import Button
from kivy.properties import ObjectProperty

from omniapp.constants import OMNISYNTH_PATH

from kivy.app import App


class ToneButton(Button):
    def on_touch_down(self, touch):
        app = App.get_running_app()
        omni = app.root.omni_instance
        if self.collide_point(*touch.pos):
            omni.synth_sel(self.text, OMNISYNTH_PATH)
            omni.patchIndex = omni.patchListIndex[
                self.text]
            self.background_color = [0, 85, 255, 1]
            if touch.is_double_tap:
                app.root.current = 'knob_val_screen'

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            self.background_color = [1, 1, 1, 1]
