# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
"""

import util
from game import Directions
class SearchProblem:
  """
  This class outlines the structure of a search problem, but doesn't implement
  any of the methods (in object-oriented terminology: an abstract class).
  
  You do not need to change anything in this class, ever.
  """
  
  def getStartState(self):
     """
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()
           

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first [p 85].
  
  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm [Fig. 3.7].
  
  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:
  """
  
  #print "Start:", problem.getStartState()
  #print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  #print "Start's successors:", problem.getSuccessors(problem.getStartState())


  nextState = (problem.getStartState(),0,0)
  explored = {}
  route = []
  print ''
  while not problem.isGoalState(nextState[0]):
    foundNext = False
    frontier = problem.getSuccessors(nextState[0])
    for each in frontier:
      if not each[0] in explored:
        route.append(nextState)
        explored[each[0]] = True
        nextState = each
        foundNext = True
        break     #this break is important. 
                  #it ignores the other children for now
                  #this way less nodes are expanded

    if foundNext:
      continue

    if not len(route):
      break
    nextState = route.pop()
    #stack.extend(problem.getSuccessors(nextState[0]))

  print route
  print len(route)
  print nextState

  route.append(nextState)
  s = Directions.SOUTH
  w = Directions.WEST
  e = Directions.EAST
  n = Directions.NORTH

  returningList = []
  for r in route[1:]:
    direction = r[1]
    #print direction
    if direction == 'West':
      returningList.append(w)
    if direction == 'East':
      returningList.append(e)
    if direction == 'North':
      returningList.append(n)
    if direction == 'South':
      returningList.append(s)
  

  return returningList
  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()


def breadthFirstSearch(problem):
  nextState = (problem.getStartState(),0,0)
  explored = {}
  childMap = {}
  q = []
  route = []
  q.insert(0, problem.getStartState())
  print ''
  while len(q):
    #print explored
    targetFound = False
    node = q.pop()
    explored[(node[0],node[3])] = True
    for child in problem.getSuccessors(node):
      #print child
      if not (child[0],child[3]) in explored:
        childMap[child] = node
        q.insert(0,child)
        if problem.isGoalState(child):
          targetFound = True
          break
    if targetFound:
      break

  parent = q[0]
  while parent in childMap:
    route.append(parent)
    parent = childMap[parent]

  #print route
  #print len(route)
  route = route[::-1]
  

  s = Directions.SOUTH
  w = Directions.WEST
  e = Directions.EAST
  n = Directions.NORTH

  returningList = []
  for r in route:
    direction = r[1]
    #print direction
    if direction == 'West':
      returningList.append(w)
    if direction == 'East':
      returningList.append(e)
    if direction == 'North':
      returningList.append(n)
    if direction == 'South':
      returningList.append(s)
  return returningList
  util.raiseNotDefined()
      
def uniformCostSearch(problem):

  nextState = (problem.getStartState(),0,0)
  explored = {}
  route = []
  print ''
  while not problem.isGoalState(nextState[0]):
    foundNext = False
    frontier = problem.getSuccessors(nextState[0])
    frontier = sorted(frontier, key = lambda k: k[2], reverse = True)
    for each in frontier:
      if not each[0] in explored:
        route.append(nextState)
        explored[each[0]] = True
        nextState = each
        foundNext = True
        break

    if foundNext:
      continue

    if not len(route):
      break
    nextState = route.pop()
    #stack.extend(problem.getSuccessors(nextState[0]))

  print route
  print len(route)
  print nextState

  route.append(nextState)
  s = Directions.SOUTH
  w = Directions.WEST
  e = Directions.EAST
  n = Directions.NORTH

  returningList = []
  for r in route[1:]:
    direction = r[1]
    #print direction
    if direction == 'West':
      returningList.append(w)
    if direction == 'East':
      returningList.append(e)
    if direction == 'North':
      returningList.append(n)
    if direction == 'South':
      returningList.append(s)
  

  return returningList
  "Search the node of least total cost first. "
  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  nextState = (problem.getStartState(),0,0)
  explored = {}
  route = []
  print ''
  while not problem.isGoalState(nextState[0]):
    foundNext = False
    frontier = problem.getSuccessors(nextState[0])
    frontier = sorted(frontier, key = lambda k: heuristic(k[0],problem), reverse = False)
    for each in frontier:
      #print each
      if not each[0] in explored:
        route.append(nextState)
        explored[each[0]] = True
        nextState = each
        foundNext = True
        break

    if foundNext:
      continue

    if not len(route):
      break
    nextState = route.pop()
    #stack.extend(problem.getSuccessors(nextState[0]))

  print route
  print len(route)
  print nextState

  route.append(nextState)
  s = Directions.SOUTH
  w = Directions.WEST
  e = Directions.EAST
  n = Directions.NORTH

  returningList = []
  for r in route[1:]:
    direction = r[1]
    #print direction
    if direction == 'West':
      returningList.append(w)
    if direction == 'East':
      returningList.append(e)
    if direction == 'North':
      returningList.append(n)
    if direction == 'South':
      returningList.append(s)
  

  return returningList
  util.raiseNotDefined()
    
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch