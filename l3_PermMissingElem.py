# lesson_3_TimeComplexity
# task_PermMissingElem_Easy -- O(N)
A = [2,3,1,5]

def solution(A):
    n = len(A)
    total = (n+1)*(n+2)/2
    summed = sum(A)
    
    return int(total)-summed