# Defining all the screens for ScreenManager
from omniapp.constants import OMNISYNTH_PATH

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.screenmanager import Screen

# The main, landing screen of the app


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__()
        self.firstTime = True
        self.patchSelectLayout = BoxLayout(
            orientation='horizontal', size_hint=[0.499, 0.395])
        self.patchSelectListLayout = BoxLayout(
            orientation='vertical', size_hint=[0.67, 1])
        self.patchSelectInterfaceLayout = BoxLayout(
            orientation='vertical', size_hint=[0.23, 1])
        self.firstTime = True

        selectUpButton = UpButton(text='Up')
        selectDownButton = DownButton(text='Down')

        self.patchSelectInterfaceLayout.add_widget(selectUpButton)
        self.patchSelectInterfaceLayout.add_widget(selectDownButton)

        self.patchSelectLayout.add_widget(self.patchSelectListLayout)
        self.patchSelectLayout.add_widget(self.patchSelectInterfaceLayout)
        self.topRightCorner.add_widget(self.patchSelectLayout)

    def on_pre_enter(self):
        print(self.manager.patch_list)
        self.manager.omni_instance.numPatch = len(self.manager.patch_list)
        if self.firstTime:
            self.manager.omni_instance.patchIndex = 0
            if self.manager.omni_instance.numPatch > 1:
                self.manager.slots[1].text = str(
                    self.manager.patch_matrix[0][0])
                self.manager.slots[2].text = str(
                    self.manager.patch_matrix[0][1])
            else:
                if self.manager.omni_instance.numPatch == 1:
                    self.manager.slots[1].text = str(
                        self.manager.patch_matrix[0][0])
            self.patchSelectListLayout.add_widget(self.manager.slots[0])
            self.patchSelectListLayout.add_widget(self.manager.slots[1])
            self.patchSelectListLayout.add_widget(self.manager.slots[2])
            self.firstTime = False
            self.manager.omni_instance.synth_sel(
                self.manager.slots[1].text, OMNISYNTH_PATH)
        else:
            if self.manager.omni_instance.patchIndex == 0:
                self.manager.slots[0].text = ''
                self.manager.slots[1].text = self.manager.patch_list[0]
                self.manager.slots[2].text = self.manager.patch_list[1]
                self.manager.omni_instance.synth_sel(
                    self.manager.slots[1].text, OMNISYNTH_PATH)
            else:
                if self.manager.omni_instance.patchIndex == self.manager.omni_instance.numPatch-1:
                    self.manager.slots[0].text = self.manager.patch_list[self.manager.omni_instance.patchIndex - 1]
                    self.manager.slots[1].text = self.manager.patch_list[self.manager.omni_instance.patchIndex]
                    self.manager.slots[2].text = ''
                    self.manager.omni_instance.synth_sel(
                        self.manager.slots[1].text, OMNISYNTH_PATH)
                else:
                    self.manager.slots[0].text = self.manager.patch_list[self.manager.omni_instance.patchIndex - 1]
                    self.manager.slots[1].text = self.manager.patch_list[self.manager.omni_instance.patchIndex]
                    self.manager.slots[2].text = self.manager.patch_list[self.manager.omni_instance.patchIndex + 1]
                    self.manager.omni_instance.synth_sel(
                        self.manager.slots[1].text, OMNISYNTH_PATH)
