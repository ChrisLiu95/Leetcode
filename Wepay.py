def alert(inputs, windowSize, allowedIncrease):
    total = sum(inputs[:windowSize])
    MaxWindow = total
    MaxNumber = max(inputs[:windowSize])
    pre = total

    for i in range(windowSize, len(inputs)):
        total = total - inputs[i - windowSize] + inputs[i]

        if total > pre * allowedIncrease:
            return True

        pre = min(pre, total)
        MaxWindow = max(MaxWindow, total)
        MaxNumber = max(MaxNumber, inputs[i])

    if MaxNumber > (MaxWindow / windowSize) * allowedIncrease:
        return True
    return False
