from functools import cache

@cache
def desiredPatternPossible(availableDesigns, desiredPattern):

    if len(desiredPattern) == 0:
        return 1
    
    ret = 0
    for pattern in availableDesigns:
        if desiredPattern[:len(pattern)] == pattern:
            # print("here", pattern, desiredPattern, desiredPattern[:len(pattern)], desiredPattern[len(pattern):])
            ret += desiredPatternPossible(availableDesigns, desiredPattern[len(pattern):])
    
    return ret
