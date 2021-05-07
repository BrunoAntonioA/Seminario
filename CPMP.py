import copy
import numpy as np

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
    return states, initMoves, finalMoves


  # This function iterates trought the node s tree path & extract his states & moves
  def get_data(self, states, init_moves, final_moves, compact, norm, elev):
    while self.parent:
      self.parent.data.fillStacksWithCeros()
      if compact:
        self.parent.data.compactState()
      if norm:
        self.parent.data.normalizeState()
      if elev:
        self.parent.data.elevateState()
      flatStacks = []
      max = -1
      for stack in self.parent.data.stacks:
        if len(stack) > max:
          max = len(stack)
        elif len(stack) == max:
          max = -1
        for item in stack:
          flatStacks.append(item)
      for val in self.parent.data.stackValues:
        flatStacks.append(val)
      flatStacks.append(self.parent.data.minCost)
      flatStacks.append(max)
      states.append(flatStacks)
      init_moves.append(self.move[0])
      final_moves.append(self.move[1])
      self = self.parent
    return states, init_moves, final_moves