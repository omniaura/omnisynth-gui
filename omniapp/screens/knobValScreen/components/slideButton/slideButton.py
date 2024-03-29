from kivy.uix.button import Button
from kivy.properties import StringProperty

from kivy.lang import Builder

from kivy.app import App


class SlideButton(Button):
    def on_touch_down(self, touch):
        app = App.get_running_app()
        if self.collide_point(*touch.pos):
            self.background_color = [0, 85, 255, 1]
            if app.root.midi_map_mode_on:
                with self.canvas:
                    self.opacity = 1
                current_control_event = app.root.OmniSynth.current_control_event()
                if current_control_event[0] is not None:
                    app.root.OmniSynth.map_knob(
                        current_control_event[1], current_control_event[2], self.text)

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            self.background_color = [1, 1, 1, 1]
