def solution(S, P, Q):
    impactf = {"A": 1, "C": 2, "G": 3, "T": 4}
    dna = ""
    presum = [[0, 0, 0, 0]]
    for s in S:
        presum.append([presum[-1][i] + 1 if impactf[s]-1 == i else presum[-1][i] 
                       for i in range(4)])
    result = []
    for p, q in zip(P, Q):
        counts = map(lambda x, y: x - y, presum[q+1], presum[p])
        for i, c in enumerate(counts):
            if c > 0:
                result.append(i+1)
                break
    return result
