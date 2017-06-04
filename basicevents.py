from __future__ import print_function
import threading
import traceback
from time import sleep
from multiprocessing import Queue, Process
import signal


class Events(object):
    subs = {}
    queue = Queue()
    logger = print

    @staticmethod
    def _run_event(event, *args, **kwargs):
        try:
            for func in Events.subs[event]:
                try:
                    func(*args, **kwargs)
                except:
                    Events.logger(traceback.format_exc())
        except:
            pass

    @staticmethod
    def add_subscribe(event, func):
        if event not in Events.subs:
            Events.subs[event] = []
        Events.subs[event].append(func)

    @staticmethod
    def subscribe(event):
        def wrap_function(func):
            Events.add_subscribe(event, func)
            return func
        return wrap_function

    @staticmethod
    def send_queue(*args, **kwargs):
        Events.queue.put((args, kwargs))

    @staticmethod
    def send_thread(*args, **kwargs):
        threading.Thread(target=Events._run_event,
                         args=args, kwargs=kwargs).start()

    @staticmethod
    def send_blocking(*args, **kwargs):
        Events._run_event(*args, **kwargs)

    # default send
    send = send_queue


def __run_queue(stop_function=lambda: True):
    proccess_queue = True

    def signal_handler(signal, frame):
        def waiting_dead(stop_function):
            while True:
                if stop_function():
                    print("send stop")
                    send("STOP")
                    break
                else:
                    sleep(2)
        print('basicevent stopping')
        Process(target=waiting_dead, args=(stop_function,)).start()

    signal.signal(signal.SIGINT, signal_handler)
    # os.setpgrp()  # kill non propagate
    while proccess_queue:
        args, kwargs = Events.queue.get()

        if args[0] == "STOP":
            proccess_queue = False
            Events.logger("basicevent stopped")
        else:
            Events._run_event(*args, **kwargs)
        Events.queue.task_done()


def run(stop_function=lambda: True):
    Process(target=__run_queue, args=(stop_function,)).start()


# deprecated
events = Events

# avoids having to import Events
add_subscribe = Events.add_subscribe
subscribe = Events.subscribe
send = Events.send
send_queue = Events.send_queue
send_thread = Events.send_thread
send_blocking = Events.send_blocking
