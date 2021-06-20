from thinkdsp import TriangleSignal,SquareSignal
from thinkdsp import decorate
import matplotlib.pyplot as plt
import numpy as np

square = SquareSignal(1100)
cysquare = square.make_wave(duration=2, framerate=10000)
cysquare.play('temp1.wav')
square = square.make_wave(duration=0.5, framerate=10000)
square.make_spectrum().plot()
decorate(xlabel='Frequency (Hz)')

from thinkdsp import SinSignal

sin=SinSignal(500).make_wave(duration=2, framerate=10000)
sin.play('temp2.wav')
plt.show()