# Defining all the screens for ScreenManager
from omniapp import OmniSynth, PatchList, PatchMatrix, Slots
from constants import OMNISYNTH_PATH
from components.buttons.downButton import DownButton
from components.buttons.upButton import UpButton
from main import BaseScreen

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout

# The main, landing screen of the app


class MainScreen(BaseScreen):
    def __init__(self):
        super().__init__()
        self.firstTime = True

    def on_pre_enter(self):
        App.get_running_app().omni_instance.numPatch = len(PatchList)
        if self.firstTime:
            App.get_running_app().omni_instance.patchIndex = 0
            if App.get_running_app().omni_instance.numPatch > 1:
                Slots[1].text = str(PatchMatrix[0][0])
                Slots[2].text = str(PatchMatrix[0][1])
            else:
                if App.get_running_app().omni_instance.numPatch == 1:
                    Slots[1].text = str(PatchMatrix[0][0])
            self.patchSelectListLayout.add_widget(Slots[0])
            self.patchSelectListLayout.add_widget(Slots[1])
            self.patchSelectListLayout.add_widget(Slots[2])
            self.firstTime = False
            App.get_running_app().omni_instance.synth_sel(
                Slots[1].text, OMNISYNTH_PATH)
        else:
            if App.get_running_app().omni_instance.patchIndex == 0:
                Slots[0].text = ''
                Slots[1].text = PatchList[0]
                Slots[2].text = PatchList[1]
                App.get_running_app().omni_instance.synth_sel(
                    Slots[1].text, OMNISYNTH_PATH)
            else:
                if App.get_running_app().omni_instance.patchIndex == App.get_running_app().omni_instance.numPatch-1:
                    Slots[0].text = PatchList[App.get_running_app(
                    ).omni_instance.patchIndex - 1]
                    Slots[1].text = PatchList[App.get_running_app(
                    ).omni_instance.patchIndex]
                    Slots[2].text = ''
                    App.get_running_app().omni_instance.synth_sel(
                        Slots[1].text, OMNISYNTH_PATH)
                else:
                    Slots[0].text = PatchList[App.get_running_app(
                    ).omni_instance.patchIndex - 1]
                    Slots[1].text = PatchList[App.get_running_app(
                    ).omni_instance.patchIndex]
                    Slots[2].text = PatchList[App.get_running_app(
                    ).omni_instance.patchIndex + 1]
                    App.get_running_app().omni_instance.synth_sel(
                        Slots[1].text, OMNISYNTH_PATH)
