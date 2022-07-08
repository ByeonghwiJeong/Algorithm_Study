from queue import Queue

def Josephus(n, k):
  Q = Queue()
  for v in range(1, n+1):       
    Q.enqueue(v)
  while len(Q) > 1:
    for i in range(1, k):
      Q.enqueue(Q.dequeue())
    Q.dequeue() # k-th number is deleted
  return Q.dequeue() # len(Q) == 1

print(Josephus(6,2))