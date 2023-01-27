import time
from CreateWave import CreateWaveComtrade
from PlayWave import WavePlayerLoop
from Comtrade import Comtrade
from PlaySine import PlaySine

class ComtradeMain():

    def wave(filePath, sampleRate):
        CreateWaveComtrade(filePath, sampleRate)

    def playWave(channel, timer):
        waveFile = 'Wavefiles/channel{}.wav'.format(channel)
        player = WavePlayerLoop(waveFile)
        player.play()
        time.sleep(timer)
        player.stop()

    def playSine(frequency, samplingRate, duration, amplitude): #amplitude from 0.0 to 1.0
        PlaySine.play(frequency, samplingRate, duration, amplitude)

    def comtradeToDict(cfg_file_Path,dat_file_path):
        rec = Comtrade()
        rec.load(cfg_file_Path,dat_file_path)
        comtradeDic = {}
        comtradeDic['frequency'] = rec.frequency
        comtradeDic['time_base'] = rec.time_base
        comtradeDic['analog_count'] = rec.analog_count
        comtradeDic['digital_count'] = rec.status_count
        comtradeDic['sample_rates']= rec._cfg.sample_rates
        analogDict = dict(map(lambda i,j : (i,j) , rec.analog_channel_ids,rec._analog_values))
        digitalDict = dict(map(lambda i,j : (i,j) , rec.status_channel_ids,rec._status_values))
        comtradeDic['analog'] = analogDict
        comtradeDic['digital'] = digitalDict
        return comtradeDic



### Testing ###
    # print(comtradeToDict("sample-comtrade/example 11.cfg", "sample-comtrade/example 11.dat"))

    # wave('sample-comtrade/example 12.dat', 9600) # enter .dat file location, and samplerate
    # time.sleep(2) # sleep time so there's time to create wave files before playWave runs.
    # playWave(4, 10) # enter the channel # you want to play, and how long (in secs) to play it.

    # playSine(200, 44100, 5, .1) # sine frequency, samplerate, duration, volume (not sure volume does anything).