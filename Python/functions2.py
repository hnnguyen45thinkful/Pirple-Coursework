def test(x, y, z):
    x = int(x)
    y = int(y)
    z = int(z)


    if x == y or x == z:
        return True
    elif y == z:
        return True
    else:
        return False

print(test(6, 5, 4))