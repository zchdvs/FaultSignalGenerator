import matplotlib.pyplot as plt
from Comtrade import Comtrade

rec = Comtrade()
rec.load("sample-comtrade/example 11.cfg", "sample-comtrade/example 11.dat")
print("Trigger time = {}s".format(rec.trigger_time))

plt.figure()
plt.plot(rec.time, rec.analog[0])
plt.plot(rec.time, rec.analog[1])
plt.legend([rec.analog_channel_ids[0], rec.analog_channel_ids[1]])
plt.show()