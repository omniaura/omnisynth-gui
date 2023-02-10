from kivy.uix.gridlayout import GridLayout

from omniapp.components.buttons.patchButton.patchButton import PatchButton
from omniapp.components.buttons.patternButton.patternButton import PatternButton
from kivy.properties import StringProperty, ListProperty, ObjectProperty, NumericProperty
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen


class PatchSelectionScreen(Screen):
    """
    This screen displays all patches available
    """

    def on_pre_enter(self):
        self.grid = GridLayout(size_hint=[0.8, 0.87], pos_hint={'x': 0.1, 'y': 0}, size_hint_y=None,
                               cols=4, spacing=[2, 2], padding=[0, 0, 0, 30])

        patches = self.manager.OmniSynth.osc_interface.patch_collection.patches

        for patch in patches:
            self.grid.add_widget(PatchButton(
                text=patch.name, patch_filename=patch.filename, size_hint=[1, 0.25]))

        self.add_widget(self.grid)
