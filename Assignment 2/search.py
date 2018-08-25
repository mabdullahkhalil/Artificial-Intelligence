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
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"


    points = util.Stack()
    direct=util.Stack()
    cost=util.Stack()

    directions=[]
    nodes_cost=[]

    point=problem.getStartState();
    points.push((problem.getStartState()))
    direct.push(directions)
    cost.push(nodes_cost)

    visited=[]


    while not points.isEmpty():
        node=points.pop()
        action=direct.pop()
        costt=cost.pop()

        if node in visited:
            continue;

        if problem.isGoalState(node):
            return action;

        visited.append(node)
        successors=problem.getSuccessors(node)

        for successor in successors:
                points.push(successor[0])
                direct.push(action+[successor[1]])
                cost.push(costt)

    return []


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    points = util.Queue()
    direct=util.Queue()
    cost=util.Queue()

    directions=[]
    nodes_cost=[]

    point=problem.getStartState();
    points.push(point)
    direct.push(directions)
    cost.push(nodes_cost)

    visited=[]


    while not points.isEmpty():
        currpoint=points.pop()
        action=direct.pop()
        costt=cost.pop()

        if currpoint in visited:
            continue;

        if problem.isGoalState(currpoint):
            return action;

        visited.append(currpoint)
        successors=problem.getSuccessors(currpoint)

        for successor in successors:
                points.push(successor[0])
                direct.push(action+[successor[1]])
                cost.push(costt)

    return []

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"



    main_queue=util.PriorityQueue()


    # took help in this part from a friend that passign 3 values in the main_queue.
    visitedpoint=[]

    startingpoint = (problem.getStartState(),0,[])
    main_queue.push(startingpoint,0)

    while not main_queue.isEmpty():
        (currentpoint, costpoint, action) = main_queue.pop()


        if problem.isGoalState(currentpoint):
            return action

        if currentpoint in visitedpoint:
            continue;

        visitedpoint.append(currentpoint)
        successors = problem.getSuccessors(currentpoint)

        for successor in successors:
            new_point=((successor[0]),costpoint+successor[2],action + [successor[1]])
            main_queue.push(new_point,costpoint+successor[2])

    return []



    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    main_queue = util.PriorityQueue()
    visitedpoint=[]

    startingpoint = (problem.getStartState(),0,[])
    main_queue.push(startingpoint,0+heuristic(startingpoint[0],problem))

    while not main_queue.isEmpty():
        (currentpoint, costpoint, action) = main_queue.pop()


        if problem.isGoalState(currentpoint):
            return action

        if currentpoint in visitedpoint:
            continue;

        visitedpoint.append(currentpoint)
        successors = problem.getSuccessors(currentpoint)

        for successor in successors:
            new_point=((successor[0]),costpoint+successor[2],action + [successor[1]])
            main_queue.push(new_point,costpoint+successor[2]+heuristic(new_point[0],problem))

    return []

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
