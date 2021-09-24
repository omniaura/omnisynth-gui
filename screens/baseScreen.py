from omniapp import OmniSynth
from constants import OMNISYNTH_PATH
from kivy.uix.screenmanager import ScreenManager, Screen

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
