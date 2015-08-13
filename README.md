# BasicEvents
python basic events send non-blocking

## Install

```bash
pip install basicevents
```

Link pypi: https://pypi.python.org/pypi/basicevents


## Example

```python
# recommeded check all examples
from basicevents import subscribe, send

@subscribe("pepito")
def example(*args, **kwargs):
    print "recv signal, values:", args, kwargs

# add to queue signals (non-blocking)
send("pepito", 1, 2, 3, example="added queue")

# add to queue signals (non-blocking)
send("pepito", 1, 2, 3, example="added queue", runtype='queue')

# create new thread for this request (non-blocking)
send("pepito", 1, 2, 3, example="new thread", runtype='thread')

# This is blocking
send("pepito", 1, 2, 3, example="blocking", runtype='blocking')
```

## Documentation
### Functions
Only two functions!

@subscribe(name_event)
With this decorator you can subscribe to all events that are sent to name_event.

send(name_event, *args, **kwargs)
If caught in a parameter called instant in kwargs with True call is placed in a new thread.

* Note: Currently running as thread to allow sharing of memory, if you want an event to use more CPU (cores), you can run processes within the event.

### Attributes events
- events.subs

return:
```python
{'juanito': [<function __main__.example2>],
 'pepito': [<function __main__.example>]}
```

- events.queue

return queue

queue is processed automatically and do not need to access this attribute, but if you want you can use https://docs.python.org/2/library/queue.html

- events.timeout

return int

It is the timeout of the get request queue.
When it reaches the timeout check the MainThread is alive, if so wait to get back, if not, it sends a signal to the EventThread.
You can modify it if you wish.
```python
from basicevents import events
events.timeout = 1
```
