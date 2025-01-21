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

def depthFirstSearch(problem: SearchProblem):
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
    "*** YOUR CODE HERE ***"
    start_state = (problem.getStartState(), [], 0)
    if problem.isGoalState(start_state[0]):
        return start_state[1]
    else:
        DFS_stack = util.Stack()
        DFS_stack.push(start_state)
        visited_nodes = set()
        while(DFS_stack.isEmpty() == False):
            popped_state, state_action, state_cost = DFS_stack.pop()
            if popped_state not in visited_nodes:
                visited_nodes.add(popped_state)
                if problem.isGoalState(popped_state):
                    return state_action
                popped_successors = problem.getSuccessors(popped_state)
                for successor, action, cost in popped_successors:
                    new_actions = state_action + [action]
                    DFS_stack.push((successor, new_actions, cost))
        return []

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    start_state = (problem.getStartState(), [], 0)
    if problem.isGoalState(start_state[0]):
        return start_state[1]
    else:
        BFS_queue = util.Queue()
        BFS_queue.push(start_state)
        visited_nodes = set()
        while(BFS_queue.isEmpty() == False):
            popped_state, state_action, state_cost = BFS_queue.pop()
            if popped_state not in visited_nodes:
                visited_nodes.add(popped_state)
                if problem.isGoalState(popped_state):
                    return state_action
                popped_successors = problem.getSuccessors(popped_state)
                for successor, action, cost in popped_successors:
                    new_actions = state_action + [action]
                    BFS_queue.push((successor, new_actions, cost))
        return []

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    start_state = (problem.getStartState(), [], 0)
    if problem.isGoalState(start_state[0]):
        return start_state[1]
    else:
        UCS_queue = util.PriorityQueue()
        UCS_queue.push(start_state, 0)
        costs = {problem.getStartState(): 0}
        visited_nodes = set()
        while(UCS_queue.isEmpty() == False):
            popped_state, state_action, state_cost = UCS_queue.pop()
            if problem.isGoalState(popped_state):
                return state_action
            visited_nodes.add(popped_state)
            popped_successors = problem.getSuccessors(popped_state)
            for successor, action, cost in popped_successors:
                new_cost = costs[popped_state] + cost
                if successor not in visited_nodes and (successor not in costs or new_cost < costs[successor]):
                    costs[successor] = new_cost
                    new_actions = state_action + [action]
                    UCS_queue.push((successor, new_actions, new_cost), new_cost)
        return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    start_state = (problem.getStartState(), [], 0)
    if problem.isGoalState(start_state[0]):
        return start_state[1]
    else:
        aStar_queue = util.PriorityQueue()
        aStar_queue.push(start_state, 0)
        costs = {problem.getStartState(): 0}
        visited_nodes = set()
        while(aStar_queue.isEmpty() == False):
            popped_state, state_action, state_cost = aStar_queue.pop()
            if problem.isGoalState(popped_state):
                return state_action
            visited_nodes.add(popped_state)
            popped_successors = problem.getSuccessors(popped_state)
            for successor, action, cost in popped_successors:
                new_cost = costs[popped_state] + cost
                if successor not in visited_nodes and (successor not in costs or new_cost < costs[successor]):
                    costs[successor] = new_cost
                    new_actions = state_action + [action]
                    priority_cost = new_cost + heuristic(successor, problem)
                    aStar_queue.push((successor, new_actions, new_cost), priority_cost)
        return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
