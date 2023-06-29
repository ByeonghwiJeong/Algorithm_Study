class Queue:
  def __init__(self):
    self.items = []
    self.front_index = 0
  def enqueue(self, val):
    self.items.append(val)
  def dequeue(self):
    if self.front_index == len(self.items): # 현재 dequeue할 수 있는 값이 없음
      print("Queue is empty")
      return None
    else:
      x = self.items[self.front_index]
      self.front_index += 1
      return x
  def __len__(self):
    return len(self.items) - self.front_index
