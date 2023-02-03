# Defining all the screens for ScreenManager
from omniapp.constants import OMNISYNTH_PATH

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.screenmanager import Screen
from kivy.properties import BooleanProperty
from kivy.lang import Builder
from kivy.uix.widget import WidgetException
import os
import time

# The main, landing screen of the app


class MainScreen(Screen):
    def on_pre_enter(self):
        omni = self.manager.omni_instance
        patch_select_list_layout = self.ids['patch_select_list_layout']

        # call omni#synth_sel on our current patch
        self.__omni_select_patch()

        # set slot text
        self.__set_slot_text()

        # add slots
        # handle exception if slots have already been added
        # and bail out with a noop
        try:
            patch_select_list_layout.add_widget(self.manager.slots[0])
            patch_select_list_layout.add_widget(self.manager.slots[1])
            patch_select_list_layout.add_widget(self.manager.slots[2])
        except WidgetException:
            pass

    def handle_up_button_release(self):
        if self.manager.omni_instance.patchIndex == 0:
            return

        self.manager.omni_instance.patchIndex -= 1
        self.__omni_select_patch()
        self.__set_slot_text()

    def handle_down_button_release(self):
        if self.manager.omni_instance.patchIndex == (self.manager.omni_instance.numPatch-1):
            return

        self.manager.omni_instance.patchIndex += 1
        self.__omni_select_patch()
        self.__set_slot_text()

    def __get_slot_text(self, patch_index):
        if patch_index >= 0 and patch_index < self.manager.omni_instance.numPatch:
            return str(self.manager.patch_list[patch_index])
        else:
            return ''

    def __set_slot_text(self):
        self.manager.slots[0].text = self.__get_slot_text(
            self.manager.omni_instance.patchIndex - 1)
        self.manager.slots[1].text = self.__get_slot_text(
            self.manager.omni_instance.patchIndex)
        self.manager.slots[2].text = self.__get_slot_text(
            self.manager.omni_instance.patchIndex + 1)

    def __omni_select_patch(self):
        self.manager.omni_instance.synth_sel(
            self.manager.patch_list[self.manager.omni_instance.patchIndex], OMNISYNTH_PATH)
