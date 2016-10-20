from __future__ import print_function
import threading
import traceback
from multiprocessing import Queue, Process


class events(object):
    subs = {}
    queue = Queue()
    logger = print

    @staticmethod
    def _run_event(event, *args, **kwargs):
        try:
            for func in events.subs[event]:
                print("iter subs", func)
                try:
                    print("init func")
                    func(*args, **kwargs)
                    print("end func")
                except:
                    print("esto peta")
                    events.logger(traceback.format_exc())
        except:
            print("peta mucho")
            pass

    @staticmethod
    def add_subscribe(event, func):
        if event not in events.subs:
            events.subs[event] = []
        events.subs[event].append(func)

    @staticmethod
    def subscribe(event):
        def wrap_function(func):
            events.add_subscribe(event, func)
            return func
        return wrap_function

    @staticmethod
    def send_queue(*args, **kwargs):
        events.queue.put((args, kwargs))

    @staticmethod
    def send_thread(*args, **kwargs):
        threading.Thread(target=events._run_event,
                         args=args, kwargs=kwargs).start()

    @staticmethod
    def send_blocking(*args, **kwargs):
        events._run_event(*args, **kwargs)

    # default send
    send = send_queue


def __run_queue():
    proccess_queue = True
    while proccess_queue:
        args, kwargs = events.queue.get()
        events._run_event(*args, **kwargs)
        if args[0] == "STOP":
            proccess_queue = False


def run():
    Process(target=__run_queue).start()


# avoids having to import events
add_subscribe = events.add_subscribe
subscribe = events.subscribe
send = events.send
send_queue = events.send_queue
send_thread = events.send_thread
send_blocking = events.send_blocking
