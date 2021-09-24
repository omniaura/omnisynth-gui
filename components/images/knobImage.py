from omniapp import KnobCoords, OmniSynth
from kivy.uix.image import Image

class KnobImage(Image):
    def __init__(self, name):
        super().__init__()
        self.knob_name = name
  
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            if OmniSynth.mapMode:
                if len(OmniSynth.knob_table) != 0:
                    with self.canvas:
                        self.opacity = 1
                    src = OmniSynth.control_evnt[2]
                    chan = OmniSynth.control_evnt[3]
                    KnobCoords[self.knob_name] = (src, chan)
                    OmniSynth.map_knob((src,chan), self.knob_name)