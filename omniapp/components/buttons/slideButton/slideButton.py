from kivy.uix.button import Button
from kivy.properties import StringProperty


class SlideButton(Button):
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.background_color = [0, 85, 255, 1]
            if self.manager.omni_instance.mapMode:
                if len(self.manager.omni_instance.knob_table) != 0:
                    with self.canvas:
                        self.opacity = 1
                    src = self.manager.omni_instance.control_evnt[2]
                    chan = self.manager.omni_instance.control_evnt[3]
                    self.manager.knob_coords[self.text] = (src, chan)
                    self.manager.omni_instance.map_knob(
                        (src, chan), self.text)

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            self.background_color = [1, 1, 1, 1]
