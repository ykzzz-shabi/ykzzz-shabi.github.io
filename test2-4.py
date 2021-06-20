from thinkdsp import Spectrum, TriangleSignal,SquareSignal
from thinkdsp import decorate
import matplotlib.pyplot as plt
import numpy as np


triangle=TriangleSignal(440).make_wave(duration=0.01)
plt.subplot(2,1,1)
triangle.plot()
decorate(xlabel="time(s)")
spectrum=triangle.make_spectrum()
print(spectrum.hs[0])

spectrum.hs[0] = 100
plt.subplot(2,1,2)
triangle.plot(color="gray")
spectrum.make_wave().plot()
decorate(xlabel='Time(s)')
plt.show()