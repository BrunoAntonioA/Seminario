import copy

class CPMP_Node():
  def __init__(self, data, parent, move=(0,0)):
    self.parent = parent
    self.data = data
    self.children = []
    self.cost = 0
    self.move = move
 
  def addChildren(self):
    for move in self.data.possibleMoves:
      copiedState = copy.deepcopy(self.data)
      copiedState.movement(move[0], move[1])
      childNode = CPMP_Node(copiedState, self, (move[0], move[1]))
      childNode.cost = self.cost + 1
      self.children.append(childNode)

  # This function iterates trought the node s tree path & extract his states & moves
  def getData(self, states, initMoves, finalMoves):
    while self.parent:
      self.parent.data.compactState()
      self.parent.data.normalizeState()
      self.parent.data.elevateState()
      flatStacks = []
      for stack in self.parent.data.stacks:
        for item in stack:
          flatStacks.append(item)
      states.append(flatStacks)
      initMoves.append(self.move[0])
      finalMoves.append(self.move[1])
      self = self.parent
    return (states, initMoves, finalMoves)

  def getData2(self, states, initMoves, finalMoves):
    while self.parent:
      self.parent.data.fillStacksWithCeros()
      self.parent.data.normalizeState()
      flatStacks = []
      for stack in self.parent.data.stacks:
        for item in stack:
          flatStacks.append(item)
      states.append(flatStacks)
      initMoves.append(self.move[0])
      finalMoves.append(self.move[1])
      self = self.parent
    return (states, initMoves, finalMoves)
