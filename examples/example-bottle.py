from bottle import get, run
from basicevents import (subscribe, send, send_thread,
                         send_blocking, send_queue)
import time


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
    send("Hello1", text_example="run normal")
    return "send signal ok, time ", str(time.time() - t1)


@get('/test2')
def test2():
    t1 = time.time()
    send_queue("Hello1", text_example="run normal", runtype='queue')
    return "send signal ok, time ", str(time.time() - t1)


@get('/test3')
def test3():
    t1 = time.time()
    send_blocking("Hello1", text_example="blocking", runtype='blocking')
    return "send signal ok, time ", str(time.time() - t1)


@get('/test4')
def test4():
    t1 = time.time()
    send_thread("Hello2", text_example="instant", runtype='thread')
    return "send signal ok, time ", str(time.time() - t1)

run(host='localhost', port=8080)
