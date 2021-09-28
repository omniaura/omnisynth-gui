from omniapp import KnobCoords, OmniSynth
from kivy.uix.image import Image


class KnobImage(Image):
    def __init__(self, name):
        super().__init__(source='../../../assets/knob1.png')
        self.knob_name = name

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            if App.get_running_app().omni_instance.mapMode:
                if len(App.get_running_app().omni_instance.knob_table) != 0:
                    with self.canvas:
                        self.opacity = 1
                    src = App.get_running_app().omni_instance.control_evnt[2]
                    chan = App.get_running_app().omni_instance.control_evnt[3]
                    KnobCoords[self.knob_name] = (src, chan)
                    App.get_running_app().omni_instance.map_knob((src, chan), self.knob_name)
