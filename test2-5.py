from thinkdsp import Spectrum, TriangleSignal,SquareSignal, play_wave
from thinkdsp import decorate
import matplotlib.pyplot as plt
import numpy as np
def filter_spectrum(spectrum):
    spectrum.hs[1:] /= spectrum.fs[1:]
    spectrum.hs[0] = 0

wave = TriangleSignal(freq=440).make_wave(duration=5)
#生成原音频
wave.play("temp3.wav")

spectrum = wave.make_spectrum()
#绘制spectrum图像
spectrum.plot(high=10000, color='gray')
filter_spectrum(spectrum)
spectrum.scale(440)
#生成使用函数修改后的spectrum所绘制的图像
spectrum.plot(high=10000,color='red')
decorate(xlabel='Frequency (Hz)')
#从修改过的spectrum绘制一个波形并生成音频试听
spectrum.make_wave().play("temp4.wav")


plt.show()