from __future__ import print_function
import threading
import traceback
from multiprocessing import Queue, Process


class events(object):
    subs = {}
    queue = Queue()
    timeout = 5
    logger = print

    @staticmethod
    def _run_event(event, *args, **kwargs):
        try:
            for func in events.subs[event]:
                try:
                    func(*args, **kwargs)
                except:
                    events.logger(traceback.format_exc())
        except:
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
    for i in threading.enumerate():
        if i.name == "MainThread":
            MainThread = i
            break
    while proccess_queue:
        try:
            args, kwargs = events.queue.get(timeout=events.timeout)
        except:
            # check main thread is alive
            if not MainThread.is_alive():
                send("STOP")
            continue  # pragma: no cover

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
