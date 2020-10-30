#2
def check_mod(x):
    return {
        x <= -1 : -1,
        x == 0 : 0,
        x >= 1 : 1
    }[True]
