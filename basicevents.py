import threading
import traceback
import Queue


class events(object):
    subs = {}
    queue = Queue.Queue()
    timeout = 30


def _run_event(event, *args, **kwargs):
    try:
        for func in events.subs[event]:
            try:
                func(*args, **kwargs)
            except:
                print(traceback.format_exc())
    except:
        pass


def subscribe(event):
    def wrap_function(func):
        if event not in events.subs:
            events.subs[event] = []
        events.subs[event].append(func)
        return func
    return wrap_function


def send(*args, **kwargs):
    """
    runtype: queue, thread or blocking
    """
    if 'runtype' not in kwargs or kwargs['runtype'] == 'queue':
        events.queue.put((args, kwargs))
    elif kwargs['runtype'] == 'thread':
        del kwargs['runtype']
        threading.Thread(target=_run_event,
                         args=args, kwargs=kwargs).start()
    elif kwargs['runtype'] == 'blocking':
        del kwargs['runtype']
        _run_event(*args, **kwargs)


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
            continue

        _run_event(*args, **kwargs)
        if args[0] == "STOP":
            proccess_queue = False

threading.Thread(target=__run_queue).start()
