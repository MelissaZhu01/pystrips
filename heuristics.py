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
       change = False
       actionsApplicable = planning.applicable(X)
       for a in actionsApplicable:
           X = X.union(a.pos_effect)
           for p in a.pos_effect:
               prev = h.get(p,sys.maxsize)
               h[p] = min(prev,(1+sum(h.get(pre, sys.maxsize) for pre in a.precond)))
               if prev != h[p]:
                   change = True
    
    return sum(h.get(i,sys.maxsize) for i in planning.problem.goal)


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
           X = X.union(a.pos_effect)
           for p in a.pos_effect:
               prev = h.get(p,sys.maxsize)
               h[p] = min(prev,(1+sum(h.get(pre, sys.maxsize) for pre in a.precond)))
               if prev != h[p]:
                   change = True
    return h[max(h,key = h.get)]
    ' YOUR CODE HERE '


def h_ff(state, planning):
    '''
    Return heuristic h_ff value for `state`.

    OBSERVATION: It receives `planning` object in order
    to access the applicable actions and problem information.
    '''
    graphplan = dict() #graphplan relaxed
    actions = planning.actions
    X = state
    goal = planning.problem.goal
    isGoal = False
    if X.intersect(goal) == goal: #ja estamos na meta entao o comprimento (a quantidade) de acoes necessaria eh zero
        return 0
    level = 0
    graphplan[(level,'state')] = X
    # expandir graphplan
    while not isGoal:
        actionsApplicable = planning.applicable(X,actions)
        level += 1
        for a in actionsApplicable:
            X = planning.successorRelaxed(X,a) 
            if X.intersect(goal) == goal:
                isGoal = True
                break
        graphplan[(level,'state')] = X
        graphplan[(level,'action')] = actionsApplicable
    #busca regressiva - procurando caminho para estado inicial até estado final
    thisLevelGoals = set()
    thisLevelGoals = thisLevelGoals.union(goal)
    relaxedActions = set()
    while (level > 0):
        prevLevelGoals = set()
        for tg in thisLevelGoals:
            if tg in graphplan[level-1,'state']:
                prevLevelGoals.add(tg)
            else:
                for a in graphplan[level,'action']:
                    if tg in a.pos_effect:
                        prevLevelGoals = prevLevelGoals.union(a.precond)
                        relaxedActions.add(a)
                        break 
        level -= 1
        thisLevelGoals = prevLevelGoals.copy()
    return len(relaxedActions)
    ' YOUR CODE HERE '
