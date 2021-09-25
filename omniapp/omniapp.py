from omniapp.constants import OMNISYNTH_PATH

from kivy.app import App

from omniapp.omnigui import OmniGui
from kivy.uix.screenmanager import NoTransition

from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen


# The screen that is shown on boot
# Right now, we just wait half a second
# and switch to the main screen;
# however, we can extend this in the future
# to support pre-loading any assets we need before
# we boot into the GUI.
class BootScreen(Screen):
    screenmanager = ObjectProperty()

    def on_enter(self):
        Clock.schedule_once(self.changeToMain ,0.5)

    def changeToMain(self):
      self.screenmanager.current = 'MainGUI'

# The Kivy App that controls our processs
class OmniApp(App):
    def build(self):
        # initialize screen manager
        sm = OmniGui(transition=NoTransition())
        sm.add_widget(BootScreen(name='BootScreen'))

        return sm

    def build_config(self, config):
        config.setdefaults('example', {
            'boolexample': True,
            'numericexample': 10,
            'optionsexample': 'option2',
            'stringexample': 'some_string',
            'pathexample': '/some/path'})

    def build_settings(self, settings):
        settings.add_json_panel('Settings Template', self.config, filename = OMNISYNTH_PATH + '/gui/settings.json')

    def on_config_change(self, config, section, key, value):
        print(config, section, key, value)