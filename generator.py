def generator(From, To, Step):
    if Step == 0:
        return []
    key = 1
    if From > To:
        Step = -Step
        key = -key
    generated = list(range(From, To + key, Step))
    return generated