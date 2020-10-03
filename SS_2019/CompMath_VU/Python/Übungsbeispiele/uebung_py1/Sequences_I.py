def seq_a(N, n):
    if n == 0:
        return N
    else:
        tmp = seq_a(N, n - 1)

        if tmp % 2 == 0:
            return tmp // 2
        else:
            return 3 * tmp + 1
