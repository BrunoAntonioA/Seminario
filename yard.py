import random

class Yard:
  def __init__(self, x, y, d, a, b):
    self.max_height = y
    self.maxValue = 0
    self.minCost = 0
    self.stacks = [] 
    self.stackValues = []
    self.possibleMoves = []
    self.initYard(x, y, d, a, b)
 
  #Function to initialize a Yard 
  def initYard(self, x, y, discount, a, b):
    for i in range(x):
      stack = []
      for j in range(y - discount):
        n = random.randint(a, b)
        stack.append(n)
        if n > self.maxValue:
          self.maxValue = n
      self.stackValues.append(0)
      self.stacks.append(stack)
    self.updatePossibleMoves()
    self.getStackValues()
    return self
 
  def evalState(self):
    for value in self.stackValues:
      if value != 0:
        return 0
    return 1
 
  #Function to get stackValue per each stack
  def getStackValues(self):
    minCost = 0
    for i in range(len(self.stacks)):
      countFlag = False
      count = 0
      for j in range(len(self.stacks[i])):
        if j == 0:
          continue
        if self.stacks[i][j] > self.stacks[i][j-1]:
          countFlag = True
        if countFlag:
          count = count + 1
      self.stackValues[i] = count
      minCost = minCost + count
    self.minCost = minCost
    return self.stackValues
 
 
  #Function to update possible movements
  def updatePossibleMoves(self):
    self.possibleMoves = []
    sLen = len(self.stacks)
    for i in range(sLen):
      for j in range(sLen):
        if i == j:
          continue
        else:
          if( len(self.stacks[i]) > 0 and len(self.stacks[j]) < self.max_height):
            self.possibleMoves.append((i, j))
    return self.possibleMoves
 
  #Function to do a movement
  def movement(self, i, j):
    if len(self.stacks[i]) != 0 and len(self.stacks[j]) < self.max_height:
      self.stacks[j].append(self.stacks[i].pop())
      self.updatePossibleMoves()
      self.getStackValues()
    else:
      print("No se puede realizar este movimiento")
    return self
 
  #Function to normalize stacks values
  def normalizeState(self):
    for i in range(len(self.stacks)):
      for j in range(len(self.stacks[i])):
        self.stacks[i][j] = self.stacks[i][j] / self.maxValue 
    return self                     
 
  #Quizas se puede utilizar una estructura mejor para guardar los datos ordenados  
  #Function to compact stacks values
  def compactState(self):
    sort = []
    for stack in self.stacks:
      for container in stack:
        if not container in sort:
          sort.append(container)
    sort = sorted(sort)
    maxValue = 0
    for i in range(len(self.stacks)):
      for j in range(len(self.stacks[i])):
        self.stacks[i][j] = sort.index(self.stacks[i][j])
        if self.stacks[i][j] > maxValue:
          maxValue = self.stacks[i][j]
 
  #Function to elevate the yard
  def elevateState(self):
    for stack in self.stacks:
      while len(stack) < self.max_height:
        stack.insert(0, 1)
    return self

  def fillStacksWithCeros(self):
    for stack in self.stacks:
      while len(stack) < self.max_height:
        stack.append(0)
    return self