import numpy as np
import os
import csv
from Comtrade import Comtrade
from scipy.io.wavfile import write

class CreateWaveComtrade:

    def __init__(self,filepath,sampleRate):
        super(CreateWaveComtrade, self).__init__()
        self.filepath = filepath
        # if channelSelection is None:
        #     channelSelection = 1
        if sampleRate is None:
            sampleRate = 9600
        # self.channelSelection = channelSelection
        self.sampleRate = sampleRate

        with open(self.filepath, encoding='utf-8') as csvfile:
            data = list(csv.reader(csvfile, delimiter=',', skipinitialspace=True))


        # TODO: automagically get number of channels
        for i in range(8):
            channel = []

            for row in data:
                channel.append(row[i+3])

            npChannel = np.array(channel, dtype=np.int16)

            waveFileName = 'Wavefiles/channel{}.wav'.format(i+1)
            write(waveFileName, self.sampleRate, npChannel.astype(np.int16))