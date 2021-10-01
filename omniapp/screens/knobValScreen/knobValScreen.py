# Defining all the screens for ScreenManager
from components.buttons.SlideButton import SlideButton
from components.sliders.omniSlider import OmniSlider
from components.images.indicatorImage import IndicatorImage
from components.images.knobImage import KnobImage
from omniapp import KnobCoords, OmniSynth

from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import Screen

# The knob value page


class KnobValScreen(Screen):
    def __init__(self):
        super().__init__()
        # # self.slideList = []
        # # self.buttonList = []

        # # # "Master" layout of patch screen, will likely change to grid later
        self.layout = BoxLayout(orientation='horizontal',
                                size_hint_y=0.75, pos_hint={'x': 0, 'y': 0.25})

        # # # Columns to group a knob or slider with associated control
        # # lpf_layout = BoxLayout(orientation='vertical', size_hint_x = 0.15, spacing = 25, padding = 25)
        # # hpf_layout = BoxLayout(orientation='vertical', size_hint_x = 0.15, spacing = 25, padding = 25)
        # # attack_layout = BoxLayout(orientation='vertical', size_hint_x = 0.15, spacing = 25, padding = 25)
        # # decay_layout = BoxLayout(orientation='vertical', size_hint_x = 0.15, spacing = 25, padding = 25)
        # # sustain_layout = BoxLayout(orientation='vertical', size_hint_x = 0.15, spacing = 25, padding = 25)
        # # release_layout = BoxLayout(orientation='vertical', size_hint_x = 0.15, spacing = 25, padding = 25)

        # # Knob setup
        # # Each knob set is a layout to allow the indicator image to be placed on top of the knob image
        # lpf_knob_set = RelativeLayout(size_hint_y=0.85)
        # hpf_knob_set = RelativeLayout(size_hint_y=0.85)
        # attack_knob_set = RelativeLayout(size_hint_y=0.85)
        # decay_knob_set = RelativeLayout(size_hint_y=0.85)
        # sustain_knob_set = RelativeLayout(size_hint_y=0.85)
        # release_knob_set = RelativeLayout(size_hint_y=0.85)

        # lpf_knob = KnobImage('lpf')
        # lpf_indicator = IndicatorImage('lpf')
        # lpf_label = Label(text='lpf', size_hint=[1, 0.15])

        # hpf_knob = KnobImage('hpf')
        # hpf_indicator = IndicatorImage('hpf')
        # hpf_label = Label(text='hpf', size_hint=[1, 0.15])

        # attack_knob = KnobImage('attack')
        # attack_indicator = IndicatorImage('attack')
        # attack_label = Label(text='attack', size_hint=[1, 0.15])

        # decay_knob = KnobImage('decay')
        # decay_indicator = IndicatorImage('decay')
        # decay_label = Label(text='decay', size_hint=[1, 0.15])

        # sustain_knob = KnobImage('sustain')
        # sustain_indicator = IndicatorImage('sustain')
        # sustain_label = Label(text='sustain', size_hint=[1, 0.15])

        # release_knob = KnobImage('release')
        # release_indicator = IndicatorImage('release')
        # release_label = Label(text='release', size_hint=[1, 0.15])

        # # Filling the knob sets
        # lpf_knob_set.add_widget(lpf_knob)
        # lpf_knob_set.add_widget(lpf_indicator)
        # hpf_knob_set.add_widget(hpf_knob)
        # hpf_knob_set.add_widget(hpf_indicator)
        # attack_knob_set.add_widget(attack_knob)
        # attack_knob_set.add_widget(attack_indicator)
        # decay_knob_set.add_widget(decay_knob)
        # decay_knob_set.add_widget(decay_indicator)
        # sustain_knob_set.add_widget(sustain_knob)
        # sustain_knob_set.add_widget(sustain_indicator)
        # release_knob_set.add_widget(release_knob)
        # release_knob_set.add_widget(release_indicator)

        # self.add_widget(self.layout)
        self.manager.omni_instance.firstTime = False

    def slideUpdate(self):
        for x in self.layout.children:
            if x.slider_name in KnobCoords:
                current_val = self.manager.omni_instance.omni_instance.knob_table[
                    KnobCoords[x.slider_name]]
    # If the last value recorded by the gui slider movement event is different from the current value,
    # x.value should be set to current_val.
    # However, if the user moves the physical slider/knob and then attempts to set it back to that exact
    # value once again, the value would not be accurately depicted on the GUI.
    # This is why the "and not x.updateSliderOn" must be added
    #            if x.prev_val != current_val:
    #                x.value = current_val
                if x.prev_val != current_val and not x.updateSliderOn:
                    x.updateSliderOn = True
                if x.updateSliderOn:
                    x.value = current_val

    def on_enter(self):
        self.slideEvent = Clock.schedule_interval(self.slideUpdate, 1/60)
        self.manager.omni_instance.midi_learn_on = True
        self.manager.omni_instance.mapMode = False

    def on_pre_leave(self):
        self.slideEvent.cancel()
        self.manager.omni_instance.midi_learn_on = False
        self.manager.omni_instance.mapMode = False

    def learnMidi(self):
        if self.manager.omni_instance.mapMode:
            self.manager.omni_instance.mapMode = False
        else:
            self.manager.omni_instance.mapMode = True