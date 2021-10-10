from kivy.uix.gridlayout import GridLayout

from omniapp.components.buttons.toneButton.toneButton import ToneButton
from kivy.properties import StringProperty, ListProperty, ObjectProperty, NumericProperty
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen


class SoundScreen(Screen):
    """A page that supports displaying
    a list of sounds via ToneButtons
    and also supports nav buttons to next and previous screens
    """

    sound_names = ListProperty()
    prev_screen = StringProperty()
    next_screen = StringProperty()
    page_number = NumericProperty()

    def on_pre_enter(self):
        self.grid = GridLayout(size_hint=[0.8, 0.87], pos_hint={'x': 0.1, 'y': 0},
                               rows=3, cols=4, spacing=[2, 2], padding=[0, 0, 0, 30])
        for sound_name in self.sound_names:
            self.grid.add_widget(ToneButton(
                text=sound_name, size_hint=[1, 0.25]))
        if self.next_screen != '':
            self.add_widget(Button(
                on_release=self.handle_next_button_release(), text='>'))
        if self.prev_screen != '':
            self.add_widget(Button(
                next_screen=self.handle_prev_button_release(), text='<'))

        self.add_widget(self.grid)

    def handle_next_button_release(self):
        self.manager.current = self.next_screen

    def handle_prev_button_release(self):
        self.manager.current = self.prev_screen
