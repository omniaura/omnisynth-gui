from omniapp import KnobCoords, OmniSynth
from kivy.uix.button import Button


class SlideButton(Button):
    def __init__(self, name):
        super().__init__(text=name, size_hint_x=0.75,
                         size_hint_y=0.1, pos_hint={'x': 0.17, 'y': 0})
        self.button_name = name

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.background_color = [0, 85, 255, 1]
            if App.get_running_app().omni_instance.mapMode:
                if len(App.get_running_app().omni_instance.knob_table) != 0:
                    with self.canvas:
                        self.opacity = 1
                    src = App.get_running_app().omni_instance.control_evnt[2]
                    chan = App.get_running_app().omni_instance.control_evnt[3]
                    KnobCoords[self.button_name] = (src, chan)
                    App.get_running_app().omni_instance.map_knob((src, chan), self.button_name)

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            self.background_color = [1, 1, 1, 1]
