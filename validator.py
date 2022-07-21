import util
from state import State


def validate(problem, solution):
    '''
    Return true if `solution` is a valid plan for `problem`.
    Otherwise, return false.

    OBSERVATION: you should check action applicability,
    next-state generation and if final state is indeed a goal state.
    It should give you some indication of the correctness of your planner,
    mainly for debugging purposes.
    '''
    ' YOUR CODE HERE '
    initial_state = problem.init
    goal = problem.goal
    
    state = set()
    state = initial_state
    for i in range(len(solution)):
        action = solution[i]
        if not applicable(action, state):
            print("not applicable")
            print(i)
            return False
            
        else:
            state = successor(state, action)
            
            
    if not goal_test(state,goal):
        print("not goal state")
        print("goal: "+goal)
        print("Estado final: "+state)
        print("stado insterseccao goal: "+State(state).intersect(goal))
        print("diferenca stado insterseccao goal com goal: "+State(state).intersect(goal).difference(goal))
        print("intersecção stado goal = stado: "+State(state).intersect(goal)==State(state))
        print("intersecção stado goal = goal: "+State(state).intersect(goal)==State(goal))
        return False
      
    return True

def applicable(action, state):
    ''' Returnif a action is appicable given a state '''
    ' YOUR CODE HERE '
    applicable = False
    if State(state).intersect(action.precond) == action.precond:
        applicable = True
        return applicable
    else:
        applicable = False
        return applicable()
        
def successor(state, action):
    ''' Return the sucessor state generated by executing `action` in `state`. '''
    ' YOUR CODE HERE '
    return State(action.pos_effect).union(State(state).difference(action.neg_effect))
    #return State(action.pos_effect).union(state)

def goal_test(state,goal):
    ''' Return true if `state` is a goal state. '''
    ' YOUR CODE HERE '
    return State(state).intersect(goal)==State(goal)
