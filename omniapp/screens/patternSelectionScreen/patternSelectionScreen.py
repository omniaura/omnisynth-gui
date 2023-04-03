from kivy.uix.gridlayout import GridLayout

from omniapp.components.buttons.patternButton.patternButton import PatternButton
from omniapp.components.buttons.patternButton.patternButton import PatternButton
from kivy.properties import StringProperty, ListProperty, ObjectProperty, NumericProperty
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen


class PatternSelectionScreen(Screen):
    """
    This screen displays all patterns available
    """

    def on_pre_enter(self):
        self.grid = GridLayout(size_hint=[0.8, 0.87], pos_hint={'x': 0.1, 'y': 0}, size_hint_y=None,
                               cols=4, spacing=[2, 2], padding=[0, 0, 0, 30])

        patterns = self.manager.OmniSynth.osc_interface.patch_collection.patterns

        for pattern in pattern:
            self.grid.add_widget(PatternButton(
                text=pattern.name, pattern_filename=pattern.filename, size_hint=[1, 0.25]))

        self.add_widget(self.grid)
