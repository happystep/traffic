def LoopDay(a, b, c):
    currentDict = {}
    firstDay = []
    for x in range(a, b):
        currentDict = c[x]
        firstDay.append(currentDict)

    return firstDay