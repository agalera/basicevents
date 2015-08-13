from basicevents import subscribe, send
import signal
import sys


def signal_handler(signal, frame):
        print('You pressed Ctrl+C!')
        send("STOP")
        sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)


@subscribe("Hello1")
def print_message(*args, **kwargs):
    print "Example function1", args, kwargs


@subscribe("Hello2")
def print_message2(*args, **kwargs):
    import time
    time.sleep(4)
    print "Example function2", args, kwargs


@subscribe("STOP")
def dead_mainthread(*args, **kwargs):
    print "dead MainThread!"

send("Hello1", text_example="normal run")
send("Hello2", text_example="new thread", runtype='thread')
send("Hello3", text_example="normal run", runtype="queue")
send("Hello4", text_example="blocking", runtype='blocking')
print "Finish send all events"
print "waiting stop"
