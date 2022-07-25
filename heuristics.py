import util


def h_naive(state, planning):
    return 0


def h_add(state, planning):
    '''
    Return heuristic h_add value for `state`.

    OBSERVATION: It receives `planning` object in order
    to access the applicable actions and problem information.
    '''
    ' YOUR CODE HERE '
    import sys
    h = dict() 
    actions = planning.actions
    X = state
    for x in X:
        h[x] = 0
    change = True
    while change:
       
       actionsApplicable = planning.applicable(X)
       for a in actionsApplicable:
           X = planning.successor(X,a)
           for p in a.pos_effect:
               prev = h.get(p,sys.maxsize)
               h[p] = min(prev,(1+sum(h.get(pre, sys.maxsize) for pre in a.precond)))
               if prev == h[p]:
                   change = False
    return h


def h_max(state, planning):
    '''
    Return heuristic h_max value for `state`.

    OBSERVATION: It receives `planning` object in order
    to access the applicable actions and problem information.
    '''
    import sys
    h = dict() 
    actions = planning.actions
    X = state
    for x in X:
        h[x] = 0
    change = True
    while change:
       change = False
       actionsApplicable = planning.applicable(X)
       for a in actionsApplicable:
           X = planning.successor(X,a)
           for p in a.pos_effect:
               prev = h.get(p,sys.maxsize)
               h[p] = min(prev,(1+sum(h.get(pre, sys.maxsize) for pre in a.precond)))
               if prev != h[p]:
                   change = True
    return sum(h.get(i,sys.maxsize).values() for i in planning.problem.goal)
    ' YOUR CODE HERE '


def h_ff(state, planning):
    '''
    Return heuristic h_ff value for `state`.

    OBSERVATION: It receives `planning` object in order
    to access the applicable actions and problem information.
    '''
    util.raiseNotDefined()
    ' YOUR CODE HERE '
