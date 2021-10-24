from kivy.uix.button import Button
from kivy.properties import StringProperty

from kivy.lang import Builder

from kivy.app import App


class SlideButton(Button):
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            app = App.get_running_app()
            omni = app.root.omni_instance
            knob_coords = app.root.knob_coords

            self.background_color = [0, 85, 255, 1]
            if omni.mapMode:
                if len(omni.knob_table) != 0:
                    with self.canvas:
                        self.opacity = 1
                    src = omni.control_evnt[2]
                    chan = omni[3]
                    knob_coords[self.text] = (src, chan)
                    omni.map_knob(
                        (src, chan), self.text)

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            self.background_color = [1, 1, 1, 1]
