from basicevents import (subscribe, send_thread, send_queue,
                         send_blocking, add_subscribe, send)


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


def other_example(*args, **kwargs):
    print "manual subscribe"


send_thread("Hello1", text_example="new thread")

send_queue("Hello2", text_example="normal run")
send("Hello2", text_example="normal run")

add_subscribe("Hello3", other_example)
send_blocking("Hello3", text_example="blocking")

print "Finish send all events"
print "waiting stop"
