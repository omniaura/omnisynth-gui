from omniapp import OmniSynth, PatchList, Slots
from kivy.uix.button import Button

from constants import OMNISYNTH_PATH


class UpButton(Button):
    def on_release(self):
        self.moveUp()

    def moveUp(self):
        if App.get_running_app().omni_instance.patchIndex != 0:
            if App.get_running_app().omni_instance.patchIndex == 1:
                Slots[0].text = ''
                Slots[1].text = str(PatchList[0])
                Slots[2].text = str(PatchList[1])
                App.get_running_app().omni_instance.patchIndex = 0
                App.get_running_app().omni_instance.synth_sel(
                    Slots[1].text, OMNISYNTH_PATH)
            else:
                Slots[2].text = str(
                    PatchList[App.get_running_app().omni_instance.patchIndex])
                App.get_running_app().omni_instance.patchIndex -= 1
                Slots[1].text = str(
                    PatchList[App.get_running_app().omni_instance.patchIndex])
                Slots[0].text = str(
                    PatchList[App.get_running_app().omni_instance.patchIndex - 1])
                App.get_running_app().omni_instance.synth_sel(
                    Slots[1].text, OMNISYNTH_PATH)
