from omniapp import OmniSynth, PatchList, Slots
from kivy.uix.button import Button

from constants import OMNISYNTH_PATH

class UpButton(Button):
    def on_release(self):
        self.moveUp()

    def moveUp(self):
        if OmniSynth.patchIndex != 0:
            if OmniSynth.patchIndex == 1:
                Slots[0].text = ''
                Slots[1].text = str(PatchList[0])
                Slots[2].text = str(PatchList[1])
                OmniSynth.patchIndex = 0
                OmniSynth.synth_sel(Slots[1].text, OMNISYNTH_PATH)
            else:
                Slots[2].text = str(PatchList[OmniSynth.patchIndex])
                OmniSynth.patchIndex -= 1
                Slots[1].text = str(PatchList[OmniSynth.patchIndex])
                Slots[0].text = str(PatchList[OmniSynth.patchIndex - 1])
                OmniSynth.synth_sel(Slots[1].text, OMNISYNTH_PATH)