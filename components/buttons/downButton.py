from omniapp import OmniSynth, PatchList, Slots
from kivy.uix.button import Button

from constants import OMNISYNTH_PATH

class DownButton(Button):
    def on_release(self):
        self.moveDown()

    def moveDown(self):
        if OmniSynth.patchIndex != (OmniSynth.numPatch-1):
            Slots[0].text = str(PatchList[OmniSynth.patchIndex])
            OmniSynth.patchIndex += 1
            Slots[1].text = str(PatchList[OmniSynth.patchIndex])
            if OmniSynth.patchIndex+1 != OmniSynth.numPatch:
                Slots[2].text = str(PatchList[OmniSynth.patchIndex + 1])
            else:
                Slots[2].text = ''
            OmniSynth.synth_sel(Slots[1].text, OMNISYNTH_PATH)
