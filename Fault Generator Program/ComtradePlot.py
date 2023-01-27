import matplotlib.pyplot as plt
from comtrade import Comtrade

rec = Comtrade()

rec.load("sample-comtrade/example 11.cfg", "sample-comtrade/example 11.dat")
print("Trigger time = {}s".format(rec.trigger_time))
print(len(rec.analog))
# print(len(rec.analog_channel_ids))
print(len(rec.analog[0]))


plt.figure()
for analogChannel in rec.analog:
    plt.plot(rec.time, analogChannel)


plt.legend(rec.analog_channel_ids)
plt.show()