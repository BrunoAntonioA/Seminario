from queue import PriorityQueue

#Recibe un estado dentro de un CPMP_Node y retorna un estado resuelto (por ahora)
def dlts_lds(s):
  count = 0
  q = PriorityQueue(0)
  addedStates = set()
  q.put((s.cost + s.data.minCost, count, s))
  count = count + 1
  while not q.empty():
    s = q.get()
    s = s[2]
    if s.data.evalState():
      return s
    s.addChildren()
    for child in s.children:
      if not child in addedStates:
        hlb = child.cost + s.data.minCost
        addedStates.add(child)
        q.put((hlb, count, child))
        count += 1