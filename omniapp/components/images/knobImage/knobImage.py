from kivy.uix.image import Image
from kivy.properties import StringProperty


class KnobImage(Image):
    knob_name = StringProperty()

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            if self.manager.midi_map_mode_on:
                with self.canvas:
                    self.opacity = 1
                src = self.manager.OmniSynth.current_control_event[1]
                chan = self.manager.OmniSynth.current_control_event[2]
                self.manager.OmniSynth.map_knob(
                    src, chan, self.knob_name)
