# main.py
#
# Creating a new instance of OmniApp and running it.

from omniapp.omniapp import OmniApp
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from kivy.lang import Builder
from pathlib import Path
from itertools import chain
import matplotlib.pyplot as plt
import os

# Create waveform plot
plt.plot([1, 23, 2, 4])
plt.title('WaveForm')
plt.ylabel('yLabel')
plt.xlabel('xLabel')

# Extending FigureCanvasKivyAgg for MatPlotLib


class WaveForm(FigureCanvasKivyAgg):
    def __init__(self, **kwargs):
        super(WaveForm, self).__init__(plt.gcf(), **kwargs)


# Run our app
if __name__ == "__main__":
    OmniApp().run()
