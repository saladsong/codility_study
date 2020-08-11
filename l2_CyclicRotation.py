# lesson_2_Arrays
# task_CyclicRotation_Easy
A = [3,8,9,7,6]
K = 3

def solution(A, K):
    res = [0]*len(A)

    for idx in range(len(A)):
        new_idx = (idx+K) % len(A)
        res[new_idx] = A[idx]

    return res