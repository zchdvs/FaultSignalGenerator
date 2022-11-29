import matplotlib.pyplot as plt
from comtrade import Comtrade
import wave
import numpy as np
import struct
import sys
import csv
import resampy

from scipy.io.wavfile import write
samplerate = 44100; fs = 100
t = np.linspace(0., 1., samplerate)
amplitude = np.iinfo(np.int16).max
data = amplitude * np.sin(2. * np.pi * fs * t)
write("example2.wav", samplerate, data.astype(np.int16))