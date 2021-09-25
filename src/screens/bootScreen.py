from omniapp import ScreenManager
from screens.baseScreen import BaseScreen
from kivy.clock import Clock

# The screen that is shown on boot
# Right now, we just wait half a second
# and switch to the main screen;
# however, we can extend this in the future
# to support pre-loading any assets we need before
# we boot into the GUI.
class BootScreen(BaseScreen):
    def on_enter(self):
        Clock.schedule_once(self.changeToMain,0.5)
    def changeToMain(self):
        ScreenManager.current = 'MainGUI'