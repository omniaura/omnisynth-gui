#GUI built on the Kivy framework

# config
from constants import OMNISYNTH_PATH
from components.buttons.toneButton import ToneButton
from components.buttons.ledButton import LedButton
from kivy.config import Config
Config.set('kivy', 'keyboard_mode', 'system')
Config.set('postproc', 'double_tap_time', '800')

# Enables referencing to packages in parent directory  #
#   Discovered this method online at codeolives.com    #
########################################################
DIVISOR = 0
from sys import platform
if platform == "linux" or platform == "linux2":
    Window.fullscreen = 'auto'
    DIVISOR = 4
elif platform == "darwin":
    Window.fullscreen = 'auto'
    DIVISOR = 8
elif platform == "win32":
    DIVISOR = 8

from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt

from kivy.core.window import Window

#Creating very simple plot
plt.plot([1, 23, 2, 4])
plt.title('WaveForm')
plt.ylabel('yLabel')
plt.xlabel('xLabel')

# Extending FigureCanvasKivyAgg for MatPlotLib
class WaveForm(FigureCanvasKivyAgg):
    def __init__(self, **kwargs):
        super(WaveForm, self).__init__(plt.gcf(), **kwargs)

class Page2Button(Button):
    def on_release(self, *kwargs):
        sm.current = 'PatchPage2'

class Page3Button(Button):
    def on_release(self, *kwargs):
        sm.current = 'PatchPage3'
        
class Page4Button(Button):
    def on_release(self, *kwargs):
        sm.current = 'PatchPage4'

class PatternPage2Button(Button):
    def on_release(self, *kwargs):
        sm.current = 'LedPage2'

class PatternPage3Button(Button):
    def on_release(self, *kwargs):
        sm.current = 'LedPage3'
        
class PatternPage4Button(Button):
    def on_release(self, *kwargs):
        sm.current = 'LedPage4'

class PatchPage1(MyScreens):
    def on_pre_enter(self):
        self.grid = GridLayout(size_hint = [0.8,0.87], pos_hint = {'x':0.1, 'y':0},
                                rows = 3, cols = 4, spacing = [2,2], padding = [0,0,0,30])
        for pName in patch1to12:
            self.grid.add_widget(ToneButton(text=pName, size_hint = [1,0.25]))
        if len(patch13to24) > 0:
            self.add_widget(Page2Button(text = '>', size_hint = [0.08,0.7], pos_hint = {'x':0.91, 'y':0.15}))
        self.add_widget(self.grid)

class PatchPage2(MyScreens):
    def on_pre_enter(self):
        self.grid = GridLayout(size_hint = [0.8,0.87], pos_hint = {'x':0.1, 'y':0},
                                rows = 3, cols = 4, spacing = [2,2], padding = [0,0,0,30])
        for pName in patch13to24:
            self.grid.add_widget(ToneButton(text=pName, size_hint = [1,0.25]))
        if len(patch25to36) > 0:
            self.add_widget(Page3Button(text = '>', size_hint = [0.08,0.7], pos_hint = {'x':0.91, 'y':0.15}))
        self.add_widget(self.grid)

class PatchPage3(MyScreens):
    def on_pre_enter(self):
        self.grid = GridLayout(size_hint = [0.8,0.87], pos_hint = {'x':0.1, 'y':0},
                                rows = 3, cols = 4, spacing = [2,2], padding = [0,0,0,30])
        for pName in patch25to36:
            self.grid.add_widget(ToneButton(text=pName, size_hint = [1,0.25]))
        if len(patch37to48) > 0:
            self.add_widget(Page4Button(text = '>', size_hint = [0.08,0.7], pos_hint = {'x':0.91, 'y':0.15}))
        self.add_widget(self.grid)

class PatchPage4(MyScreens):
    def on_pre_enter(self):
        self.grid = GridLayout(size_hint = [0.8,0.87], pos_hint = {'x':0.1, 'y':0},
                                rows = 3, cols = 4, spacing = [2,2], padding = [0,0,0,30])
        for pName in patch37to48:
            self.grid.add_widget(ToneButton(text=pName, size_hint = [1,0.25]))
        self.add_widget(self.grid)

class LedPage1(MyScreens):
    def on_pre_enter(self):
        self.grid = GridLayout(size_hint = [0.8,0.87], pos_hint = {'x':0.1, 'y':0},
                                rows = 3, cols = 4, spacing = [2,2], padding = [0,0,0,30])
        for pName in pattern1to12:
            self.grid.add_widget(LedButton(text=pName, size_hint = [1,0.25]))
        if len(pattern13to24) > 0:
            self.add_widget(PatternPage2Button(text = '>', size_hint = [0.08,0.7], pos_hint = {'x':0.91, 'y':0.15}))
        self.add_widget(self.grid)
class LedPage2(MyScreens):
    def on_pre_enter(self):
        self.grid = GridLayout(size_hint = [0.8,0.87], pos_hint = {'x':0.1, 'y':0},
                                rows = 3, cols = 4, spacing = [2,2], padding = [0,0,0,30])
        for pName in pattern13to24:
            self.grid.add_widget(LedButton(text=pName, size_hint = [1,0.25]))
        if len(pattern25to36) > 0:
            self.add_widget(PatternPage3Button(text = '>', size_hint = [0.08,0.7], pos_hint = {'x':0.91, 'y':0.15}))
        self.add_widget(self.grid)
class LedPage3(MyScreens):
    def on_pre_enter(self):
        self.grid = GridLayout(size_hint = [0.8,0.87], pos_hint = {'x':0.1, 'y':0},
                                rows = 3, cols = 4, spacing = [2,2], padding = [0,0,0,30])
        for pName in pattern25to36:
            self.grid.add_widget(LedButton(text=pName, size_hint = [1,0.25]))
        if len(pattern37to48) > 0:
            self.add_widget(PatternPage4Button(text = '>', size_hint = [0.08,0.7], pos_hint = {'x':0.91, 'y':0.15}))
        self.add_widget(self.grid)
class LedPage4(MyScreens):
    def on_pre_enter(self):
        self.grid = GridLayout(size_hint = [0.8,0.87], pos_hint = {'x':0.1, 'y':0},
                                rows = 3, cols = 4, spacing = [2,2], padding = [0,0,0,30])
        for pName in patch37to48:
            self.grid.add_widget(LedButton(text=pName, size_hint = [1,0.25]))
        self.add_widget(self.grid)
class WaveFormPage(MyScreens):
    pass
class MidiLearnPage(MyScreens):
    pass
