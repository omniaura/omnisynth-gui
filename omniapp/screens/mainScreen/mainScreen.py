# Defining all the screens for ScreenManager
from omniapp.constants import OMNISYNTH_PATH

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.screenmanager import Screen
from kivy.properties import BooleanProperty

# The main, landing screen of the app


class MainScreen(Screen):
    first_time = BooleanProperty(True)

    def on_pre_enter(self):
        self.manager.omni_instance.numPatch = len(self.manager.patch_list)

        patch_select_list_layout = self.ids.patch_select_list_layout
        if self.first_time:
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
            patch_select_list_layout.add_widget(self.manager.slots[0])
            patch_select_list_layout.add_widget(self.manager.slots[1])
            patch_select_list_layout.add_widget(self.manager.slots[2])
            self.first_time = False
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
