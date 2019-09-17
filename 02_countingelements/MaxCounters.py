def solution(N, A):
    counter = [0] * N
    mustmax = 0
    currmax = 0
    for a in A:
        if a == N+1:
            mustmax = currmax
        else:
            counter[a-1] = max(mustmax + 1, counter[a-1] + 1)
            currmax = max(counter[a-1], currmax)
    for i in range(N):
        counter[i] = max(mustmax, counter[i])
    return counter
