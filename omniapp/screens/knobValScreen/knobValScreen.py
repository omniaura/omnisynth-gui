from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import Screen
from kivy.properties import ListProperty, ObjectProperty
from . components.omniSlider.omniSlider import OmniSlider
from . components.slideButton.slideButton import SlideButton
from omniapp.components.layouts.controlGroup.controlGroup import ControlGroup
from omnisynth import omni

# The knob value page


class KnobValScreen(Screen):
    sliders = ListProperty()
    page_layout = ObjectProperty()

    def on_pre_enter(self):
        # remove previous knob layout from screen
        if self.page_layout != None:
            self.remove_widget(self.page_layout)

        # erase previous sliders
        self.sliders = []

        # create new page layout to be filled with knobs
        self.page_layout = BoxLayout(
            size_hint_y=0.75, pos_hint={'x': 0, 'y': 0.25}, orientation='horizontal')

        current_patch_params = list(
            self.manager.OmniSynth.active_patch().params)

        # Screen is a group of ControlGroups, which are groups of controls (aka knobs)
        # so lets add our knobs from our current patch params

        for knob_name in current_patch_params:
            slider = OmniSlider(knob_name=knob_name)
            button = SlideButton(text=knob_name)
            control_group = ControlGroup()
            control_group.add_widget(slider)
            control_group.add_widget(button)
            self.page_layout.add_widget(control_group)
            self.sliders.append(slider)

        # add the knob layout to the screen
        self.add_widget(self.page_layout)

    def slide_update(self, dt):
        active_patch = self.manager.OmniSynth.active_patch()
        for x in self.sliders:
            # print(f'Value of {x.knob_name}:')
            # print(active_patch.params[x.knob_name])
            param_midi_value = int(omni.ValueConverter.to_midi_value(
                x.knob_name, active_patch.params[x.knob_name]))
            # If the last value recorded by the gui slider movement event is different from the current value,
            # x.value should be set to current_val.
            # However, if the user moves the physical slider/knob and then attempts to set it back to that exact
            # value once again, the value would not be accurately depicted on the GUI.
            # This is why the "and not x.updateSliderOn" must be added
            #            if x.prev_val != current_val:
            #                x.value = current_val
            if x.prev_value != param_midi_value:
                x.prev_value = param_midi_value
                x.value = param_midi_value

    def on_enter(self):
        self.slide_event = Clock.schedule_interval(self.slide_update, 1/60)
        self.manager.OmniSynth.set_midi_learn(True)
        self.manager.midi_map_mode_on = False

    def on_pre_leave(self):
        self.slide_event.cancel()
        self.manager.OmniSynth.set_midi_learn(False)
        self.manager.midi_map_mode_on = False

    def learn_midi(self):
        self.manager.midi_map_mode_on = not self.manager.midi_map_mode_on
        self.text = str(self.manager.midi_map_mode_on)
