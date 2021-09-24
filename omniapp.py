from scdMatrix import SCDMatrix, SCDType
from constants import OMNISYNTH_PATH
import subprocess
import numpy as np
import omnisynth as omni

from kivy.app import App

from omnigui import OmniGui
from kivy.uix.screenmanager import NoTransition
from kivy.uix.label import Label

# initialize screen manager
ScreenManager = OmniGui(transition=NoTransition())

# initialize omnisynth instance
OmniSynth = omni.Omni()

# initialize slider and slot UI elements
updateSliderOn = True

Slots = [
  Label(size_hint = [1,0.33], color = [1,1,50,1]),
  Label(size_hint = [1,0.33], color = [0, 85, 255, 1]),
  Label(size_hint = [1,0.33], color = [1,1,50,1]),
]

# initialize knob coords
KnobCoords = dict()

# initialize patch and pattern matrices
# initialize SCDMatrix classes for patches and patterns
PatchMatrix = SCDMatrix(SCDType.patch).get_matrix()
PatchList = np.array(PatchMatrix).flatten()
PatternMatrix = SCDMatrix(SCDType.patttern).get_matrix()
PatternList = np.array(PatternMatrix).flatten()



class OmniApp(App):
    def build(self):
        # Compile all synthDefs and select first patch
        sc_main = OMNISYNTH_PATH + "dsp/main.scd"
        subprocess.Popen(["sclang", sc_main])
        OmniSynth.sc_compile("patches", OMNISYNTH_PATH) # compiles all synthDefs.
        OmniSynth.synth_sel("tone1", OMNISYNTH_PATH) # selects first patch.

    def build_config(self, config):
        config.setdefaults('example', {
            'boolexample': True,
            'numericexample': 10,
            'optionsexample': 'option2',
            'stringexample': 'some_string',
            'pathexample': '/some/path'})
    def build_settings(self, settings):
        settings.add_json_panel('Settings Template', self.config, filename = OMNISYNTH_PATH + '/gui/settings.json')

    def on_config_change(self, config, section, key, value):
        print(config, section, key, value)