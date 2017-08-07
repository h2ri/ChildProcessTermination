import signal
import psutil
import os

MEMORY_IN_KB = 4000

def kill_child_processes(parent_pid):
    try:
      parent = psutil.Process(parent_pid)
    except psutil.NoSuchProcess:
      return
    children = parent.children(recursive=True)
    print(children)
    for process in children:
      if process.memory_info().rss/1024 > MEMORY_IN_KB :
          process.terminate()

file = open("input.txt", "r")
with open("input.txt") as f:
    parent_process_id = int(f.readlines()[0])
kill_child_processes(parent_process_id)
