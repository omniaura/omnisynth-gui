from screens.baseScreen import BaseScreen
from kivy.uix.gridlayout import GridLayout

from components.buttons.screenNavButton import ScreenNavButton
from components.toneButton import ToneButton

# A page that supports displaying
# a list of sounds via ToneButtons
# and also supports a navigation button
# to another screen
class SoundPage(BaseScreen):
  def __init__(self, sound_names, next_screen = None):
    super().__init__()

    self.sound_names = sound_names
    self.next_screen = next_screen

  def on_pre_enter(self):
        self.grid = GridLayout(size_hint = [0.8,0.87], pos_hint = {'x':0.1, 'y':0},
                                rows = 3, cols = 4, spacing = [2,2], padding = [0,0,0,30])
        for sound_name in self.sound_names:
            self.grid.add_widget(ToneButton(text=sound_name, size_hint = [1,0.25]))
        if self.next_screen != None:
            self.add_widget(ScreenNavButton(self.next_screen))
        self.add_widget(self.grid)