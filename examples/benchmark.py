from basicevents import subscribe, send, events
import time

@subscribe("speedtest")
def speedtest(*args, **kwargs):
    pass

%timeit send("speedtest", runtype="blocking")

print 'send("speedtest", runtype="thread")'
%timeit send("speedtest", runtype="thread")
time.sleep(4)
print 'send("speedtest", runtype="queue")'
%timeit send("speedtest", runtype="queue")
time.sleep(4)
print 'send("speedtest", runtype="blocking")'
%timeit send("speedtest", runtype="blocking")
time.sleep(4)
print 'speedtest()'
%timeit speedtest()
