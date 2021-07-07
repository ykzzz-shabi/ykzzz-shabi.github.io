from thinkdsp import Chirp
from thinkdsp import normalize, unbias, decorate,read_wave
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

wave = read_wave('72475__rockwehrmann__glissup02.wav')
wave.make_spectrogram(512).plot(high=5000)
decorate(xlabel='Time (s)', ylabel='Frequency (Hz)')
plt.show()