import math

def solution(A, B, K):
    return B//K - math.ceil(A/K) + 1
