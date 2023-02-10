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
        omni = self.manager.OmniSynth
        omni.compile_patches("patches", OMNISYNTH_PATH)

        patch_select_list_layout = self.ids['patch_select_list_layout']

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

    def active_patch_index(self):
        return next(
            (idx for idx, patch in enumerate(self.manager.OmniSynth.patch_collection.patches) if patch == self.manager.OmniSynth.active_patch()), -1)

    def handle_up_button_release(self):
        active_index = self.active_patch_index()
        if (active_index > 0):
            new_patch = self.manager.OmniSynth.patch_collection.patches[active_index - 1]
            self.manager.OmniSynth.set_active_patch(new_patch.filename)
            self.__set_slot_text()

    def handle_up_button_release(self):
        active_index = self.active_patch_index()
        if (active_index < self.manager.OmniSynth.patch_collection.patch_count()):
            new_patch = self.manager.OmniSynth.patch_collection.patches[active_index + 1]
            self.manager.OmniSynth.set_active_patch(new_patch.filename)
            self.__set_slot_text()

    def __get_slot_text(self, offset):
        patch_index = self.active_patch_index() + offset

        if patch_index >= 0 and patch_index < self.manager.OmniSynth.patch_collection.patch_count():
            patch = self.manager.OmniSynth.patch_collection.patches[patch_index]
            return patch.name
        else:
            return ''

    def __set_slot_text(self):
        self.manager.slots[0].text = self.__get_slot_text(-1)
        self.manager.slots[1].text = self.__get_slot_text(0)
        self.manager.slots[2].text = self.__get_slot_text(1)
