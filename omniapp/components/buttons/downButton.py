from omniapp import OmniSynth, PatchList, Slots
from kivy.uix.button import Button

from constants import OMNISYNTH_PATH


class DownButton(Button):
    def on_release(self):
        self.moveDown()

    def moveDown(self):
        if App.get_running_app().omni_instance.patchIndex != (App.get_running_app().omni_instance.numPatch-1):
            Slots[0].text = str(
                PatchList[App.get_running_app().omni_instance.patchIndex])
            App.get_running_app().omni_instance.patchIndex += 1
            Slots[1].text = str(
                PatchList[App.get_running_app().omni_instance.patchIndex])
            if App.get_running_app().omni_instance.patchIndex+1 != App.get_running_app().omni_instance.numPatch:
                Slots[2].text = str(
                    PatchList[App.get_running_app().omni_instance.patchIndex + 1])
            else:
                Slots[2].text = ''
            App.get_running_app().omni_instance.synth_sel(
                Slots[1].text, OMNISYNTH_PATH)
