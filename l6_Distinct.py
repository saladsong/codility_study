# lesson_6_Sorting
# task_Distinct_Easy -- O(N)
A = [2,1,1,2,3,1]

def solution(A):
    res = dict()
    for i in A:
        if i not in res:
            res[i] = 1
            
    return len(res)