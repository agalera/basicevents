from bottle import get, run
from basicevents import subscribe, send
import time
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


@get('/test1')
def test1():
    t1 = time.time()
    send("Hello1", text_example="instant")
    return "send signal ok, time ", str(time.time() - t1)


@get('/test2')
def test2():
    t1 = time.time()
    send("Hello2", text_example="instant", instant=True)
    return "send signal ok, time ", str(time.time() - t1)

run(host='localhost', port=8080)
