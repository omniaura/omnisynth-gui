from kivy.app import App
from kivy.uix.button import Button
from kivy.properties import StringProperty

from omniapp.constants import OMNISYNTH_PATH

from kivy.app import App


class PatchButton(Button):
    patch_filename = StringProperty()

    def on_touch_down(self, touch):
        app = App.get_running_app()

        if self.collide_point(*touch.pos):
            self.background_color = [0, 85, 255, 1]
            app.root.OmniSynth.set_active_patch(
                self.patch_filename)
            app.root.current = 'knob_val_screen'
