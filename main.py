# main.py
#
# Responsible for:
# Initializing Kivy config
# Initializing new OmniSynth instance
# Initializing global parameters such as patch / pattern list, and knob coordinates
# Creating a new instance of OmniApp and running it.

from omniapp.omniapp import OmniApp
import subprocess
from omniapp.constants import OMNISYNTH_PATH
from omniapp.scdMatrix import SCDMatrix, SCDType
import numpy as np
from omnisynth import omni
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label

from kivy.config import Config

# Initialize Kivy config
Config.set('kivy', 'keyboard_mode', 'system')
Config.set('postproc', 'double_tap_time', '800')

# initialize omnisynth instance
OmniSynth = omni.Omni()

# Compile all synthDefs and select first patch
sc_main = OMNISYNTH_PATH + "dsp/main.scd"
subprocess.Popen(["sclang", sc_main])
OmniSynth.sc_compile("patches", OMNISYNTH_PATH) # compiles all synthDefs.
OmniSynth.synth_sel("tone1", OMNISYNTH_PATH) # selects first patch.

# Initialize slot UI elements
Slots = [
  Label(size_hint = [1,0.33], color = [1,1,50,1]),
  Label(size_hint = [1,0.33], color = [0, 85, 255, 1]),
  Label(size_hint = [1,0.33], color = [1,1,50,1]),
]

# initialize knob coords
KnobCoords = dict()

# initialize SCDMatrix classes for patches and patterns
PatchMatrix = SCDMatrix(SCDType.patch).get_matrix()
PatchList = np.array(PatchMatrix).flatten()
PatternMatrix = SCDMatrix(SCDType.pattern).get_matrix()
PatternList = np.array(PatternMatrix).flatten()

# Create waveform plot
plt.plot([1, 23, 2, 4])
plt.title('WaveForm')
plt.ylabel('yLabel')
plt.xlabel('xLabel')

# Extending FigureCanvasKivyAgg for MatPlotLib
class WaveForm(FigureCanvasKivyAgg):
    def __init__(self, **kwargs):
        super(WaveForm, self).__init__(plt.gcf(), **kwargs)

# Creating the parent class for the screens and
# defining the functions they will need to share
class BaseScreen(Screen):
    def screenSel(self, screenName):
        ScreenManager.current = screenName
    def toneSel(self, tone):
        OmniSynth.synth_sel(tone, OMNISYNTH_PATH)
    def exitSel(self):
        OmniSynth.exit_sel()
        exit()
    
# Run our app
if __name__ == "__main__":
    OmniApp().run()
