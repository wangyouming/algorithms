
def hanoi(n, a, b, c):
    """
    Args:
        n: count of rings
        a: from column, left column
        b: helper column, middle column
        c: target column, right column
    """
    if n == 1:
        print(a, '-->', c)
    else:
        hanoi(n-1, a, c, b)
        print(a, '-->', c)
        hanoi(n-1, b, a, c)

if __name__ == '__main__':
    hanoi(5, 'A', 'B', 'C')