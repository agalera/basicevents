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

def bla_bla():
    # much code
    # add to queue signals (non-blocking)
    send("pepito", 1, 2, 3, example="added queue")
    # create new thread for this request (non-blocking) not removing key instant
    send("pepito", 1, 2, 3, example="new thread", instant=True)

bla_bla()
```

## Documentation functions
Only two functions!

@subscribe(name_event)
With this decorator you can subscribe to all events that are sent to name_event

send(name_event, *args, **kwargs)
If caught in a parameter called instant in kwargs with True call is placed in a new thread

* Note: Currently running as thread to allow sharing of memory, if you want an event to use more CPU (cores), you can run processes within the event.

