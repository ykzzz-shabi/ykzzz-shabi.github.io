from thinkdsp import Chirp
from thinkdsp import normalize, unbias, decorate
import numpy as np
import matplotlib.pyplot as plt
PI2 = 2 * np.pi

class SawtoothChirp(Chirp):

    def evaluate(self, ts):
        """
        改写evaluate函数
        ts: 时间
        """
        freqs = np.linspace(self.start, self.end, len(ts))
        dts = np.diff(ts, prepend=0)
        dphis = PI2 * freqs * dts
        phases = np.cumsum(dphis)
        cycles = phases / PI2
        frac, _ = np.modf(cycles)
        ys =  normalize(unbias(frac), self.amp)
        return ys

signal = Chirp(start=220, end=440)
wave = signal.make_wave(duration=1)
spectrum = wave.make_spectrum()
plt.subplot(2,1,1)
spectrum.plot(high=700)
decorate(xlabel='Frequency (Hz)')
wave.play("niaojiao.wav")


signal = SawtoothChirp(start=220, end=880)
wave = signal.make_wave(duration=1, framerate=14000)
sp = wave.make_spectrogram(256)
plt.subplot(2,1,2)
sp.plot()
decorate(xlabel='Time (s)', ylabel='Frequency (Hz)')
plt.show()
#wave.play("temp2.wav")
