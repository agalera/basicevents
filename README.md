# BasicEvents
python basic events non-blocking

## Install
pip install basicevents

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
    send("pepito", 1, 2, 3, pepe="pepe mola")
    # create new thread for this request (non-blocking) not removing key instant
    send("pepito", 1, 2, 3, pepe="pepe mola in other thread", instant=True)

bla_bla()
```
