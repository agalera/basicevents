# CHANGELOG

## 2.0.12(2017-06-05)
- revert task_done() (not exists in multiprocessing)

## 2.0.11(2017-06-05)
- task_done()

## 2.0.10(2017-04-07)
- graceful stop

## 2.0.9(2017-04-03)
- Fix pip version

## 2.0.8(2017-03-31)
- Fix default argument

## 2.0.7(2017-03-31)
- Support waiting for stop loop

## 2.0.6(2016-10-20)
- events to Events
- correct shutdown

## 2.0.5(2016-10-20)
- events to Events

## 2.0.4(2016-10-20)
- Update document
- Remove old code

## 2.0.3(2016-10-19)
- PEP8

## 2.0.2(2016-09-28)
- It lets you send messages from different processes. (Required to import of basicevents before starting the process)

## 2.0.1 (2016-07-06)
- Fix tests

## 2.0.0 (2016-07-05)
- Require call run() for init events loop

## 1.2.5 (2016-06-15)
- Fix MANIFEST.in

## 1.2.4 (2015-10-15)
- Fix support python 3

## 1.2.3 (2015-10-14)
- Remove 3.2 support
- Prepare travis

## 1.2.2 (2015-10-14)
- Fix readme

## 1.2.1 (2015-10-14)
- Remove bad examples
- Update readme

## 1.2.0 (2015-09-22)
- You can change the method that executes when an exception occurs
- Remove deprecated functions
- Send internally calls send_queue
- Official support python 3.5.0
- Permit change default send

## 1.1.3 (2015-08-14)
- Fix bug in add_subcribe

## 1.1.1 (2015-08-14)
- Try fix changelog in pypi

## 1.1.0 (2015-08-14)
- Refactor code
- Added new functions: send_queue, send_thread, send_blocking, add_subscribe

## 1.0.2 (2015-08-14)
- increase performance function send (19%+)
- increase performance subscribe (2%+)

## 1.0.1 (2015-08-13)
- fix pip install basicevents

## 1.0.0 (2015-08-13)
- Now you can run blocker way events
- break compatibility function send (check documentation)

## 0.1.5 (2015-08-12)
- update documentation

## 0.1.4 (2015-08-12)
- update documentation
- remove instant key in kwargs

## 0.1.3 (2015-08-12)
- Added changelog
- Auto convert md to rst in setup.py
