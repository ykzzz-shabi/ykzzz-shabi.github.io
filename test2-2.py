from thinkdsp import TriangleSignal
from thinkdsp import decorate
import matplotlib.pyplot as plt
import numpy as np
#三角波
signal = TriangleSignal(200)
duration = signal.period*3
segment = signal.make_wave(duration, framerate=10000)
plt.subplot(3,2,1)
segment.plot()
decorate(xlabel='Time (s)')
wave = signal.make_wave(duration=0.5, framerate=10000)
spectrum = wave.make_spectrum()
plt.subplot(3,2,2)
spectrum.plot()
decorate(xlabel='Frequency (Hz)')

#方波
from thinkdsp import SquareSignal

signal = SquareSignal(200)
duration = signal.period*3
segment = signal.make_wave(duration, framerate=10000)
plt.subplot(3,2,3)
segment.plot()
decorate(xlabel='Time (s)')
wave = signal.make_wave(duration=0.5, framerate=10000)
spectrum = wave.make_spectrum()
plt.subplot(3,2,4)
spectrum.plot()
decorate(xlabel='Frequency (Hz)')

#sawtoothSignal类
from thinkdsp import Sinusoid
from thinkdsp import normalize, unbias

class SawtoothSignal(Sinusoid):
    def evaluate(self, ts):
        cycles = self.freq * ts + self.offset / np.pi / 2
        frac, _ = np.modf(cycles)
        ys = normalize(unbias(frac), self.amp)
        return ys



signal = SawtoothSignal(200)
duration = signal.period*3
segment = signal.make_wave(duration, framerate=10000)
plt.subplot(3,2,5)
segment.plot()
decorate(xlabel='Time (s)')
wave = signal.make_wave(duration=0.5, framerate=10000)
spectrum = wave.make_spectrum()
plt.subplot(3,2,6)
spectrum.plot()
decorate(xlabel='Frequency (Hz)')


plt.show()