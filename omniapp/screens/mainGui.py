# Defining all the screens for ScreenManager
from omniapp import OmniSynth, PatchList, PatchMatrix, Slots
from constants import OMNISYNTH_PATH
from components.buttons.downButton import DownButton
from components.buttons.upButton import UpButton
from main import BaseScreen

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout

# The main, landing screen of the app
class MainGUI(BaseScreen):
    def __init__(self):
        super().__init__()

        self.topRightCorner = AnchorLayout(anchor_x = 'right', anchor_y = 'top')
        self.patchSelectLayout = BoxLayout(orientation = 'horizontal', size_hint = [0.499,0.395])
        self.patchSelectListLayout = BoxLayout(orientation = 'vertical', size_hint = [0.67,1])
        self.patchSelectInterfaceLayout = BoxLayout(orientation = 'vertical', size_hint = [0.23,1])
        self.firstTime = True
        
        selectUpButton = UpButton(text = 'Up')
        selectDownButton = DownButton(text = 'Down')

        self.patchSelectInterfaceLayout.add_widget(selectUpButton)
        self.patchSelectInterfaceLayout.add_widget(selectDownButton)

        self.patchSelectLayout.add_widget(self.patchSelectListLayout)
        self.patchSelectLayout.add_widget(self.patchSelectInterfaceLayout)
        self.topRightCorner.add_widget(self.patchSelectLayout)
        self.add_widget(self.topRightCorner)

    def on_pre_enter(self):
        OmniSynth.numPatch = len(PatchList)
        if self.firstTime:
            OmniSynth.patchIndex = 0
            if OmniSynth.numPatch > 1:
                Slots[1].text = str(PatchMatrix[0][0])
                Slots[2].text = str(PatchMatrix[0][1])
            else:
                if OmniSynth.numPatch == 1:
                    Slots[1].text = str(PatchMatrix[0][0])
            self.patchSelectListLayout.add_widget(Slots[0])
            self.patchSelectListLayout.add_widget(Slots[1])
            self.patchSelectListLayout.add_widget(Slots[2])
            self.firstTime = False
            OmniSynth.synth_sel(Slots[1].text, OMNISYNTH_PATH)
        else:
            if OmniSynth.patchIndex == 0:
                Slots[0].text = ''
                Slots[1].text = PatchList[0]
                Slots[2].text = PatchList[1]
                OmniSynth.synth_sel(Slots[1].text, OMNISYNTH_PATH)
            else:
                if OmniSynth.patchIndex == OmniSynth.numPatch-1:
                    Slots[0].text = PatchList[OmniSynth.patchIndex - 1]
                    Slots[1].text = PatchList[OmniSynth.patchIndex]
                    Slots[2].text = ''
                    OmniSynth.synth_sel(Slots[1].text, OMNISYNTH_PATH)
                else:
                    Slots[0].text = PatchList[OmniSynth.patchIndex - 1]
                    Slots[1].text = PatchList[OmniSynth.patchIndex]
                    Slots[2].text = PatchList[OmniSynth.patchIndex + 1]
                    OmniSynth.synth_sel(Slots[1].text, OMNISYNTH_PATH)