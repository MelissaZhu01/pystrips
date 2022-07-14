import util

from state import State
from node  import Node


class Frontier(object):
    '''
    Frontier class implement a search frontier using a
    PriorityQueue for ordering the nodes and a set for
    constant-time checks of states in frontier.

    OBSERVATION: it receives as input a function `f` that
    itself receives a node and returns the priority for
    the given node. Check util.PriorityQueueWithFunction for
    more details.
    '''

    def __init__(self, f):
        self._queue = util.PriorityQueueWithFunction(f)
        self._set = set()

    def __contains__(self, node):
        ''' Return true if `node.state` is in the frontier. '''
        return node.state in self._set

    def __len__(self):
        ''' Return the number of nodes in frontier. '''
        assert(len(self._queue) == len(self._set))
        return len(self._queue)

    def is_empty(self):
        ''' Return true if frontier is empty. '''
        return self._queue.isEmpty()

    def push(self, node):
        ''' Push `node` to frontier. '''
        self._queue.push(node)
        self._set.add(node.state)

    def pop(self):
        ''' Pop `node` from frontier. '''
        node = self._queue.pop()
        self._set.remove(node.state)
        return node

    def __str__(self):
        ''' Return string representation of frontier. '''
        return str(self._queue)


class ProgressionPlanning(object):
    '''
    ProgressionPlanning class implements all necessary components
    for implicitly generating the state space in a forward way (i.e., by progression).self
    '''

    def __init__(self, domain, problem):
        self._problem = problem
        self._all_actions = problem.ground_all_actions(domain)

    @property
    def problem(self):
        return self._problem

    @property
    def actions(self):
        return self._all_actions

    def applicable(self, state):
        ''' Return a list of applicable actions in a given `state`. '''
        ' YOUR CODE HERE '
        applicable = list()
        for action in self.actions:
            if State(state).intersect(action.precond) == action.precond:
                applicable.append(action)
        return applicable
            
    def successor(self, state, action):
        ''' Return the sucessor state generated by executing `action` in `state`. '''
        ' YOUR CODE HERE '
        return State(action.pos_effect).union(State(state).difference(action.neg_effect))
        #return State(action.pos_effect).union(state)

    def goal_test(self, state):
        ''' Return true if `state` is a goal state. '''
        ' YOUR CODE HERE '
        return State(state).intersect(self.problem.goal) == State(state)

    def solve(self, W, heuristics):
        '''
        Implement best-first graph-search WA*. It receives `W` the weight of WA*
        and `heuristics` a function that receives a state s and the planning object (ie., self)
        and returns h(s). Check heuristics.py for more information.

        If problem has solution, return a triple (plan, num_explored, num_generated) where:
         - `plan` is a sequence of actions;
         - `num_explored` is the number of states explored; and
         - `num_generated` is the nubmer of states generated.
        Otherwise, it should return None.

        OBSERVATION: a state is 'explored' when it is removed from the frontier and
        a state is 'generated' when it is the successor state generated by an action
        regardless whether or not it is in the explored set or already in the frontier.
        '''
        plan = []
        num_explored = 0
        num_generated = 0
        ' YOUR CODE HERE '
        opened = list()
        max_step = 10
        goal_state = self.problem.goal
        initialNode = Node(State(self.problem.init))
        frontier = Frontier(lambda searchNode:(searchNode.g + W*searchNode.h))
        frontier.push(initialNode)
        reached = False
        for i in range(max_step):
            sNode = frontier.pop()
            opened.append(sNode.state)
            if sNode.state.intersect(goal_state) == goal_state:
                reached = True
                num_explored = opened.length
                break
            actionsApplicable = self.applicable(sNode.state)
            for action in actionsApplicable:
                stateSon = self.successor(sNode.state, action)
                if stateSon in opened:
                    continue
                nodeSon = Node(stateSon,
                               action,
                               sNode,
                               sNode.g + 1,
                               heuristics(stateSon, self)) 
                frontier.push(nodeSon)
                num_generated = num_generated+1
            if frontier.is_empty():
                print ('Problem does not have a solution')
                return None
        plan = sNode.path() 
        return (plan, num_explored, num_generated)
        
        
