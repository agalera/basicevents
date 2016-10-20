
[![pythonversions](https://img.shields.io/pypi/pyversions/basicevents.svg)](https://pypi.python.org/pypi/basicevents)
[![Code Climate](https://img.shields.io/codeclimate/github/kianxineki/basicevents.svg)](https://codeclimate.com/github/kianxineki/basicevents)
[![Codecov](https://img.shields.io/codecov/c/github/kianxineki/basicevents.svg)](https://codecov.io/github/kianxineki/basicevents)
[![Travis](https://img.shields.io/travis/kianxineki/basicevents.svg)](https://travis-ci.org/kianxineki/basicevents)
[![License](https://img.shields.io/pypi/l/basicevents.svg)](http://www.gnu.org/licenses/gpl-3.0.txt)

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
from basicevents import (subscribe, send_thread, send_queue,
                         send_blocking, add_subscribe, send, run)

@subscribe("pepito")
def example(*args, **kwargs):
    print "recv signal, values:", args, kwargs

def example2(*args, **kwargs):
    print "manual subscribe"

# manual subscribe
add_subscribe("pepito", example2)

# add to queue signals (non-blocking)
send("pepito", 1, 2, 3, example="added queue")

# add to queue signals (non-blocking)
send_queue("pepito", 1, 2, 3, example="added queue")

# create new thread for this request (non-blocking)
send_thread("pepito", 1, 2, 3, example="new thread")

# This is blocking
send_blocking("pepito", 1, 2, 3, example="blocking")

run()
send("STOP")
```

## Documentation
### Functions

@subscribe(name_event)
With this decorator you can subscribe to all events that are sent to name_event.

manual subscribe
add_subscribe(name_event, function)

- added in queue (non-blocking)

send_queue(name_event, *args, **kwargs)


- run in new thread (non-blocking)

send_thread(name_event, *args, **kwargs)


- run blocking (blocking)

send_blocking(name_event, *args, **kwargs)



* Note: Currently running in individual process.

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

```

- events.logger

return function

You can change the function that is executed when an exception occurs. Uses default print
You can modify it if you wish.
```python
from basicevents import events
events.logger = function
```


- events.send

return function

You can change the function send (It is a link). default is events.send_queue

```python
from basicevents import events
events.send = events.send_blocking # or other functions
```

- these parameters are too, have documented above:

```python
add_subscribe, send, send_queue, send_thread, send_blocking
```
