# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    #utilizando uma pilha para a busca em profundidade
    stack = util.Stack()
    #conjunto para armazenar os estados visitados
    visitado = set()

    #inicia a busca a partir do estado inicial
    stack.push((problem.getStartState(), []))

    while not stack.isEmpty():
        estado, actions = stack.pop()

        #verifica se o estado atual é o objetivo
        if problem.isGoalState(estado):
            return actions

        #marca o estado como visitado
        if estado not in visitado:
            visitado.add(estado)
            #obtém os sucessores do estado atual
            sucessores = problem.getSuccessors(estado)
            for sucessor in sucessores:
                next_state, action, _ = sucessor
                if next_state not in visitado:
                    #adiciona o próximo estado e a ação à pilha
                    stack.push((next_state, actions + [action]))
    return []



def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    #inicializa com o nó inicial
    fila = util.Queue()
    fila.push((problem.getStartState(), []))
    #inicializa o conjunto de nós visitados
    visitado = set()
    
    #enquanto houver nós na fronteira
    while not fila.isEmpty():
        #remove o primeiro nó da fronteira
        node, path = fila.pop()
        
        #se o nó não foi visitado
        if node not in visitado:
            #marca o nó como visitado
            visitado.add(node)
            
            #se o nó for o objetivo, retorna o caminho até ele
            if problem.isGoalState(node):
                return path
            
            #para cada ação possível a partir do nó
            for next_node, action, cost in problem.getSuccessors(node):
                #adiciona o próximo nó à fronteira juntamente com o caminho até ele
                fila.push((next_node, path + [action]))
        return None

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    frontier = util.PriorityQueue()
    frontier.push((problem.getStartState(), [], 0), 0) 
    explored = set()

    while not frontier.isEmpty():
        node, actions, cost = frontier.pop()
        if problem.isGoalState(node):
            return actions
        if node not in explored:
            explored.add(node)
            for successor, action, stepCost in problem.getSuccessors(node):
                totalCost = cost + stepCost
                frontier.push((successor, actions + [action], totalCost), totalCost)

    return None


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
