print('#', '-'*64, '#', '\n')

# -------------------------------- #

def verschmelzen(A, B):

    C = [0] * (len(A) + len(B))

    i = 1
    j = 1

    for k in range(1, len(A) + len(B) + 1):

        if j > len(B) or (i <= len(A) and A[i-1] <= B[j-1]):

            C[k-1] = A[i-1]
            i = i + 1

        else:

            C[k-1] = B[j-1]
            j = j + 1

    return C

# -------------------------------- #

"""

A = [1, 3, 5, 7]
B = [2, 4, 6]
C = verschmelzen(A, B)

print(C)

"""

# -------------------------------- #

def get_runs(A):

    runs = []

    while len(A) != 0:

        run = [A.pop(0)]

        while len(A) != 0:

            if run[-1] <= A[0]:
                run.append(A.pop(0))
            else:
                break

        runs.append(run)

    return runs

# -------------------------------- #

"""

A = [2, 4, 3, 1, 7, 6, 8, 9, 0, 5]
runs = get_runs(A)

print(runs)

"""

# -------------------------------- #

def natural_merge_sort(A):

    runs = get_runs(A)
    print(runs)
    print()

    A = []
    for run in runs:

        A = verschmelzen(A, run)
        print(A)

    return A

# -------------------------------- #

A = [2, 4, 3, 1, 7, 6, 8, 9, 0, 5]
A_sorted = natural_merge_sort(A)

print()
print(A_sorted)
print()

# -------------------------------- #

print('#', '-'*64, '#', '\n')
