# lesson_4_CountingElements
# task_FrogRiverOne_Easy -- O(N)
A = [1,3,1,4,2,3,5,4]
X = 5

def solution(X, A):
    res = dict()

    for idx in range(len(A)):
        if A[idx] not in res:
            res[A[idx]] = 1
            if len(res) == X:
                return idx
    
    return -1