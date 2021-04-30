from yard import Yard
from CPMP import CPMP_Node
import dtls
import pandas as pd

def dataGenerator(x, y, d, n, opt=1):
  states = []
  initMoves = []
  finalMoves = []
  for i in range(n):
    yard = Yard(x, y, d)
    node = CPMP_Node(yard, None)
    result = dtls.dlts_lds(node)
    if opt == 1:
      result.getData(states, initMoves, finalMoves)
    else:
      result.getData2(states, initMoves, finalMoves)
  return (states, initMoves, finalMoves)

def generateDataFrameIntoCSV(dfname, opt,  x, y, d, n):
  states, initMoves, finalMoves = dataGenerator(x, y, d, n, opt)
  dataTrain = pd.DataFrame(states) 
  dataTrain.insert(0, column = "initMove", value = pd.DataFrame(initMoves))
  dataTrain.insert(0, column = "finalMove", value = pd.DataFrame(finalMoves))
  dataTrain.to_csv(dfname)

def importDf(path):
  df = pd.read_csv(path)
  labels1 = df.pop('initMove')
  labels2 = df.pop('finalMove')
  return df, labels1, labels2, df.shape

def swapDataStacks(states, initMoves, finalMoves):
  for i in range(len(states)):
    states[i], initMoves[i], finalMoves[i] = swapStacks(states[i], initMoves[i], finalMoves[i])
  return states
 
def swapStacks(state, origin, destiny):
  if origin != 0:
    aux = state[0]
    state[0] = state[origin]
    state[origin] = aux
 
    if destiny == 0:
      destiny = origin
  
  return state, origin, destiny

#generateDataFrameIntoCSV("data/experimento-1.csv", 1, 4, 4, 2, 50)
#generateDataFrameIntoCSV("experimento-2-train-5000.csv", 2, 4, 4, 2, 5000)
#generateDataFrameIntoCSV("experimento-1-test-3000.csv", 1, 4, 4, 2, 3000)
#generateDataFrameIntoCSV("experimento-2-test-3000.csv", 2, 4, 4, 2, 3000)