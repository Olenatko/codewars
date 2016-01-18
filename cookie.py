def cookie(x):
    if type(x) == type(str()):
        return "Who ate the last cookie? It was Zach!"
    if (type(x) == type(int())) or (type(x) == type(float())):
        return "Who ate the last cookie? It was Monica!"
    if type(x) == type(bool()):
        return "Who ate the last cookie? It was the dog!"
print(cookie("Ryan"))
print(cookie(2.3))
print(cookie(26))
print(cookie(True))
