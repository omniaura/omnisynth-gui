# used for triggering events
from omniapp import ScreenManager
from screens.baseScreen import BaseScreen
from kivy.clock import Clock

class BootScreen(BaseScreen):
    def on_enter(self):
        Clock.schedule_once(self.changeToMain,0.5)
    def changeToMain(self):
        ScreenManager.current = 'MainGUI'