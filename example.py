from basicevents import subscribe, send


@subscribe("Hello2")
def print_message(*args, **kwargs):
    import time
    time.sleep(4)
    print "Example function", args, kwargs


send("Hello2", text_example="normal run")
send("Hello2", text_example="instant", instant=True)
send("STOP")

print "Finish send all events"
