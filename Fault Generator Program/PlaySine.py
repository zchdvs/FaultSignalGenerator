import time

import numpy as np
import pyaudio

class PlaySine:

    def play(frequency, samplingRate, duration, amplitude):
        p = pyaudio.PyAudio()

        volume = amplitude  # range [0.0, 1.0]
        fs = samplingRate  # sampling rate, Hz, must be integer
        duration = duration  # in seconds, may be float
        f = frequency  # sine frequency, Hz, may be float

        # generate samples, note conversion to float32 array
        samples = (np.sin(2 * np.pi * np.arange(fs * duration) * f / fs)).astype(np.float32)

        # per @yahweh comment explicitly convert to bytes sequence
        output_bytes = (volume * samples).tobytes()

        # for paFloat32 sample values must be in range [-1.0, 1.0]
        stream = p.open(format=pyaudio.paFloat32,
                        channels=1,
                        rate=fs,
                        output=True)

        # play. May repeat with different volume values (if done interactively)
        stream.write(output_bytes)

        stream.stop_stream()
        stream.close()

        p.terminate()