from threading import Thread


class events(object):
    import Queue
    subs = {}
    queue = Queue.Queue()

    @classmethod
    def _run_event(cls, event):
        if event[0] not in events.subs:
            return
        for func in events.subs[event[0]]:
            func(*event[1], **event[2])

    def send_queue(queue):
        proccess_queue = True
        while proccess_queue:
            event = queue.get()
            if event[0] == "STOP":
                print "STOP Thread"
                proccess_queue = False
                continue
            events._run_event(event)

    Thread(target=send_queue, args=(queue, )).start()

    @classmethod
    def subscribe(cls, event, func):
        if event not in cls.subs:
            cls.subs[event] = []
        cls.subs[event].append(func)

    @classmethod
    def send(cls, type_event, *args, **kwargs):
        event = (type_event, args, kwargs)
        if "instant" in kwargs and kwargs['instant']:
            Thread(target=cls._run_event,
                   kwargs={'event': event}).start()
        else:
            cls.queue.put(event)


def subscribe(event):
    def wrap_function(*args, **kwargs):
        events.subscribe(event, args[0])
        return args[0]
    return wrap_function


def send(*args, **kwargs):
    return events.send(*args, **kwargs)
