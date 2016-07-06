from basicevents import (subscribe, send_thread, send_queue,
                         send_blocking, add_subscribe, send,
                         __run_queue, run)
# import unittest
import time
import threading
import unittest


@subscribe("pepito_test")
def example2(*args, **kwargs):
    return True


@subscribe("voluntary_error")
def best_error(*args, **kwargs):
    raise Exception("test")


def stop_new_thread(*args, **kwargs):
    time.sleep(70)
    send("STOP")


def timeout_exception():
    send("STOP")
    time.sleep(10)
    threading.Thread(target=stop_new_thread).start()
    __run_queue()
    threading.Thread(target=__run_queue).start()


def exception_dead_mainthread():
    def fake_is_alive():
        return False

    def modify_isAlive():
        MainThread.is_alive = fake_is_alive
        MainThread.isAlive = fake_is_alive
    for i in threading.enumerate():
        if i.name == "MainThread":
            MainThread = i
            break
    send("STOP")
    time.sleep(5)
    threading.Thread(target=modify_isAlive).start()
    __run_queue()
    threading.Thread(target=__run_queue).start()


class TestMethods(unittest.TestCase):
    def test_exception_in_queue(self):
        send_blocking("voluntary_error")
        self.assertEqual(True, True)

    def test_add_subscribe(self):
        add_subscribe("random", example2)
        self.assertEqual(True, True)

    def test_send(self):
        send("pepito", 1, 2, 3, example="added queue")
        self.assertEqual(True, True)

    def test_send_queue(self):
        # add to queue signals (non-blocking)
        send_queue("pepito", 1, 2, 3, example="added queue")
        self.assertEqual(True, True)

    def test_send_thread(self):
        # create new thread for this request (non-blocking)
        send_thread("pepito", 1, 2, 3, example="new thread")
        self.assertEqual(True, True)

    def test_send_blocking(self):
        # This is blocking
        send_blocking("pepito", 1, 2, 3, example="blocking")
        self.assertEqual(True, True)

if __name__ == '__main__':
    add_subscribe("pepito", example2)
    run()
    timeout_exception()
    # kill brains
    exception_dead_mainthread()
    unittest.main()

