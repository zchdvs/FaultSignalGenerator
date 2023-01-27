from . import Comtrade

def test():
    rec = Comtrade.Comtrade()
    rec.load(r"C:\Users\zachd\Documents\GitHub\FaultSignalGenerator\WebGui\FastAPI Backend\routers\FSGFunctions\sample-comtrade\example 11.cfg", r"C:\Users\zachd\Documents\GitHub\FaultSignalGenerator\WebGui\FastAPI Backend\routers\FSGFunctions\sample-comtrade\example 11.dat")
    channels = []
    for channel in rec.analog:
        channels.append(channel.tolist())
    return channels
