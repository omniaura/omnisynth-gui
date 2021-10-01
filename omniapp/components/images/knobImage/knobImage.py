from kivy.uix.image import Image
from kivy.properties import StringProperty


class KnobImage(Image):
    knob_name = StringProperty()

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            if self.manager.omni_instance.mapMode:
                if len(self.manager.omni_instance.knob_table) != 0:
                    with self.canvas:
                        self.opacity = 1
                    src = self.manager.omni_instance.control_evnt[2]
                    chan = self.manager.omni_instance.control_evnt[3]
                    self.manager.knob_coords[self.knob_name] = (src, chan)
                    self.manager.omni_instance.map_knob(
                        (src, chan), self.knob_name)
