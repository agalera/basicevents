import threading
import traceback


class events(object):
    import Queue
    subs = {}
    queue = Queue.Queue()
    timeout = 30

    for i in threading.enumerate():
        if i.name == "MainThread":
            MainThread = i
            break

    @classmethod
    def _run_event(cls, event):
        if event[0] not in events.subs:
            return
        for func in events.subs[event[0]]:
            try:
                func(*event[1], **event[2])
            except:
                print traceback.format_exc()

    @classmethod
    def subscribe(cls, event, func):
        if event not in cls.subs:
            cls.subs[event] = []
        cls.subs[event].append(func)

    @classmethod
    def send(cls, type_event, *args, **kwargs):
        event = (type_event, args, kwargs)
        if "instant" in kwargs and kwargs['instant']:
            threading.Thread(target=cls._run_event,
                             kwargs={'event': event}).start()
        else:
            cls.queue.put(event)


def subscribe(event):
    def wrap_function(func):
        events.subscribe(event, func)
        return func
    return wrap_function


def send(*args, **kwargs):
    return events.send(*args, **kwargs)


def __run_queue():
    proccess_queue = True
    while proccess_queue:
        try:
            event = events.queue.get(timeout=events.timeout)
        except:
            # check main thread is alive
            if not events.MainThread.is_alive():
                print("MainThread dead")
                send("STOP")
            continue

        events._run_event(event)
        if event[0] == "STOP":
            print("STOP Thread")
            proccess_queue = False

threading.Thread(target=__run_queue).start()
