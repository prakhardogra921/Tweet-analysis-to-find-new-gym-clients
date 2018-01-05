__author__ = 'prakhardogra'
def check(x,y):
    if x == 0:
        if y > 10:
            return False
        return True
    if y/x >= 5:
        return False
    return True