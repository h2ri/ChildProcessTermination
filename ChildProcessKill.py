import signal
import psutil

MEMORY_IN_KB = 4000

def terminate_child_process(parent_pid):
    try:
      parent = psutil.Process(parent_pid)
    except psutil.NoSuchProcess:
      return
    children = parent.children()
    for process in children:
      if process.memory_info().rss/1024 > MEMORY_IN_KB :
          print(process)
          process.terminate()

file = open("input.txt", "r")
with open("input.txt") as f:
    parent_process_id = int(f.readlines()[0])
terminate_child_process(parent_process_id)
