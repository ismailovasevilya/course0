def closest_mod_5(x):
    if x % 5 == 0:
        return x
    else:
        y=x
        while y % 5 != 0:
            y += 1
        return y