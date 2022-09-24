def tower_hanoi(n, a, b, c):
    # Base Case
    if(n == 1):
        print('move first disk from', a, 'to', c)
        return 

    # Induction Hypothesis
    tower_hanoi(n - 1, a, c, b)    

    print('move',n, 'nth disk from', a, 'to', c)

    tower_hanoi(n - 1, b, a, c)

if __name__ == '__main__':
    n = 2
    tower_hanoi(n, 'a', 'b', 'c')
