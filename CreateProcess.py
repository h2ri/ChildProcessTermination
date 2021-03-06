import signal
import psutil
import os
import time

def child():
   print('\nA new child ',  os.getpid())
   time.sleep(100)
   os._exit(0)

def parent():
   while True:
      newpid = os.fork()
      if newpid > 0:
         child()
      else:
         pids = (os.getpid(), newpid)
         print("parent: %d, child: %d\n" % pids)
      reply = input("q for quit / c for new fork")
      if reply == 'c':
          continue
      else:
          break

parent()
