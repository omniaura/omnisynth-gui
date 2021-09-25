from omniapp.screens.baseScreen import BaseScreen
from kivy.clock import Clock
from kivy.properties import ObjectProperty

# The screen that is shown on boot
# Right now, we just wait half a second
# and switch to the main screen;
# however, we can extend this in the future
# to support pre-loading any assets we need before
# we boot into the GUI.
class BootScreen(BaseScreen):
    screenmanager = ObjectProperty()

    def on_enter(self):
        Clock.schedule_once(self.screenSel('MainGUI') ,0.5)

    def changeToMain(self):
        self.screenmanager.current = 'MainGUI'