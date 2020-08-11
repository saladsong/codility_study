# lesson_2_Arrays
# task_OddOccurrences_Easy -- O(N) or O(N*logN)
A = [9,3,9,3,9,7,9]

def solution(A):
    res = {}

    for item in A:
        if item not in res:
            res[item] = 1
        else:
            del res[item]
    
    return max(res)