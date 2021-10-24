from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import Screen
from kivy.properties import ListProperty
from . components.omniSlider.omniSlider import OmniSlider
from . components.slideButton.slideButton import SlideButton
from omniapp.components.layouts.controlGroup.controlGroup import ControlGroup

DEFAULT_CONTROL_GROUPS = [
    'LPF', 'HPF', 'Attack', 'Decay', 'Sustain', 'Release',
]

# The knob value page


class KnobValScreen(Screen):
    sliders = ListProperty()

    def on_pre_enter(self):
        page_layout = BoxLayout(
            size_hint_y=0.75, pos_hint={'x': 0, 'y': 0.25}, orientation='horizontal')

        self.manager.logger.log('Current patches and their params (dict):')
        for k, v in self.manager.omni_instance.sc.patch_param_table.items():
            self.manager.logger.log(
                f'(Synth, param num): ${v}; [param_name, default_value]: ${v}')
        # Screen is a group of ControlGroups.
        #
        # Add our default control groups
        for knob_name in DEFAULT_CONTROL_GROUPS:
            slider = OmniSlider(knob_name=knob_name)
            button = SlideButton(text=knob_name)
            control_group = ControlGroup()
            control_group.add_widget(slider)
            control_group.add_widget(button)
            page_layout.add_widget(control_group)
            self.sliders.append(slider)

        self.add_widget(page_layout)

        self.manager.omni_instance.firstTime = False

    def slide_update(self, dt):
        for x in self.sliders:
            if x.knob_name in self.manager.knob_coords:
                current_val = self.manager.omni_instance.omni_instance.knob_table[
                    self.manager.knob_coords[x.knob_name]]
    # If the last value recorded by the gui slider movement event is different from the current value,
    # x.value should be set to current_val.
    # However, if the user moves the physical slider/knob and then attempts to set it back to that exact
    # value once again, the value would not be accurately depicted on the GUI.
    # This is why the "and not x.updateSliderOn" must be added
    #            if x.prev_val != current_val:
    #                x.value = current_val
                if x.prev_val != current_val and not x.update_slider_on:
                    x.update_slider_on = True
                if x.update_slider_on:
                    x.value = current_val

    def on_enter(self):
        self.slide_event = Clock.schedule_interval(self.slide_update, 1/60)
        self.manager.omni_instance.midi_learn_on = True
        self.manager.omni_instance.mapMode = False

    def on_pre_leave(self):
        self.slide_event.cancel()
        self.manager.omni_instance.midi_learn_on = False
        self.manager.omni_instance.mapMode = False

    def learn_midi(self):
        new_map_mode_value = not self.manager.omni_instance.mapMode
        self.manager.omni_instance.mapMode = new_map_mode_value
        self.text = str(new_map_mode_value)
