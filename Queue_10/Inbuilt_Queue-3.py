import queue 

q = queue.Queue()
q.put(1)
q.put(12)
q.put(13)
q.put(14)
q.put(15)

while(q.empty() is False):
    print(q.get())
