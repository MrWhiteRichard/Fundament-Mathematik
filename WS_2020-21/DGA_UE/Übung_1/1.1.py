# ---------------------------------------------------------------- #

tab = ' '*4

# ---------------------------------------------------------------- #

def selection_sort(A):

    """
    Selection Sort:
    der Algorithmus sucht zunächst das kleinste Element und bringt es an die erste Position.
    Anschließend sucht er das zweitkleinste Element und bringtes an die zweite Position, usw.
    """

    print('#', '-'*64, '#', '\n')

    print('n := A.Länge =', len(A), '\n')
    n = len(A)

    for i in range(n-1):
        print('i :=', i)

        print(f'A_{i} =', A)

        print(tab, end = '')
        print(f'i_min :=', i)
        i_min = i

        for j in range(i+1, n):
            print()
            print(tab, end = '')
            print('j :=', j)

            if A[j] < A[i_min]:
                print()
                print(tab, end = '')
                print(tab, end = '')
                print(f'A[j] = A[{j}] = {A[j]} < A[i_min] = A[{i_min}] = {A[i_min]}')

                print(tab, end = '')
                print(tab, end = '')
                print(f'i_min :=', j)
                i_min = j

                print()

        print(tab, end = '')
        print(f'A[i], A[i_min] := A[i_min] = A[{i_min}] = {A[i_min]}, A[i] = A[{i}] = {A[i]}')
        A[i], A[i_min] = A[i_min], A[i]

        print(f'A\'_{i} =', A)
        print()

    print('#', '-'*64, '#', '\n')
    return A

# ---------------------------------------------------------------- #

def bubble_sort(A):

    """
    Bubble-Sort:
    Der Algorithmus vergleicht der Reihe nach je zwei benachbarte Zahlenund vertauscht diese, falls sie nicht in der richtigen Reihenfolge angeordnet sind.
    Dieses Verfahren wird so lange wiederholt, bis alle Zahlen der Eingabe sortiert sind.
    """

    print('#', '-'*64, '#', '\n')

    print('n := A.Länge =', len(A), '\n')
    n = len(A)

    for i in range(n):
        print('i :=', i)

        print(f'A_{i} =', A)

        for j in range(n-(i+1)):
            print()
            print(tab, end = '')
            print('j :=', j)

            print(tab, end = '')
            print('A_' + r'{' + str(i) + ', ' + str(j) + r'} =', A)

            if A[j+1] < A[j]:
                print()
                print(tab, end = '')
                print(tab, end = '')
                print(f'A[j+1] = A[{j+1}] = {A[j+1]} < A[j] = A[{j}] = {A[j]}')

                print(tab, end = '')
                print(tab, end = '')
                print(f'A[j], A[j+1] := A[j+1] = A[{j}] = {A[j]}, A[j] = A[{j+1}] = {A[j+1]}')
                A[j], A[j+1] = A[j+1], A[j]

                print()

            print(tab, end = '')
            print('A\'_' + r'{' + str(i) + ', ' + str(j) + r'} =', A)
            print()

        print(f'A\'_{i} =', A)
        print()

    print('#', '-'*64, '#', '\n')
    return A

# ---------------------------------------------------------------- #

A = [6, 77, 45, 103, 4, 17]

A_selection_sorted = selection_sort(A)
print('Selection Sort liefert ...', A_selection_sorted, '\n')

A = [6, 77, 45, 103, 4, 17]

A_bubble_sorted = bubble_sort(A)
print('Bubble Sort liefert ...', A_bubble_sorted, '\n')

# ---------------------------------------------------------------- #
