from __future__ import print_function
import threading
import traceback
from multiprocessing import Queue, Process


class Events(object):
    subs = {}
    queue = Queue()
    logger = print

    @staticmethod
    def _run_event(event, *args, **kwargs):
        try:
            for func in Events.subs[event]:
                print("iter subs", func)
                try:
                    print("init func")
                    func(*args, **kwargs)
                    print("end func")
                except:
                    print("esto peta")
                    Events.logger(traceback.format_exc())
        except:
            print("peta mucho")
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


def __run_queue():
    proccess_queue = True
    while proccess_queue:
        args, kwargs = Events.queue.get()
        Events._run_event(*args, **kwargs)
        if args[0] == "STOP":
            proccess_queue = False


def run():
    Process(target=__run_queue).start()


# deprecated
events = Events

# avoids having to import Events
add_subscribe = Events.add_subscribe
subscribe = Events.subscribe
send = Events.send
send_queue = Events.send_queue
send_thread = Events.send_thread
send_blocking = Events.send_blocking
